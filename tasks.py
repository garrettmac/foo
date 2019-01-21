from invoke import task
from os import environ
import os
from sys import exit
import subprocess
import shutil
import glob
import boto3
import json
import yaml

def sanity_check(ctx):
    if environ.get('ARTIFACT_DEPLOY_REGION') is None:
        exit("Environment variable ARTIFACT_DEPLOY_REGION not set")
    ctx.travis_pull_request = environ.get('TRAVIS_PULL_REQUEST')
    if ctx.travis_pull_request is None or ctx.travis_pull_request == 'false':
        print("NOT a pull request")
        if environ.get('TRAVIS_BRANCH') == 'master':
            ctx.travis_pull_request = 'master'
        else:
            exit(0)
    else:
        print("Found pull request number via environment variable: [TRAVIS_PULL_REQUEST={}]".format(
            ctx.travis_pull_request))


def init(ctx):
    ctx.artifact_deploy_region = environ.get('ARTIFACT_DEPLOY_REGION', 'us-west-2')
    ctx.github_base_url = "https://github.com"
    ctx.travis_base_url = "https://travis-ci.com"



        # We will s3 sync all build assets to this folder
    if env_name:
        artifact_builds_s3_object_folder = "ecom/client/webApp/environments/{}/{}/{}".format(env_name, name, tag)
    else:
        tag = 'master' if ctx.travis_pull_request == 'master' else 'pr-{}'.format(ctx.travis_pull_request)
        artifact_builds_s3_object_folder = "ecom/client/webApp/distributions/{}/{}".format(name, tag)

    ssr_entry_file = 'index.js'
    ssr_dependency_dir = 'node_modules'
    build_dir = 'build'
    dist_file = '{}.zip'.format(ctx.rev)
    latest_file = 'latest'

    ctx.run('zip -r {}/{} {} {}/ {}/'.format(
        build_dir,
        dist_file,
        ssr_entry_file,
        ssr_dependency_dir,
        build_dir), hide=True)

    ctx.run('aws --region {} s3 cp {}/{} s3://{}/{}/{}'.format(
        ctx.artifact_deploy_region,
        build_dir,
        dist_file,
        ctx.artifact_deploy_s3_bucket,
        artifact_builds_s3_object_folder,
        dist_file))

    """ We indicate which was the last build by writing the current git short SHA to a file called 'latest' """
    s3_client = boto3.client('s3')
    s3_client.put_object(
        Body=bytes(ctx.rev, 'utf-8'),
        Key='{}/latest'.format(artifact_builds_s3_object_folder),
        Bucket=ctx.artifact_deploy_s3_bucket, Metadata=meta_data
    )

    return artifact_builds_s3_object_folder



@task()
def package(ctx):
    """
    Packaging consists of:

    1. Building the web app
    3. Compress all of the files from the web app build
    5. Distribute the web app to the client builds bucket location

     The result is that the following artifacts / files will be in S3:

     contents of `./build/` will be synced to:

     lll-testing-static-clients/ecom/client/<path>/distributions/my-app/pr-<PR_NUMBER>

    :return:
    """
    """ We use the current commit's short SHA1 fingerprint to name the artifact. """
    ctx.rev = ctx.run('git rev-parse --short HEAD').stdout.strip()

    """ Perform sanity check to make sure that we can build safely and that we have some build related env vars set. """
    sanity_check(ctx)
    init(ctx)

    """ Now we distribute the web app and create a sentry release"""
    ctx.artifact_deploy_s3_bucket = 'lll-testing-static-clients'
    distribute(ctx, 'my-app')
