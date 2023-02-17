import web
from DB import Db

web.config.debug = True

urls = (
    '/', 'index',
    '/artist', 'artist'
    
)



##ajout de la class genres 
class artist:
    def GET(self) :
        db=Db().getDb()
        artists=db.select('Artists',limit=10)
        result='<html><head><title>test</title>'
        result += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">'
        result += '<link rel="stylesheet" href="style.css">'
        result += '</head><body>'

        #lien des menu
        result += '<table border="1">'  
        result += '<ul>'

        result += '<body>'
        result += '<ul class="navbar list-unstyled" style="background-color: lightgray; padding: 10px;">'

        result += '<li><a href="/">Home</a></li>'
        result += '<li><a href="/genre">Genres</a></li>'
        result += '<li><a href="/artist">Artists</a></li>'
        result += '<li><a href="/albums">Albums</a></li>'
        result += '<li><a href="/tracks">Tracks</a></li>'
        result += '<li><a href="/media_types">Media Types</a></li>'
        result += '<li><a href="/playlists">Playlists</a></li>'
        result += '</ul>'
        result += '<table border="1">'

        result += '<tr class="table-success"><th>Artist</th></tr>'
        for artist in artists:
            result += '<tr></tr>'
           
            result +='<td>'+artist.Name+'</td>'
            result += '</tr>'
        result += '</table>'
        result += '</body></html>'
        return result
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()