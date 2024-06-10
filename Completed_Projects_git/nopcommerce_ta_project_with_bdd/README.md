## Title: Nopcommerce Test Automation project with bdd framework.
## Installation:
-> Install python and pycharm
-> Use the package manager pip to install selenium and behave framework
- pip install -U selenium
- pip install behave
- pip install behave-html-formatter 


## Description:
-> The purpose of this project is test in an automation manner this site https://demo.nopcommerce.com/
for different capabilities such as login with valid/invalid credentials, register, search, shopping cart feature

-> We will be working with Behave Framework and Page Object Model design pattern


## Project Structure
-> Features directory where tests are mapped in english language

-> Pages directory where are written methods for actions and verifications 

-> Steps directory where is linked the features directory and pages directory

## Utilization 
-> There are 4 features: login, register, search, shopping_cart
-> For running the TCs we have to use tags (login, register, search, cart)

## How to run and generate the report
-> behave -f html -o choose_name.html --tags=choose_tag


### Feature: Register report
![img.png](img.png)


### Feature: Login report
![img_2.png](img_2.png)
![img_3.png](img_3.png)

### Feature: Search report
![img_4.png](img_4.png)

### Feature: Shopping cart report
![img_5.png](img_5.png)