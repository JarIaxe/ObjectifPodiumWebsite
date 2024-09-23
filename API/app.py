from flask import Flask, request, Response
from Services import spotifyService, songService

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route('/api/searchSong')
def searchSongEndPoint():
    data = request.json
    res = spotifyService.get_song_from_title(data["title"])
    return res
    
@app.route('/api/saveSong', methods=['POST'])
def saveSongEndPoint():
    data = request.json
    songData = spotifyService.get_song_by_id(data["id"])
    songService.songInsert(songData)
    return {'a':'b'}, 201    

if __name__ == "__main__":
    app.run(debug=True)