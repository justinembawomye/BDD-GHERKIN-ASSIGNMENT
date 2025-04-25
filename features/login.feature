Feature: User login
  Scenario: User logs in with correct credentials
    Given the user is on the login page
    When the user enters valid username and password
    Then the user should be redirected to the github dashboard