Feature: User login
  Scenario: User logs in with correct credentials
    Given the user enters valid username or password
    When the user enters valid username and password
    Then the user should be redirected to the github dashboard
  Scenario: Invalid Login Credentials
    Given the user enters invalid username or password
    When the user enters invalid username or password
    Then the user should see a login error message
  Scenario: User Already Logged In
    Given the user is on the login page
    When the user is already logged in
    Then the user should be redirected to the dashboard