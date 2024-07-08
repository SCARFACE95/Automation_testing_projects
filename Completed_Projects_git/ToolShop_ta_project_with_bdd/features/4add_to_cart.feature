Feature: Cart
  Background: Open home page
    Given home: I am on the home page
    When home: I delete all filters
    When home: I click on first product from the search list
    Then product: The URL page contains "https://practicesoftwaretesting.com/product"
    Then product: I should see "Combination Pliers" as product name
    When product: I click to Add to cart button

 #@cart
 #Scenario: Add item to cart

  # Then product: I should see "Product added to shopping cart." as message
  # Then product: I check the cart with 1 item



 @cart
 Scenario: Finish a command
   When product: I click on cart checkout button
   Then checkout: I land on checkout page
   When checkout: I click to "Proceed to checkout"
   When login: I enter "robertbst20@yahoo.com" as Email Address
   When login: I enter "1123aA#123" as Password
   When login: I click on the login button
   When checkout: I click to "Proceed to checkout 2"
   When checkout: I click to "Proceed to checkout 3"
   When checkout: Select payment method as cash on delivery
   When checkout: I click on confirm button
   Then checkout: I should see "Payment was successful"


