Feature: Search
  Background: Open home page
    Given home: I am on the home page

  @search
  Scenario Outline: Search box works properly for 5 elements
    When home: I enter "<element>" in the search field
    And  home: I click the search button
    Then home: There are some results displayed
    Examples:
      | element    |
      | hammer     |
      | measure   |
      | pliers     |
      | Wrench     |
      | Screwdriver|


  @search
    Scenario: Search by sorting the name
      When home: I sort from A-Z
      Then home: There are some results displayed

    @search
    Scenario: Search by price using slider
      When home: I change the value from 100 to a lower value
      Then home: I should see "85" < 100
      Then home: There are some results displayed


    @search
     Scenario Outline: Search by setting the category for 3 times
       When home: I delete all filters
       When home: I click on " <name> " box
       Then home: There are some results displayed
       Then home: I check first element displayed if in the name contains "<name>"


       Examples:
         | name    |
         | Hammer  |
         | Chisels |
         | Wrench |




