#Aici adaug scenariul scris -> cu plugin Gherkin
  #Here I add Gherkin Scenarios for Login Feature

  Feature: Login
    #Background -> Common begining for each of TCs for Login Feature
    Background: Open login page
      Given login: I am on the login page

    @login
    Scenario: Check that the URL of the page is correct
      Then login: The URL of the page is "https://demo.nopcommerce.com/login"


    @login
    Scenario: Check that the title page is correct
      Then login: The title of the login page is "nopCommerce demo store. Login"


    #Outline Scenario -> here we are adding 3 combinations of wrong username and password
    @login
    Scenario Outline: Log in with invalid credentials
      When login: I enter "<username>" as username
      And login: I enter "<password>" as password
      And login: I click the login button
      Then login: An error message is displayed
      Then login: I should see "No customer account found"
      Examples:
        | username         | password |
        | pyta14@gmail.com | 1234567  |
        | pyta14@yahoo.com | 12345671 |
        | pyta14@bing.com  | 123456723|



      #Outline Scenario -> at this moment is added 1 comabinations of valid username and password
      @test
      Scenario Outline: Log in with valid credentials
         When login: I enter "<username>" as username
         And login: I enter "<password>" as password
         And login: I click the login button
         Then login: I should land on home page
        Examples:
          | username | password |
          | bst24@gmail.com| 123456789|
