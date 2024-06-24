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
    Scenario: Check mandatory fields for login
      When  login: I click on the login button
      Then login: Email mandatory error is displayed
      Then login: Password mandatory error is displayed
