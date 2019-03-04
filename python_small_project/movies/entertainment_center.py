from python_small_project.movies import media
from python_small_project.movies import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A Story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

print(toy_story.storyline)
# toy_story.show_trailer()

avatar = media.Movie("Avatar",
                     "A marine on a alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
print(avatar.storyline)
# avatar.show_trailer()
# print(avatar.storyline2) #get error: 'Movie' object has no attribute 'storyline2'

school_of_rock = media.Movie("School of Rock",
                             "Storyline",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille",
                             "Storyline",
                             "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                             "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
                             "Storyline",
                             "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                             "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games",
                             "Storyline",
                             "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                             "https://www.youtube.com/watch?v=mfmrPu43DF8")

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)