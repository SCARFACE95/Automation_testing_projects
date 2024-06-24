Feature: Contact
  Background: Enter to contact page
    Given home: I am on the home page
    When  home: I click on the contact button

#  @obsolete
#  Scenario: Check validation for mandatory fields
#    When contact: I click on Send button
#    Then contact: First name mandatory error is displayed
#    Then contact: Last name mandatory error is displayed
#    Then contact: Email mandatory error is displayed
#    Then contact: Message mandatory error is displayed


  @contact
  Scenario: Send successful contact message on a specific subject
    When contact: I enter "Robert" as First Name
    And  contact: I enter "Bostan" as Last Name
    And  contact: I enter "test@yahoo.com" as email address
    And  contact: I choose a subject
    And  contact: I enter a message with a minim 50 chrs to be valid
    And  contact: I click on Send button
    Then contact: I should see "Thanks for your message! We will contact you shortly." msg



