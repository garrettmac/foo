#! /bin/sh

set -e

## env vars
# SLUG - repo name, in the form "OWNER/REPO"
# SITE - org or com, defaults to com

# OWNER=${SLUG%%/*}
# # REPO=${SLUG##*/}
# REPO='foo'
PAYLOAD=''
echo "INFO: Done! Don't forget to thank new contributors :)"

# if [ -z ${TRAVIS_TOKEN} ]; then
#   echo "Please set \$TRAVIS_TOKEN"
#   exit 1
# fi

# curl -sSf -X POST \
#   -H "Content-Type: application/json" \
#   -H "Accept: application/json" \
#   -H "Travis-API-Version: 3" \
#   -H "Authorization: token ${TRAVIS_TOKEN}" \
#   -d "{\"request\": {${PAYLOAD}}}" \
#   https://api.travis-ci.com/repo/garrettmac%2Ffoo/requests