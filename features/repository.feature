Feature: Repository Management
  Scenario: User creates a new repository
    Given the user is logged in his/her github
    When the user creates a repository named "my-web-app"
    Then the repository "my-web-app" should be visible in the user's dashboard
  Scenario: Repository Already Exists
    Given the user is logged in github account
    When the user tries to create a repository with an existing name
    Then the user should see a message indicating the repository already exists
  Scenario: Delete Repository Successfully
    Given the user is logged in their github account
    When the user tries to delete a repository
    Then the repository should be deleted and no longer visible in the dashboard
