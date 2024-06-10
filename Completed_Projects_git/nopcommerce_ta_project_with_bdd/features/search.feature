Feature: Search

  Background: Open home page
    Given Home: I am on the home page


  @search
  Scenario Outline: Search works properly for 3 elements
    When Home: I enter "<element>" in the search field
    And Home: I click the search button
    Then Search: I am redirected to the search results page
    And Search: There are some results displayed
    Examples:
      |element |
      |HTC     |
      |Notebook|
      |Nike    |

