import media
import fresh_tomatoes

#movie created with title, about, poster image and link to trailer
toy_story = media.Movie("Toy Story",
                        "The story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#movie created with title, about, poster image and link to trailer
avatar = media.Movie("Avatar",
                     "The story of aliens that are blue",
                     "http://4outof10.com/wp-content/uploads/custom/avatar-poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

#movie created with title, about, poster image and link to trailer
school_of_rock = media.Movie("School Of Rock",
                             "A music teacher who brings rock to his classroom",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")
#movie created with title, about, poster image and link to trailer
ratatouille = media.Movie("Ratatouille",
                          "A story about an unsuspecting chef",
                          "http://i15.photobucket.com/albums/a395/al_finete/Ratatouille/Poster007.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")
#movie created with title, about, poster image and link to trailer
midnight_in_paris = media.Movie("Midnight In Paris",
                                 "This is a romantic comedy set in Paris about a family that goes there because of business",
                                 "http://images.moviepostershop.com/midnight-in-paris-movie-poster-2011-1020695872.jpg",
                                 "https://www.youtube.com/watch?v=BYRWfS2s2v4")
#movie created with title, about, poster image and link to trailer
the_hunger_games = media.Movie("The Hunger Games",
                 "The Story of a tribute, who fights for her life",
                 "http://www.hungergamesdwtc.net/wp-content/uploads/2014/02/The-Hunger-Games-Poster.jpg",
                 "https://www.youtube.com/watch?v=4S9a5V9ODuY")

#movie created with title, about, poster image and link to trailer
gardians_of_the_galaxy = media.Movie("Gardians of the Galaxy",
                                  "A group of misfits travels the Galaxy",
                                  "http://1.media.dorkly.cvcdn.com/26/95/18b149286ca6f2920e017bd5d2ffcbf5.jpg",
                                  "https://www.youtube.com/watch?v=B16Bo47KS2g")


#collect instances of media.Move() into an array
movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, the_hunger_games, gardians_of_the_galaxy]
#pass array to fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)


