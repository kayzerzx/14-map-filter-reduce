movies = [
    ("the matrix", 1999),
    ("avatar", 2009),
    ("jurassic park", 1993),
    ("avengers: endgame", 2019),
    ("inception", 2010),
    ("titanic", 1997)
]

movies.sort(key=lambda movie: movie[1], reverse=True)

for title, year in movies:
    print(title, year)