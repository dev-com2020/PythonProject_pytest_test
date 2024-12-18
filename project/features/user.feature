Feature: Pobieranie danych użytkownika

  Scenario: Użytkownik istnieje
    Given istnieje użytkownik o ID 1
    When pobiorę dane użytkownika
    Then dane użytkownika powinny zawierać nazwę "John Doe"

#  Scenario: Użytkownik Jan istnieje
#    Given istnieje użytkownik o ID 1
#    When pobiorę dane użytkownika
#    Then dane użytkownika powinny zawierać nazwę "Jan Doe"

  Scenario: Użytkownik nie istnieje
    Given nie istnieje użytkownik o ID 999
    When pobiorę dane użytkownika
    Then dane użytkownika powinny być puste