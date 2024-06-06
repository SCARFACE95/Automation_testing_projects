
Feature: Login capability
  #is run before each start and after the scenario steps will run
  Background:
          Given home: I am an user on home page
          When home: I click bookstore application
          When books: I click login button


       @login
  Scenario Outline: I login with invalid credentials
          When login: I login with valid user "<user>" and pass "<password>"
          Then login: I validate that error message is displayed
         Examples:
           |user         | password|
           |scarface95   |1234567  |
           |itfactory    |12345678 |


      @login
  Scenario: I login with valid credentials
          When login: I login with valid user "scarface95" and pass "123456asdASD@"
          Then books: I should land on books page


