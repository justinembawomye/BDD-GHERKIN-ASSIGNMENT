Feature: Pull Requests
  Scenario: User submits a pull request
    Given the user has committed changes to a new branch
    When the user opens a pull request to the main branch
    Then the pull request should appear in the list of open pull requests

    