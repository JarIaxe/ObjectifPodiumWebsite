from flask import Flask, request, Response
from flask_cors import CORS
from Services import spotifyService, songService, sessionService

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Hello World"

#region Chansons
@app.route('/api/searchSong', methods=['POST'])
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
#endregion

#region Session
@app.route('/api/getTodaySession', methods=['GET'])
def getTodaySession():
    global idSession
    idSession = sessionService.GetTodaySession()
    return {'session': idSession}, 201
#endregion

if __name__ == "__main__":
    app.run(debug=True)