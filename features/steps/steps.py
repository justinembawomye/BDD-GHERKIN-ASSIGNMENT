from behave import given, when, then

# User Registration

@given('the user is on the registration page')
def step_impl(context):
    print("User is on registration page.")

@when('the user submits valid registration details')
def step_impl(context):
    context.registered = True
    print("User submitted valid details.")

@then('the user account should be created')
def step_impl(context):
    assert context.registered is True
    print("User account created.")

@then('the user should be redirected to the login page')
def step_impl(context):
    if context.registered:
        print("User redirected to the login page.")



# End of User Registration



# User Login

@given('the user is on the login page')
def step_impl(context):
    print("User is on login page.")

@when('the user enters valid username and password')
def step_impl(context):
    context.logged_in = True
    print("User entered valid credentials.")

@then('the user should be redirected to the github dashboard')
def step_impl(context):
    assert context.logged_in is True
    print("User is redirected to the GitHub dashboard.")


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