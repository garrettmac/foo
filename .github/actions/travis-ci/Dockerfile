# # FROM alpine

# # LABEL version="0.1.0"
# # LABEL repository="https://github.com/garrettmac/foo"

# # RUN apk add curl


# # COPY "entrypoint.sh" "/entrypoint.sh"
# # ENTRYPOINT ["/entrypoint.sh"]

# # CMD [""]

# FROM node:10

# LABEL "name" = "travis-ci"
# LABEL "version" = "0.0.1"
# LABEL "repository"="https://github.com/garrettmac/foo"
# LABEL "com.github.actions.name" = "Travis CI"
# LABEL "com.github.actions.description" = "Trigger a new GitHub release and generate the changelog using lerna-changelog."
# LABEL "com.github.actions.icon" = "tag"
# LABEL "com.github.actions.color" = "yellow"

# ADD entrypoint.sh /action/entrypoint.sh
# # ADD package.json /action/package.json
# # ADD package-lock.json /action/package-lock.json
# # ADD release.js /action/release.js

# RUN chmod +x /action/entrypoint.sh

# ENTRYPOINT ["/action/entrypoint.sh"]
FROM debian:9.5-slim

LABEL "com.github.actions.name"="Hello World"
LABEL "com.github.actions.description"="Write arguments to the standard output"
LABEL "com.github.actions.icon"="mic"
LABEL "com.github.actions.color"="purple"

LABEL "repository"="http://github.com/octocat/hello-world"
LABEL "homepage"="http://github.com/actions"
LABEL "maintainer"="Octocat <octocat@github.com>"

ADD entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]