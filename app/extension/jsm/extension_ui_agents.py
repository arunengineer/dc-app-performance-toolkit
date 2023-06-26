from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.jsm.pages.agent_pages import Login, PopupManager, Logout, BrowseProjects, BrowseCustomers, \
    ViewCustomerRequest, ViewQueue, Report, InsightLogin, InsightNewSchema, InsightNewObject, InsightDeleteSchema, \
    InsightViewQueue, ViewIssueWithObject, InsightSearchByIql
from util.api.jira_clients import JiraRestClient
from util.conf import JSM_SETTINGS


# def app_specific_action(webdriver, datasets):
#     page = BasePage(webdriver)
#     if datasets['custom_issues']:
#         issue_key = datasets['custom_issue_key']

#     # To run action as specific user uncomment code bellow.
#     # NOTE: If app_specific_action is running as specific user, make sure that app_specific_action is running
#     # just before test_2_selenium_z_log_out action

#     # @print_timing("selenium_app_specific_user_login")
#     # def measure():
#     #     def app_specific_user_login(username='admin', password='admin'):
#     #         login_page = Login(webdriver)
#     #         login_page.delete_all_cookies()
#     #         login_page.go_to()
#     #         login_page.set_credentials(username=username, password=password)
#     #         if login_page.is_first_login():
#     #             login_page.first_login_setup()
#     #         if login_page.is_first_login_second_page():
#     #             login_page.first_login_second_page_setup()
#     #         login_page.wait_for_page_loaded()
#     #     app_specific_user_login(username='admin', password='admin')
#     # measure()

#     @print_timing("selenium_agent_app_custom_action")
#     def measure():

#         @print_timing("selenium_agent_app_custom_action:view_request")
#         def sub_measure():
#             page.go_to_url(f"{JSM_SETTINGS.server_url}/browse/{issue_key}")
#             # Wait for summary field visible
#             page.wait_until_visible((By.ID, "summary-val"))
#             # Wait for you app-specific UI element by ID selector
#             page.wait_until_visible((By.ID, "ID_OF_YOUR_APP_SPECIFIC_UI_ELEMENT"))
#         sub_measure()
#     measure()

def app_specific_action(webdriver, datasets):
    page = BasePage(webdriver)
    if datasets['custom_issues']:
        issue_key = datasets['custom_issue_key']

    @print_timing("selenium_agent_app_custom_action")
    def measure():

        @print_timing("selenium_agent_app_custom_action:view_request")
        def sub_measure():
            page.go_to_url(f"{JSM_SETTINGS.server_url}/browse/{issue_key}")
            # Wait for summary field visible
            page.wait_until_visible((By.ID, "summary-val"))
            # Wait for you app-specific UI element by ID selector
            page.element_exists((By.ID, "admanagerPlusActions-label"))
        sub_measure()
    measure()

def app_specific_action_admp_create_user(webdriver, datasets):
    page = BasePage(webdriver)
    if datasets['custom_issues']:
        issue_key = datasets['custom_issue_key']

    @print_timing("selenium_agent_app_custom_action_admp_create_user")
    def measure():
        def sub_measure():
            page.go_to_url(f"{JSM_SETTINGS.server_url}/browse/{issue_key}")
            # Wait for summary field visible
            page.wait_until_visible((By.ID, "summary-val"))
            # Wait for you app-specific UI element by ID selector
            page.element_exists((By.LINK_TEXT, 'Create User'))
            # page.get_element((By.LINK_TEXT, 'Create User')).click()
        sub_measure()
    measure()

def app_specific_action_admp_configuration(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_agent_app_custom_action_admp_configuration")
    def measure():
        def sub_measure():
            page.go_to_url(f"{JSM_SETTINGS.server_url}/plugins/servlet/admanagerConfigurationServlet")
            page.wait_until_visible((By.ID, "admpServerDetails"))  # Wait for Associate Users table visible
        sub_measure()
    measure()

    
def app_specific_action_admp_association(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_agent_app_custom_action_admp_association")
    def measure():
        def sub_measure():
            page.go_to_url(f"{JSM_SETTINGS.server_url}/plugins/servlet/admanagerAssociateUserServlet")
            page.wait_until_visible((By.ID, "admp-associateUser-mappedUserTable"))  # Wait for Associate Users table visible
        sub_measure()
    measure()

def app_specific_action_admp_associate_new(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_agent_app_custom_action_admp_associate_new")
    def measure():
        def sub_measure():
            page.go_to_url(f"{JSM_SETTINGS.server_url}/plugins/servlet/admanagerAssociateUserServlet")
            page.wait_until_clickable((By.ID, "admp-associate-user-button"))  # Wait for Associate Users table visible
            page.get_element((By.ID, "admp-associate-user-button")).click()
        sub_measure()
    measure()

def app_specific_action_admp_support(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_agent_app_custom_action_admp_support")
    def measure():
        def sub_measure():
            page.go_to_url(f"{JSM_SETTINGS.server_url}/plugins/servlet/admanagerPlusSupportServlet")
            page.wait_until_visible((By.ID, "admp_support_page"))  # Wait for Associate Users table visible
        sub_measure()
    measure()
