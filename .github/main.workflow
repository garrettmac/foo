workflow "Travis CI" {
    on = "push"
    resolves = ["Trigger Travis CI"]
  }
  action "Trigger Travis CI" {
    needs = "ACTION"
    uses = "./.github/actions/travis-ci"
    secrets = [ "TRAVIS_TOKEN" ]
    env = {
      SLUG = "garrettmac/foo"
      SITE = "org"
    }
  } # Filter for
