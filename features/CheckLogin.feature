Feature: Check login table
  Scenario: Check login func
    Given Collection of credentials
    | username  | password  |
    | user1 | pwd1      |
    | user2 | pwd2      |
    Then user should be ok