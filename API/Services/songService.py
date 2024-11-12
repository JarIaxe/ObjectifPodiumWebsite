from Class.song import Song
from Class.artist import Artist
from Services.sessionService import doesTodaySessionExists, GetTodaySession
from config import load_config
from connect import connect
import psycopg2

def songExist(songId):
    config = load_config(filename="database.ini", section='PostgreSQL')
    with connect(config) as conn:
        with conn.cursor() as cur:
            sqlVerif = f"""SELECT COUNT(1) FROM SONG 
                            WHERE id = '{songId}'"""

            cur.execute(sqlVerif)
            result = cur.fetchone()
            return result[0]

def songInsert(songData):
    global idSession
    config = load_config(filename="database.ini", section='PostgreSQL')
    with connect(config) as conn:
        # print(songData)
        artistsFromData = songData['artists']

        song = Song(songData["id"], songData["name"])

        artists = []
        for artistFromData in artistsFromData:
            artist = Artist(artistFromData["id"], artistFromData["name"])
            artists.append(artist)
            print(artist)
            
        with conn.cursor() as cur:
            
            if not doesTodaySessionExists():
                idSession = GetTodaySession(None)
            
            sqlSession = f"""INSERT INTO SONG_SESSION (id_session, id_song, found, isoral)
                            values('{idSession}', '{song.id}', '0', '0')"""
            cur.execute(sqlSession)

            # Verif si existe deja en bd
            sqlVerif = f"""SELECT COUNT(1) FROM SONG 
                            WHERE id = '{song.id}'"""

            cur.execute(sqlVerif)
            result = cur.fetchone()

            # Si pas présent en bd
            if (result[0] == 0):
                sqlInsert = f"""INSERT INTO SONG (id, name, numberstream, nboccurence) 
                                values('{song.id}', '{song.name}', 0, {song.nbOccurence})"""
            
                cur.execute(sqlInsert)

                for artist in artists:
                    # Verif si existe deja en bd
                    sqlVerif = f"""SELECT COUNT(1) FROM ARTIST 
                                    WHERE id = '{artist.id}'"""
                    cur.execute(sqlVerif)
                    result = cur.fetchone()
                    #Ajoute l'artiste en bd si inexistant
                    if (result[0] == 0):
                        sqlArtist = f"""INSERT INTO ARTIST (id, name) 
                                        values('{artist.id}', '{artist.name}')"""
                        cur.execute(sqlArtist)
                    #Ajoute l'occurence de la liaison chanson / artiste
                    sqlSongArtist = f"""INSERT INTO SONG_ARTIST (id_song, id_artist) 
                                    values('{song.id}', '{artist.id}')"""
                    cur.execute(sqlSongArtist)
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