workflow "Travis CI" {
    on = "push"
    resolves = ["Travis CI"]
  }
  
  action "Travis CI" {
    uses = "garrettmac/travis-ci-action@master"
    secrets = ["TRAVIS_TOKEN"]
    env = {
      SLUG = "garrettmac/foo"
      SITE = "org"
    }
  } # Filter for a new tag