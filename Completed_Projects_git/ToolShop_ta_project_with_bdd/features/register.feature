

Feature: Register

  Background: Enter to register page
    Given home: I am on the home page
    When  home: I click on Sign In button
    Then  login: The URL page is "https://practicesoftwaretesting.com/#/auth/login"
    When  login: I click on Register your account link
    Then  register: I land on the customer registration page

  @register
  Scenario Outline: Check validation for all fields and if register is successful for 3 customers

    When  register: I enter "<name>" as First Name
    And   register: I enter "<last_name>" as Last Name
    And   register: I enter "<birthday>" as birth day
    And   register: I enter "<address>" as Address
    And   register: I enter "<postcode>" as Post Code
    And   register: I enter "<city>" as City
    And   register: I enter "<state>" as State
    And   register: I enter "<phone>" as Phone
    And   register: I enter "<email>" as Email Address
    And   register: I enter "<password>" as Password
    And   register: I select RO country
    And   register: I click to register button
    Then  login: I should land on login page
    Examples:
      |name  |last_name|birthday|address      |postcode |city     |state    |phone   |email               |password|
      |Andrei |Robert   |06091995|Red Street  |12343    |Bucharest|Bucharest|07123453|andrei9510@yahoo.com |123aA#123
      |Nicu   |Ionel    |10081995|Blue Street |324523   |Bucharest|Bucharest|02134353|nicu9510@gmail.com   |321bB!123
      |Andreea|Elena    |09021994|White Street|32553    |Bucharest|Bucharest|02235321|andreea9510@gmail.com|321cC!123



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




