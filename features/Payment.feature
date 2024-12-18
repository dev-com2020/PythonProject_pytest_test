Feature: Payment Types
#  wprowadzamy poszczególne kroki i scenariusz
  Scenario: Verify user has two payment options
    Given User is on Payment screen
    When User clicks on Payment types
    Then User should get Types cash method