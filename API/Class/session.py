from datetime import date
from uuid import uuid4


class Session:
    def __init__(self, themeBlindTest) -> None:
        self.id = uuid4()
        self.date = date.today()
        self.nbShooters = 0
        self.themeBlindTest = themeBlindTest
        self.nbDropCoupe = 0