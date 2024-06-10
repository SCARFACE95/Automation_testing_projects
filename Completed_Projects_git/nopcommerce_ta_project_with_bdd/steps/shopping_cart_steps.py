from behave import *

#Given Section

#When Section



@when("ShoppingCart: I click on the first item")
def step_impl(context):
    context.shopping_cart_page.click_first_item()


@when("ShoppingCart: I add to cart")
def step_impl(context):
    context.shopping_cart_page.click_add_to_cart_item()


#Then Section
@then('ShoppingCart: Verify if add success message is displayed "{expected}"')
def step_impl(context, expected):
    context.shopping_cart_page.verify_add_success_to_cart_message_is_displayed(expected)

@then('ShoppingCart: Verify if quantity 1 is added')
def step_impl(context):
    context.shopping_cart_page.verify_if_item_is_added_to_shopping_cart()