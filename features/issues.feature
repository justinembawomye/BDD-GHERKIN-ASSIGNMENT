Feature: Issue Tracking
  Scenario: User opens a new issue on a repo
    Given the user is viewing the repository "my-web-app"
    When the user creates an issue titled "Bug report"
    Then the issue "Bug report" should be listed in the Issues tab