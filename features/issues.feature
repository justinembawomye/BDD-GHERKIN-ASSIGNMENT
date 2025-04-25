Feature: Issue Tracking

  Scenario: User opens a new issue on a repo
    Given the user is viewing the repository "my-web-app"
    When the user creates an issue titled "Bug report"
    Then the issue "Bug report" should be listed in the Issues tab

  Scenario: User tries to create a duplicate issue
    Given the repository "my-web-app" already has an issue titled "Bug report"
    When the user creates another issue titled "Bug report"
    Then the user should see a message indicating the issue already exists

  Scenario: User closes an existing issue
    Given there is an open issue titled "Bug report" in the repository
    When the user closes the issue titled "Bug report"
    Then the issue "Bug report" should no longer be listed in the Issues tab
