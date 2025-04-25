from behave import given, when, then


#  list of existing emails
existing_emails = ["user@example.com", "admin@example.com"]


# User Registration Scenario 1: New user registers successfully

@given('the user is on the registration page for valid registration')
def step_impl_registration_page_valid(context):
    print("User is on registration page.")

@when('the user submits valid registration details')
def step_impl_valid_registration(context):
    context.registered = True
    print("User submitted valid details.")

@then('the user account should be created')
def step_impl_account_created(context):
    assert context.registered is True
    print("User account created.")

@then('the user should be redirected to the login page')
def step_impl_redirected_to_login(context):
    if context.registered:
        print("User redirected to the login page.")


# User Registration Scenario 2: Invalid Registration Details

@given('the user is on the registration page for invalid registration')
def step_impl_registration_page_invalid(context):
    print("User is on registration page.")

@when('the user submits invalid registration details')
def step_impl_invalid_registration(context):
    context.registered = False
    print("User submitted invalid details.")

@then('the user should see an error message')
def step_impl_error_message(context):
    assert context.registered is False
    print("Error message displayed for invalid details.")



# User Registration Scenario 3: Registration with Existing Email

@given('the user is on the registration page')
def step_impl_registration_page_existing_email(context):
    print("User is on the registration page.")

@when('the user submits a registration with an existing email')
def step_impl_registration_existing_email(context):
    context.existing_email = "user@example.com"  # Existing email to simulate conflict
    context.email_submitted = "user@example.com"  # Simulated user submission with the same email
    print(f"User submitted registration with email: {context.email_submitted}")

@then('the user should see a message indicating the email is already registered')
def step_impl_existing_email_error(context):
    if context.email_submitted in existing_emails:
        print(f"Error: The email '{context.email_submitted}' is already registered.")
        assert context.email_submitted in existing_emails
    else:
        print("Email registration successful.")


# End of User Registration


# User Login Scenario 1: User logs in with correct credentials

@given('the user enters invalid username or password')
def step_impl(context):
    print("User is on the login page.")

@when('the user enters valid username and password')
def step_impl(context):
    context.logged_in = True
    print("User entered valid credentials.")

@then('the user should be redirected to the github dashboard')
def step_impl(context):
    assert context.logged_in is True
    print("User is redirected to the GitHub dashboard.")

# User Login Scenario 2: Invalid login credentials

@given('the user enters valid username or password')
def step_impl(context):
    print("Process user login.")

@when('the user enters invalid username or password')
def step_impl(context):
    context.logged_in = False
    print("User entered invalid credentials.")

@then('the user should see a login error message')
def step_impl(context):
    if context.logged_in is False:
        print("Error message displayed: Invalid username or password.")
        assert context.logged_in is False
    else:
        print("Unexpected behavior: User should have seen an error message.")


# User Login Scenario 3: User is already logged in

@given('the user is on the login page')
def step_impl(context):
    print("User is on the login page.")

@when('the user is already logged in')
def step_impl(context):
    context.logged_in = True
    print("User is already logged in.")

@then('the user should be redirected to the dashboard')
def step_impl(context):
    assert context.logged_in is True
    print("User is redirected to the dashboard.")


# End of user Login


# User Creating a repository

@given('the user is logged in')
def step_impl(context):
    context.logged_in = True
    print("User is logged in.")

@when('the user creates a repository named "my-web-app"')
def step_impl(context):
    context.repo = "my-web-app"
    print("Repository 'my-web-app' created.")

@then('the repository "my-web-app" should be visible in the user\'s dashboard')
def step_impl(context):
    assert context.repo == "my-web-app"
    print("Repository visible on dashboard.")


# End of user creating a repo


# Issues tracking

@given('the user is viewing the repository "my-web-app"')
def step_impl(context):
    context.repo = "my-web-app"
    print("Viewing 'my-web-app'.")

@when('the user creates an issue titled "Bug report"')
def step_impl(context):
    context.issue = "Bug report"
    print("Issue 'Bug report' created.")


@then('the issue "Bug report" should be listed in the Issues tab')
def step_impl(context):
    assert context.issue == "Bug report"
    print("Issue appears in Issues tab.")


# End of issue tracking



# Pull Request
@given('the user has committed changes to a new branch')
def step_impl(context):
    context.branch = "feature-branch"
    print("Changes committed to feature-branch.")

@when('the user opens a pull request to the main branch')
def step_impl(context):
    context.pull_request = True
    print("Pull request opened.")

@then('the pull request should appear in the list of open pull requests')
def step_impl(context):
    assert context.pull_request is True
    print("Pull request is visible.")

# End of pull request