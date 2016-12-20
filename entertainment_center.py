import media
import movie_web_page
import json

##Adding data from movie_data.json
display_list =[]
CONST_MOVIE_TITLE = 'original_title'
CONST_MOVIE_STORYLINE = 'overview'
CONST_MOVIE_POSTER = 'poster_path'
CONST_MOVIE_POSTER_URL = 'https://image.tmdb.org/t/p/w500'
CONST_MOVIE_TRAILER = 'no trailer available'
CONST_MOVIE_TRAILER_URL = 'https://www.youtube.com/watch?v='
with open('movie_data.json') as data_file:
    movie_data = json.load(data_file)

movie_list = movie_data['results']

#print movie_list

for movie in movie_list:
    display_list.append(media.Movie(movie[CONST_MOVIE_TITLE],
                                    movie[CONST_MOVIE_STORYLINE],
                                    CONST_MOVIE_POSTER_URL + movie[CONST_MOVIE_POSTER],
                                    CONST_MOVIE_TRAILER_URL + CONST_MOVIE_TRAILER))


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

display_list = display_list + [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]

movie_web_page.open_movies_page(display_list)