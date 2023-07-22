from comp import sort_by_year, sort_by_title, ignore_leading_words

def test_sort_by_year():
    movies = [
        {"title": "The Dark Knight", "year": 2008},
        {"title": "Inception", "year": 2010},
        {"title": "The Avengers", "year": 2012}
    ]
    sorted_movies = sort_by_year(movies)
    assert sorted_movies == [
        {"title": "The Avengers", "year": 2012},
        {"title": "Inception", "year": 2010},
        {"title": "The Dark Knight", "year": 2008}
    ]

def test_sort_by_title():
    movies = [
        {"title": "The Dark Knight", "year": 2008},
        {"title": "Inception", "year": 2010},
        {"title": "The Avengers", "year": 2012}
    ]
    sorted_movies = sort_by_title(movies)
    assert sorted_movies == [
        {"title": "Inception", "year": 2010},
        {"title": "The Dark Knight", "year": 2008},
        {"title": "The Avengers", "year": 2012}
    ]


def test_ignore_leading_words():
    assert ignore_leading_words("The Dark Knight") == "Dark Knight"
    assert ignore_leading_words("An Inception") == "Inception"
    assert ignore_leading_words("The Avengers") == "Avengers"

