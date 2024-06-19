#login with valid credentials
Feature: Login

  Background: Enter to Sign In page
    Given home: I am on the home page
    When  home: I click on Sign In button


  @login
  Scenario Outline: Login with invalid credentials 2 times
    When  login: I enter "<email>" as Email Address
    When  login: I enter "<password>" as Password
    When  login: I click on the login button

    Then  login: An error message is displayed
    Then  login: I should see "Invalid email or password"

    Examples:
      | email             | password  |
      | testmail@yahoo.ro | ABCabc123@|
      | testmail@gmai.com | ASDasd321!|





  @login
  Scenario: Login with valid credentials
    When  login: I enter "robertbst20@yahoo.com" as Email Address
    When  login: I enter "1123aA#123" as Password
    When  login: I click on the login button
    Then  account: The URL page is "https://practicesoftwaretesting.com/#/account"
    Then  account: I should see My account in the page



