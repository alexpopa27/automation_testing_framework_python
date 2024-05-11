Feature: Check the inventory functionality

  Background:
    Given login: I am an user on the login page

  @test6
  Scenario: Try to click on a product, than back to products
    When login: I fill the username with value "standard_user"
    When login: I fill the password with value "secret_sauce"
    When login: I press the login button
    When inventory: I click on a product
    Then inventory: The URL has changed
    When inventory: I click on "Back to products"
    Then login: The URL has changed

  @test7
  Scenario: Try to click on the settings icon
    When login: I fill the username with value "standard_user"
    When login: I fill the password with value "secret_sauce"
    When login: I press the login button
    When inventory: I click on settings icon
    Then inventory: Settings list is displayed

  @test8
  Scenario: Try to click on shopping cart icon
    When login: I fill the username with value "standard_user"
    When login: I fill the password with value "secret_sauce"
    When login: I press the login button
    When inventory: I click on the shopping cart icon
    Then cart: The URL has changed

  @test9
  Scenario: Try to add items in shopping cart
    When login: I fill the username with value "standard_user"
    When login: I fill the password with value "secret_sauce"
    When login: I press the login button
    When inventory: I add to cart the first item
    When inventory: I click on the shopping cart icon
    Then cart: The URL has changed
    Then cart: Items are in the cart