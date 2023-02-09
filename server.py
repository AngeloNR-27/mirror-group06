import web
web.config.debug = True

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        db = web.database(
            dbn='mysql',
            host='tmp-insi.rktmb.org',
            port=3306,
            user='insigroup00',
            pw='insigroup00',
            db='project00',
        )
        # premier modification: ajout des albums,artist,... te changement de limite = 10
        a2=db.select('Album', limit=10) 
        artists=db.select('Artist', limit=10)
        genres=db.select('Genre',limit=10)
        tracks=db.select('Track',limit=10)
        media_types=db.select('MediaType',limit=10)
        playlists=db.select('Playlist',limit=10)

        #ajout html pour afficher la base de donne
        result = '<html><head><title>test</title></head>'
        result += '<head><link rel="stylesheet" href="style.css">'
        result += '</head>'
        result += '<table border="1">'
        
        result += '<tr><th>Genre</th><th>Artists</th><th>Album</th><th>Track</th><th>Media type</th><th>Playlist</th>'
        result += '<body>'
        for a in a2:
            result += a.Title + ',(' + str(a.ArtistId) + ') <br/>'
        result += '</body></html>'
        return result

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
