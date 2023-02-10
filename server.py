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

        """ antsoina any amin'ny base de données chinook,  """
        """ premier commit: ajout des albums et changement de limit=10"""
        album06=db.select('Album', limit=10) 

        # premier modification: ajout des albums,artist,... te changement de limite = 10
        a2=db.select('Album', limit=10) 

        artists=db.select('Artist', limit=10)
        genres=db.select('Genre',limit=10)
        tracks=db.select('Track',limit=10)
        media_types=db.select('MediaType',limit=10)
        playlists=db.select('Playlist',limit=10)


        """ajout du fichier style.css"""
        result = '<html><head><title>Server.py G06</title></head>'

        #ajout html pour afficher la base de donne
        result = '<html><head><title>test</title>'
        result += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">'
        result += '<link rel="stylesheet" href="style.css">'

        result += '</head>'

        result += '<table border="1">'  
        result += '<ul>'

        result += '<body>'
        result += '<ul class="navbar list-unstyled" style="background-color: lightgray; padding: 10px;">'

        result += '<li><a href="#albums">Albums</a></li>'
        result += '<li><a href="#artists">Artists</a></li>'
        result += '<li><a href="#genres">Genres</a></li>'
        result += '<li><a href="#tracks">Tracks</a></li>'
        result += '<li><a href="#media_types">Media Types</a></li>'
        result += '<li><a href="#playlists">Playlists</a></li>'
        result += '</ul>'
        result += '<table border="1">'
        
        result += '<tr><th>Genre</th><th>Artists</th><th>Album</th><th>Track</th><th>Media type</th><th>Playlist</th>'

        
        """ajout des boucles sur artist/playlists"""
        for a in album06:
            result +='<tr>'
            for genre in genres:
                result +='<td>'+genre.Name+'</td>'
                break
            for artist in artists:
                result +='<td>'+artist.Name+'</td>'
                break
            for track in tracks:
                result +='<td>'+track.Name+'</td>'
                break
            for media_type in media_types:
                result +='<td>'+ media_type.Name+'</td>'
                break
            for playlist in playlists:
                result +='<td>'+playlist.Name+'</td>'
                break
            result +='<td>'+a.Title+'</td>'
            result +='</tr>'
        result +='</table>'

        result += '<body>'
        """ Mise en commentaire de la boucle pour enlever les listes apparues au-dessous du tableau """
        """for a in a2:
         result += a.Title + ',(' + str(a.ArtistId) + ') <br/>' """

        
        """ for a in a2:
            result += a.Title + ',(' + str(a.ArtistId) + ') <br/>' """


        result += '</body></html>'
        return result
        

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
