import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, movie_poster, movie_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer

        storyline2 = movie_storyline
        # print_storyline(storyline2) #get error: name 'print_storyline' is not define
        # print_storyline2(storyline2)

    def print_storyline(self, storyline):
        print("storyline:", storyline)

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

def print_storyline2(storyline):
    print("storyline:", storyline)