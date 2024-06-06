Feature: Register

  Background: Open register page
    Given I am on the register page

    #Verificam ca daca dai register fara sa completezi iti raspunde cu email,pass,conf pass required etc..
  @regression
  Scenario: Check validation for mandatory fields
    When I click Register button
    Then First name mandatory error is displayed
    Then Last name mandatory error is displayed
    Then Email mandatory error is displayed
    Then Password mandatory confirm error is displayed

#TEMA Sa facem un register complet si sa verificam ca apare success la finalul inregistrarii
  #tip: Verificati ca exista mesajul
  #verificati textul de pe mesaj
  #adresa de email se va genera random
  #Sa avem grija la dropdown, am facut o functie la inceputul cursurilor:
#  def select_dropdown_text(self, locator, text):
#    dropdown = Select(self.find(locator))
#    dropdown.select_by_visible_text(text)

  #Homework fill register page and click register and check if success
  Scenario: Check the completion of fields and register
    When I enter "Andrei" as First Name
    And I enter "Robert" Last Name
    #And I enter date of birth day {}, month {}, year {}
    And I click on day of birth box
    And I enter "6" as day o birth

    And I click on month of birth box
    And I enter "September" as month o birth

    And I click on year of birth box
    And I enter "1995" as year of birth

    And I enter "bst24@gmail.com" as new Email
    And I enter "HOMEcompany" as Company Name
        #password e deja mapat in login
    And I enter "123456789" as password
    And I enter "123456789" as confirm password
        #register button e mapat deja in register
    And I click Register button
    Then Success message displayed "Your registration completed"