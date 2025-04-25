Feature: Repository Management
  Scenario: User creates a new repository
    Given the user is logged in
    When the user creates a repository named "my-web-app"
    Then the repository "my-web-app" should be visible in the user's dashboard