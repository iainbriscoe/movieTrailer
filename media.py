import webbrowser

class Movie():
    """This Class provides a way to store movie related information"""
    #constants of ratings 
    VALID_RATINGS = ["G","PG","PG-13","R"]
    #initialize each movie with a title, story line, image, trailer url 
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline 
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    #opens a browser window with the instance of 
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
