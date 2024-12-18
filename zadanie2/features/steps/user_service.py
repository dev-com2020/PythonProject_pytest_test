class UserService:

    def __init__(self, mail_service):
        self.mail_service = mail_service
        self.registered_users = set()

    def register_user(self, email):
        if email in self.registered_users:
            raise ValueError("Użytkownik już istnieje")
        self.registered_users.add(email)
        self.mail_service.send_email(email, "Witamy w naszej aplikacji!")

