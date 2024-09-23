from Class.song import Song
from Class.artist import Artist
from config import load_config
from connect import connect

def songInsert(songData):
    config = load_config(filename="database.ini", section='PostgreSQL')
    with connect(config) as conn:
        # print(songData)
        artistsFromData = songData['artists']

        song = Song(songData["id"], songData["name"])

        artists = []
        for artistFromData in artistsFromData:
            artist = Artist(artistFromData["id"], artistFromData["name"])
            print(artist)
            
        with conn.cursor() as cur:
            # Verif si existe deja en bd
            sqlVerif = f"""SELECT COUNT(1) FROM SONG 
                            WHERE id = '{song.id}'"""

            cur.execute(sqlVerif)
            result = cur.fetchone()
            # Si pas présent en bd
            if (result[0] == 0):
                sqlInsert = f"""INSERT INTO SONG (id, name, numberstream, nboccurence, imagealbum) 
                                values('{song.id}', '{song.name}', 0, {song.nbOccurence}, {song.imageAlbum})"""
            
                cur.execute(sqlInsert)
            else:
                # si présent en bd
                sqlGet = f"""   select nboccurence from song 
                                where id = '{song.id}'"""
                cur.execute(sqlGet)

                result = cur.fetchone()
                song.nbOccurence = result[0]+1

                sqlUpdate = f"""    update song
                                    set nboccurence = {song.nbOccurence} where id = '{song.id}'"""
                
                cur.execute(sqlUpdate)
            conn.commit()





if __name__ == "__main__":
    pass