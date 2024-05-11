Feature: Check the login functionality

  Background:
    Given login: I am an user on the login page

  @test1
  Scenario: Try to login with correct credentials
    When login: I fill the username with value "standard_user"
    When login: I fill the password with value "secret_sauce"
    When login: I press the login button
    Then login: The URL has changed

  @test2
  Scenario: Try to login with wrong username and correct password
    When login: I fill the username with value "Alex"
    When login: I fill the password with value "secret_sauce"
    When login: I press the login button
    Then login: Error message appears: "Epic sadface: Username and password do not match any user in this service"

    @test3
  Scenario: Try to login with correct username and wrong password
    When login: I fill the username with value "locked_out_user"
    When login: I fill the password with value "Alex27"
    When login: I press the login button
    Then login: Error message appears: "Epic sadface: Username and password do not match any user in this service"

  @test4
  Scenario: Try to login only with username
    When login: I fill the username with value "problem_user"
    When login: I press the login button
    Then login: Error message appears: "Epic sadface: Password is required"

  @test5
  Scenario: Try to login only with password
    When login: I fill the password with value "secret_sauce"
    When login: I press the login button
    Then login: Error message appears: "Epic sadface: Username is required"