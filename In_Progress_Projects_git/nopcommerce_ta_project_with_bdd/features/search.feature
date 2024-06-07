Feature: Search

  Background: Open home page
    Given Search: I am on the home page



  Scenario Outline: Search works properly for 3 elements
    When Search: I enter "<element>" in the search field
    And Search: I click the search button
    Then Search: I am redirected to the search results page
    And Search: There are some results displayed
    Examples:
      |element |
      |HTC     |
      |Notebook|
      |Nike    |

