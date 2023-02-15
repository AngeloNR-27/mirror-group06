class Genres:
    def GET(self):
        genres = ['Rock', 'Pop', 'Jazz', 'Hip-hop', 'Electronic', 'Classical']
        return '\n'.join(genres)
