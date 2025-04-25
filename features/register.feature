Feature: User Registration
  Scenario: New user registers successfully
    Given the user is on the registration page for valid registration
    When the user submits valid registration details
    Then the user account should be created
    And the user should be redirected to the login page
  
  Scenario: Invalid Registration Details
    Given the user is on the registration page for invalid registration
    When the user submits invalid registration details
    Then the user should see an error message

  Scenario: Registration with Existing Email
    Given the user is on the registration page
    When the user submits a registration with an existing email
    Then the user should see a message indicating the email is already registered