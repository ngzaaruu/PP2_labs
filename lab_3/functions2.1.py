def is_imdb_above_5_5(movie):
    return movie["imdb"] > 5.5
movie = {
    "name": "AlphaJet",
    "imdb": 3.2,
    "category": "War"
}

print(is_imdb_above_5_5(movie))  