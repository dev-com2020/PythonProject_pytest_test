Feature: User Information
  Scenario Outline: Check login
    Given user enters "<name>" and "<password>"
    Then user should be logged in
    Examples: Credentials
    | name  | password  |
    | user1 | pwd1      |
    | user2 | pwd2      |
    | user3 | pwd3      |