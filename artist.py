import web
import nav
from DB import Db

web.config.debug = True

urls = (
    '/', 'index',
    '/artist', 'artist'
    
)



##ajout de la class artist
class artist:
    def GET(self) :
        db=Db().getDb()
        artists=db.select('Artist',limit=10)
        result='<html><head><title>test</title>'
        result += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">'
        result += '<link rel="stylesheet" href="style.css">'
        result += '</head><body>'

        #lien des menu
        result += '<table border="1">'  
        result += '<ul>'

        result += '<body>'
        result += nav.nav()
        result += '<table class="table table-secondary" border="1" style="width: 90%; margin: 0 auto;">'

        result += '<tr class="table-secondary"><th>Artist</th></tr>'
        for artist in artists:
            result += '<tr>'
           
            result +='<td>'+artist.Name+'</td>'
            result += '</tr>'
        result += '</table>'
        result += '</body></html>'
        return result
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()