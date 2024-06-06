Feature: Books capability

  Background:
          Given home: I am an user on home page
          When home: I click bookstore application
          When books: I click login button
          When login: I login with valid user "scarface95" and pass "123456asdASD@"


    @books
    Scenario: I validate the stock count
          Then books: I validate that 8 books are displayed


      @books
    Scenario Outline: I validate that search is working
          When books: I search after "<query>"
          Then books: I validate that only "Git Pocket Guide" book is displayed
        Examples:
          | query  |
          | git    |
          | richard|
        #git word is related with title of the book Git Pocket Guide
        #Richard name is related with the author of the same book


    @books
    Scenario: I validate that clear search is working
          When books: I search after "test"
          When books: I clear search input
          Then books: I validate that 8 books are displayed