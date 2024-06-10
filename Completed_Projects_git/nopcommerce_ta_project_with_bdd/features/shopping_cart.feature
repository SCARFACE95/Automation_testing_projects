
@cart
Feature: Shopping Cart

     Scenario: Add 1 item to cart
       Given Home: I am on the home page
       When Home: I enter "phone" in the search field
       And  Home: I click the search button
       Then Search: I am redirected to the search results page
       And  Search: There are some results displayed
       When ShoppingCart: I click on the first item
       When ShoppingCart: I add to cart
       Then ShoppingCart: Verify if add success message is displayed "The product has been added to your shopping cart"
       Then ShoppingCart: Verify if quantity 1 is added



