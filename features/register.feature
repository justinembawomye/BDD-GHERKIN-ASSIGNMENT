Feature: User Registration
  Scenario: New user registers successfully
    Given the user is on the registration page
    When the user submits valid registration details
    Then the user account should be created
    And the user should be redirected to the login page