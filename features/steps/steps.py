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

@given('the user is on the login page on github')
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

@given('the user is on the login page')
def step_impl(context):
    print("User is on the login page.")

@when('the user enters invalid username or password')
def step_impl(context):
    context.logged_in = False
    print("User entered invalid credentials.")

@then('the user should see a login error message')
def step_impl(context):
    assert context.logged_in is False
    print("Error message displayed: Invalid username or password.")

# User Login Scenario 3: User Already Logged In

@given('the user is already logged in')
def step_impl(context):
    context.logged_in = True
    print("User is already logged in.")

@when('the user tries to access the login page')
def step_impl(context):
    print("User is redirected to the dashboard because they are already logged in.")

@then('the user should be redirected to the dashboard')
def step_impl(context):
    assert context.logged_in is True
    print("User is redirected to the dashboard.")


# End of user Login


# User Creating a valid repository

@given('the user is logged in his/her github')
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


# # User Logged In Scenario
# @given('the user is logged in check')
# def step_impl(context):
#     context.logged_in = True
#     print("User is logged in.")

# Repository Already Exists Scenario
@given('the user is logged in github account')
def step_impl_logged_in(context):
    context.logged_in = True
    print("User is logged in.")

@when('the user tries to create a repository with an existing name')
def step_impl_create_existing_repo(context):
    context.repo_name = "existing-repo"
    context.existing_repos = ["existing-repo", "my-web-app"]
    if context.repo_name in context.existing_repos:
        context.repo_creation_success = False
    else:
        context.repo_creation_success = True
    print(f"User tried to create repository: {context.repo_name}")

@then('the user should see a message indicating the repository already exists')
def step_impl_existing_repo_error(context):
    if not context.repo_creation_success:
        print(f"Error: The repository '{context.repo_name}' already exists.")
        assert context.repo_name in context.existing_repos
    else:
        print("Repository created successfully.")

# Scenario 3 - Deleting Repository
@given('the user is logged in their github account')
def step_impl(context):
    context.logged_in = True
    context.existing_repos = ["repo-1", "repo-2", "my-web-app"]
    print("User is logged in.")

# Delete Repository Successfully Scenario
@when('the user tries to delete a repository')
def step_impl_delete_repo(context):
    context.repo_to_delete = "repo-1"  # Simulate a repository the user wants to delete
    if context.repo_to_delete in context.existing_repos:
        context.existing_repos.remove(context.repo_to_delete)  # Simulate successful deletion
        context.repo_deletion_success = True
    else:
        context.repo_deletion_success = False
    print(f"User tried to delete repository: {context.repo_to_delete}")

@then('the repository should be deleted and no longer visible in the dashboard')
def step_impl_deleted_repo(context):
    if context.repo_deletion_success:
        print(f"Repository '{context.repo_to_delete}' successfully deleted.")
        assert context.repo_to_delete not in context.existing_repos  # Confirm it's deleted
    else:
        print(f"Error: Repository '{context.repo_to_delete}' could not be deleted.")
        assert context.repo_to_delete not in context.existing_repos  # Confirm non-existence



# End of user creating a repo


# Issues tracking
# Scenario: User opens a new issue on a repo
@given('the user is viewing the repository "my-web-app"')
def step_impl(context):
    context.repo = "my-web-app"
    print("Viewing 'my-web-app'.")

@when('the user creates an issue titled "Bug report"')
def step_impl(context):
    context.issue = "Bug report"
    context.issues = getattr(context, 'issues', [])
    context.issues.append(context.issue)
    print("Issue 'Bug report' created.")

@then('the issue "Bug report" should be listed in the Issues tab')
def step_impl(context):
    assert "Bug report" in context.issues
    print("Issue appears in Issues tab.")


# Scenario: User tries to create a duplicate issue
@given('the repository "my-web-app" already has an issue titled "Bug report"')
def step_impl(context):
    context.repo = "my-web-app"
    context.issues = ["Bug report"]
    print("Repo already has an issue titled 'Bug report'.")

@when('the user creates another issue titled "Bug report"')
def step_impl(context):
    context.new_issue = "Bug report"
    context.duplicate_issue = context.new_issue in context.issues
    print("User tried to create a duplicate issue.")

@then('the user should see a message indicating the issue already exists')
def step_impl(context):
    assert context.duplicate_issue is True
    print("Error: Issue with this title already exists.")


# Scenario: User closes an existing issue
@given('there is an open issue titled "Bug report" in the repository')
def step_impl(context):
    context.repo = "my-web-app"
    context.issues = ["Bug report"]
    print("Open issue 'Bug report' exists.")

@when('the user closes the issue titled "Bug report"')
def step_impl(context):
    if "Bug report" in context.issues:
        context.issues.remove("Bug report")
        context.issue_closed = True
    else:
        context.issue_closed = False
    print("User closed issue 'Bug report'.")

@then('the issue "Bug report" should no longer be listed in the Issues tab')
def step_impl(context):
    assert "Bug report" not in context.issues
    print("Issue 'Bug report' is no longer listed.")



# End of issue tracking



# Pull Request
# Scenario: User submits a pull request
@given('the user has committed changes to a new branch')
def step_impl(context):
    context.branch = "feature-branch"
    context.commits = 3
    print("Changes committed to feature-branch.")

@when('the user opens a pull request to the main branch')
def step_impl(context):
    if context.commits > 0:
        context.pull_request = True
        context.open_pull_requests = ["feature-branch"]
    else:
        context.pull_request = False
    print("Pull request opened.")

@then('the pull request should appear in the list of open pull requests')
def step_impl(context):
    assert "feature-branch" in context.open_pull_requests
    print("Pull request is visible.")


# Scenario: User tries to open a pull request without committing changes
@given('the user is on a new branch with no changes committed')
def step_impl(context):
    context.branch = "empty-branch"
    context.commits = 0
    print("User is on an empty branch with no commits.")

@when('the user attempts to open a pull request')
def step_impl(context):
    if context.commits == 0:
        context.pull_request = False
        context.warning = "No changes to pull request."
    else:
        context.pull_request = True
        context.warning = None
    print("User attempted to open pull request.")

@then('the pull request should not be created and a warning should be shown')
def step_impl(context):
    assert context.pull_request is False
    assert context.warning == "No changes to pull request."
    print(f"Warning: {context.warning}")


# Scenario: User merges a pull request
@given('there is an open pull request from "feature-branch" to "main"')
def step_impl(context):
    context.open_pull_requests = ["feature-branch"]
    print("Pull request from 'feature-branch' is open.")

@when('the user merges the pull request')
def step_impl(context):
    if "feature-branch" in context.open_pull_requests:
        context.open_pull_requests.remove("feature-branch")
        context.merged = True
    else:
        context.merged = False
    print("Pull request merged.")

@then('the pull request should be removed from the list of open pull requests')
def step_impl(context):
    assert "feature-branch" not in context.open_pull_requests
    assert context.merged is True
    print("Pull request has been removed from open list.")


# End of pull request