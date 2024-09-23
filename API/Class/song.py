class Song:
    def __init__(self, id, name, nbOccurence = 1, imageAlbum = None) -> None:
        self.id = id
        self.name = name
        self.nbOccurence = nbOccurence
        self.imageAlbum = imageAlbum