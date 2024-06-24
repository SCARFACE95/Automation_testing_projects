

Feature: Register

  Background: Enter to register page
    Given home: I am on the home page
    When  home: I click on Sign In button
    Then  login: The URL page is "https://practicesoftwaretesting.com/#/auth/login"
    When  login: I click on Register your account link
    Then  register: I land on the customer registration page

  @register
  Scenario: Check validation for all fields and if register is successful

    When  register: I enter "Andrei" as First Name
    And   register: I enter "Robert" as Last Name
    And   register: I enter "06091995" as birth day
    And   register: I enter "Red Street" as Address
    And   register: I enter "324668" as Post Code
    And   register: I enter "Bucharest" as City
    And   register: I enter "Bucharest" as State
    And   register: I enter "07641235" as Phone
    And   register: I enter a random Email Address
    And   register: I enter "123aA#123" as Password
    And   register: I select RO country
    And   register: I click to register button
    Then  login: I should land on login page



   @register
    Scenario: Check validation for mandatory fields
      When register: I click to register button
      Then register: First name mandatory error is displayed
      Then register: Last name mandatory error is displayed
      Then register: Birth mandatory error is displayed
      Then register: Address mandatory error is displayed
      Then register: Post code mandatory error is displayed
      Then register: City mandatory error is displayed
      Then register: State mandatory error is displayed
      Then register: Country mandatory error is displayed
      Then register: Phone mandatory error is displayed
      Then register: Email mandatory error is displayed
      Then register: Password mandatory error is displayed




