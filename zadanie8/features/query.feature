Feature: Zarządzanie Flapami
  Scenario: Utworzenie nowego Flapa
    Given użytkownik chce utworzyć nowy Flap o nazwie "Testowy Flap"
    When wysyła polecenie utworzenia Flapa
    Then Flap powinien zostać utworzony pomyślnie
