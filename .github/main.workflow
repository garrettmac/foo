workflow "Travis CI" {
    on = "push"
    resolves = ["Travis CI"]
  }
  
  action "Trigger Travis CI" {
    uses = "./.github/actions/travis-ci/"
    secrets = [ "TRAVIS_TOKEN" ]
    env = {
      SLUG = "garrettmac/foo"
      SITE = "org"
    }
  } # Filter for a new tag
