Feature: Pull Requests

  Scenario: User submits a pull request
    Given the user has committed changes to a new branch
    When the user opens a pull request to the main branch
    Then the pull request should appear in the list of open pull requests

  Scenario: User tries to open a pull request without committing changes
    Given the user is on a new branch with no changes committed
    When the user attempts to open a pull request
    Then the pull request should not be created and a warning should be shown

  Scenario: User merges a pull request
    Given there is an open pull request from "feature-branch" to "main"
    When the user merges the pull request
    Then the pull request should be removed from the list of open pull requests
