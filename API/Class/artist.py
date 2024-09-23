class Artist:
    def __init__(self, id, name):
        self.id=id
        self.name=name

    def __str__(self) -> str:
        return f"id : {self.id}, name : {self.name}"