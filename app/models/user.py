from .base import BaseModel


class User(BaseModel):
    username = None
    email = None
    password = None

    def __init__(self, **kwargs):
        self.kind = "User"
        super().__init__(self.kind, **kwargs)
        self.username = self.data.get("username")
        self.email = self.data.get("email")
        self.password = self.data.get("password")

    def get_id(self):
        try:
            return self.id
        except AttributeError:
            return self.data.get("id")

    def set_active(self, active):
        self.data["is_active"] = active
        if self.confirmed_at:
            self.data["confirmed_at"] = self.confirmed_at
        self.update(self.data.get("id"), self.data)

    def has_confirmed_email(self):
        return self.data.get("confirmed_at")

    def is_active(self):
        return self.data.get("is_active")

    @property
    def is_authenticated(self):
        return True
