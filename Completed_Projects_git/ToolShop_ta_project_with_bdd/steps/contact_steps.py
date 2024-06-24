from behave import *

from pages.contact_page import ContactPage

contact_page = ContactPage()

@When('contact: I click on Send button')
def step_impl(context):
    contact_page.click_send_button()


@When('contact: I enter "{text}" as First Name')
def step_impl(context, text):
    contact_page.type_first_name(text)

@When('contact: I enter "{text}" as Last Name')
def step_impl(context, text):
    contact_page.type_last_name(text)




@When('contact: I enter "{text}" as email address')
def step_impl(context, text):
    contact_page.type_email(text)

@When('contact: I choose a subject')
def step_impl(context):
    contact_page.choose_subject()


@When('contact: I enter a message with a minim 50 chrs to be valid')
def step_impl(context):
    text = (
        "Hello, My name is Andrei and I have not received any information about status of my command from this site,"
        "could you give me more info please? it`s already shipped?")
    contact_page.type_message(text)


@Then('contact: First name mandatory error is displayed')
def step_impl(context):
    contact_page.verify_error_first_name_is_displayed()


@Then('contact: Last name mandatory error is displayed')
def step_impl(context):
    contact_page.verify_error_last_name_is_displayed()

@Then('contact: Email mandatory error is displayed')
def step_impl(context):
    contact_page.verify_error_email_is_displayed()

@Then('contact: Message mandatory error is displayed')
def step_impl(context):
    contact_page.verify_error_message_is_displayed()


@Then('contact: I should see "{text}" msg')
def step_impl(context, text):
    contact_page.verify_success_message_displayed_msg(text)
