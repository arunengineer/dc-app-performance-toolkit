from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.jsm.pages.agent_pages import Login, PopupManager, Logout, BrowseProjects, BrowseCustomers, \
    ViewCustomerRequest, ViewQueue, Report, InsightLogin, InsightNewSchema, InsightNewObject, InsightDeleteSchema, \
    InsightViewQueue, ViewIssueWithObject, InsightSearchByIql
from util.api.jira_clients import JiraRestClient
from util.conf import JSM_SETTINGS


def app_specific_action_admp_configuration(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_agent_app_custom_action_admp_configuration")
    def measure():
        def sub_measure():
            page.go_to_url(f"{JSM_SETTINGS.server_url}/plugins/servlet/admanagerConfigurationServlet")
            page.wait_until_visible((By.ID, "admpServerDetails"))
        sub_measure()
    measure()
    
def app_specific_action_admp_association(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_agent_app_custom_action_admp_association")
    def measure():
        def sub_measure():
            page.go_to_url(f"{JSM_SETTINGS.server_url}/plugins/servlet/admanagerAssociateUserServlet")
            page.wait_until_visible((By.ID, "admp-associateUser-mappedUserTable"))
        sub_measure()
    measure()

def app_specific_action_admp_associate_new(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_agent_app_custom_action_admp_associate_new")
    def measure():
        def sub_measure():
            page.go_to_url(f"{JSM_SETTINGS.server_url}/plugins/servlet/admanagerAssociateUserServlet")
            page.wait_until_clickable((By.ID, "admp-associate-user-button"))
            page.get_element((By.ID, "admp-associate-user-button")).click()
        sub_measure()
    measure()

def app_specific_action_admp_support(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_agent_app_custom_action_admp_support")
    def measure():
        def sub_measure():
            page.go_to_url(f"{JSM_SETTINGS.server_url}/plugins/servlet/admanagerPlusSupportServlet")
            page.wait_until_visible((By.ID, "admp_support_page"))
        sub_measure()
    measure()

def app_specific_action_admp_actions(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_agent_app_custom_action_admp_actions")
    def measure():
        def sub_measure():
            page.go_to_url(f"{JSM_SETTINGS.server_url}/plugins/servlet/admanagerPlusActionsPageServlet")
            page.wait_until_clickable((By.ID, "admp_actions_table"))
            page.get_element((By.ID, "admp_actions_table")).click()
        sub_measure()
    measure()