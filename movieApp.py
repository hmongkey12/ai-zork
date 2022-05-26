#!/usr/env/bin

import pandas as pd

def main():
    #import movie spreasheet
    movie_File = 'movies.xls'
    #create a dataframe and read moviefile and all sheets in
    # make Title column the index w/ index_col 0
    #multiple sheets added at once create a dict
    #reduce the number of columns to only those used by the app
    movies = pd.read_excel(movie_File, sheet_name=['1900s', '2000s', '2010s'], index_col= 0, usecols=['Title', 'Year', 'Genres', 'Language', 'Content Rating', 'Duration', 'Budget', 'Actor 1', 'Actor 2', 'Actor 3', 'IMDB Score'])
    #test print of movies dict
    print(movies)
main()
