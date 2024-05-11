Feature: Check the checkout functionality

  Background:
    Given login: I am an user on the login page

  @test12
  Scenario: Check if "Cancel" button is working
    When login: I fill the username with value "standard_user"
    When login: I fill the password with value "secret_sauce"
    When login: I press the login button
    When inventory: I click on the shopping cart icon
    When cart: I click on "Checkout"
    When checkout: I click on "Cancel"
    Then cart: The URL has changed

  @test13
  Scenario: Try to click on continue without any personal information
    When login: I fill the username with value "standard_user"
    When login: I fill the password with value "secret_sauce"
    When login: I press the login button
    When inventory: I click on the shopping cart icon
    When cart: I click on "Checkout"
    When checkout: I click on "Continue"
    Then checkout: Error message is displayed: "Error: First Name is required"

  @test14
  Scenario: Try to click continue with first and last name, but without postal code
    When login: I fill the username with value "standard_user"
    When login: I fill the password with value "secret_sauce"
    When login: I press the login button
    When inventory: I click on the shopping cart icon
    When cart: I click on "Checkout"
    When checkout: I fill the first name with value: "Alex"
    When checkout: I fill the last name with value: "Alex27"
    When checkout: I click on "Continue"
    Then checkout: Error message is displayed: "Error: Postal Code is required"

  @test15
  Scenario: Try to click continue with correct values
    When login: I fill the username with value "standard_user"
    When login: I fill the password with value "secret_sauce"
    When login: I press the login button
    When inventory: I click on the shopping cart icon
    When cart: I click on "Checkout"
    When checkout: I fill the first name with value: "Alex"
    When checkout: I fill the last name with value: "Alex27"
    When checkout: I fill the postal code with value: "40000"
    When checkout: I click on "Continue"
    Then checkout: The URL has changed again