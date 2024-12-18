@important @smoke
Feature: Test aplikacji kalkulatora

  @add
  Scenario: Dodawanie dwóch liczb
    Given I have a calculator
    When I add 2 and 3
    Then the result should be 5

  @subtract
  Scenario: Odejmowanie dwóch liczb
    Given I have a calculator
    When I subtract 3 from 8
    Then the result should be 5
