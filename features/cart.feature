Feature: Check the shopping cart functionality

  Background:
    Given login: I am an user on the login page

  @test10
  Scenario: Check if "Continue Shopping" button is working
    When login: I fill the username with value "standard_user"
    When login: I fill the password with value "secret_sauce"
    When login: I press the login button
    When inventory: I click on the shopping cart icon
    When cart: I click on "Continue Shopping"
    Then login: The URL has changed

  @test11
  Scenario: Check if "Checkout" button is working
    When login: I fill the username with value "standard_user"
    When login: I fill the password with value "secret_sauce"
    When login: I press the login button
    When inventory: I click on the shopping cart icon
    When cart: I click on "Checkout"
    Then checkout: The URL has changed