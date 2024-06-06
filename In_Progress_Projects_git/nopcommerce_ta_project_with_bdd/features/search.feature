Feature: Search

  Background: Open home page
    Given I am on the home page

#  Scenario: Search works properly
#    When I enter "HTC" in the search field
#    And I click the search button
#    Then I am redirected to the search results page
#    And There are some results displayed


  #Transformati scenariul in Scenario Outline
  #In field-ul de cautare minim 3 nume de produse care returneaza un rezultat
  Scenario Outline: Search works properly for 3 elements
    When I enter "<element>" in the search field
    And I click the search button
    Then I am redirected to the search results page
    And There are some results displayed
    Examples:
      |element |
      |HTC     |
      |Notebook|
      |Nike    |

