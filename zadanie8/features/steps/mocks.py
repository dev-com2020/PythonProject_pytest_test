from zadanie8.features.steps.commands import UtworzFlapCommand


class MockCommandHandler:
    def __init__(self):
        self.last_command = None

    def handle(self, command):
        if isinstance(command, UtworzFlapCommand):
            self.last_command = command.nazwa_flapa
            return "Flap został utworzony"
