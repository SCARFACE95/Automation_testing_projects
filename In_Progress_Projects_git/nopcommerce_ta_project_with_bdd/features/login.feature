#Aici adaug scenariul scris -> cu plugin Gherkin

  Feature: Login
    #Inceputul comun de la un test se poate scrie intr-un background ca sa nu ne repetam
    #practic se ruleaza background la fiecare inceput de test
    Background: Open login page
      Given I am on the login page

    @smoke @regression
    Scenario: Check that the URL of the page is correct
      #Given I am on the login page -> este declarat ca background
      Then The URL of the page is "https://demo.nopcommerce.com/login"

    #TEMA: Implementati un test similar cu cel de sus pentru verificarea titlului paginii



    #parametrizam testul sa fie rulat de 3 ori cu 3 combinatii de username si pass gresite
    #Putem sa rulam un test case de mai multe ori cu Scenario outline, Examples (cu tabel)
    @regression
    Scenario Outline: Log in with invalid credentials
      #Given I am on the login page -> este declarat ca baackground
      When I enter "<username>" as username
      And I enter "<password>" as password
      And I click the login button
      Then An error message is displayed
      Then I should see "No customer account found"
      Examples:
        | username         | password |
        | pyta14@gmail.com | 1234567  |
        | pyta14@yahoo.com | 12345671 |
        | pyta14@bing.com  | 123456723|


