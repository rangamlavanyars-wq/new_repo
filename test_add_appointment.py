import logging

from pages.appointment_list_page import Appointment_list
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.title_verification import verify

def test_add_appointment(setup, session_logger):
    logger = logging.getLogger("MyFrameworkLogger")
    logger.info('logging in')  # to store log information
    driver = setup  # calling fixture

    login = LoginPage(driver)  # creating object

    verify(driver, login.login_title_text())

    '''after login only we can perform task on dashboard'''

    login.enter_email_id('prem@gmail.com')
    login.enter_password('123456')
    login.click_login_button()

    verify(driver, login.home_title_text())

    homepage = HomePage(driver)  # creating object
    '''To verify all title page by clicking on eack link in dashboard'''
    driver.implicitly_wait(10)

    homepage.click_appointment()
    homepage.click_appointment_List()
    verify(driver, homepage.appointment_title)
    
    appointment=Appointment_list(driver)
    
    appointment.click_on_add_appointment_button()
    appointment.add_date('12/24/2025')
    appointment.add_time('12:12')
    appointment.click_on_paitent_textfield()
    appointment.select_paitent_from_dropdown()
    appointment.click_on_notify()
    appointment.click_on_submit_button()
    


