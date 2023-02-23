import web
from DB import Db

web.config.debug = True

urls = (
    '/', 'index',
    '/genre', 'genre'
)


##ajout de la class genres 
class genre:
    def GET(self) :
        db=Db().getDb()
        genres=db.select('Genre',limit=10)
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
        result += '<table border="1" style="width: 90%; margin: 0 auto;">'

        result += '<tr class="table-success"><th>Genre</th></tr>'
        for genre in genres:
            result += '<tr></tr>'
           # result +='<td>'+str(genre.GenreId)+'</td>'
            result +='<td>'+genre.Name+'</td>'
            result += '</tr>'
        result += '</table>'
        result += '</body></html>'
        return result
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()