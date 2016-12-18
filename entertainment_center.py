import media
import movie_web_page

toy_story = media.Movie('Toy Story',
                        'A story about a boy and his toys',
                        'http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
                        'https://www.youtube.com/watch?v=vwyZH85NQC4')

print toy_story.storyline

avatar = media.Movie('Avatar',
                     'A marine on an alien planet',
                     'http://upload.wikipedia.org/wikimedia/id/b/b0/Avatar-Teaser-Poster.jpg',
                     'https://www.youtube.com/watch?v=5PSNL1qE6VY')
                     
school_of_rock = media.Movie('School of Rock',
                             'Storyline',
                             'http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg',
                             'https://www.youtube.com/watch?v=3PsUJFEBC74')

ratatouille = media.Movie('Ratatouille',
                          'Storyline',
                          'http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg',
                          'https://www.youtube.com/watch?v=c3sBBRxDAqk')

midnight_in_paris = media.Movie('Midnight in Paris',
                                'Storyline',
                                'http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg',
                                'https://www.youtube.com/watch?v=atLg2wQQxvU')

hunger_games = media.Movie('Hunger Games',
                           'Storyline',
                           'http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg',
                           'https://www.youtube.com/watch?v=PbA63a7H0bo')

all_movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]

movie_web_page.open_movies_page(all_movies)