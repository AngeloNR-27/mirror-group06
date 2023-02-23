import web
import nav
from DB import Db

web.config.debug = True

urls = (
    '/', 'index',
    '/', 'media',
    '/media', 'media'
    
)


##ajout de la class genres 
class media:
    def GET(self) :
        d = Db()
        db = d.getDb()
        a2=db.select('Album', limit=10)
        media_types=db.select('MediaType', limit=10)
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

        result += '<tr class="table-success"><th>Media type</th></tr>'
        for a in a2:
            result +='<tr>'
            for media_type in media_types:
                result +='<td>'+media_type.Name+'</td>'
                break
            result += '</tr>'
        result += '</table>'
        result += '</body></html>'
        return result
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()