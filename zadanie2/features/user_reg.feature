Feature: Rejestracja użytkownika
  Background:
    Given Konfiguracja środowiska pocztowego

  Scenario: Poprawna rejestracja użytkownika
    Given System pocztowy jest skonfigurowany
    When Użytkownik rejestruje się z e-mailem "test@example.com"
    Then Powinna zostać wysłana jedna wiadomość potwierdzająca

