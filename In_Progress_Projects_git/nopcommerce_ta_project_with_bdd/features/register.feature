Feature: Register

  Background: Open register page
    Given Register: I am on the register page

  @regression
  Scenario: Check validation for mandatory fields
    When Register: I click Register button
    Then Register: First name mandatory error is displayed
    Then Register: Last name mandatory error is displayed
    Then Register: Email mandatory error is displayed
    Then Register: Password mandatory confirm error is displayed


  @register
  Scenario: Check validation for all fields and if register success
    When Register: I enter "Andrei" as First Name
    And Register: I enter "Robert" Last Name
    #And I enter date of birth day {}, month {}, year {}
    And Register: I click on day of birth box
    And Register: I enter "6" as day o birth

    And Register: I click on month of birth box
    And Register: I enter "September" as month o birth

    And Register: I click on year of birth box
    And Register: I enter "1995" as year of birth

    And Register: I enter "bst24@gmail.com" as new Email
    And Register: I enter "HOMEcompany" as Company Name
        #password e deja mapat in login
    And Login: I enter "123456789" as password
    And Register: I enter "123456789" as confirm password
        #register button e mapat deja in register
    And Register: I click Register button
    Then Register: Success message displayed "Your registration completed"