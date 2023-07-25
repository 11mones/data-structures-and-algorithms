
def sort_by_year(movies):
    return sorted(movies, key=lambda movie: movie["year"], reverse=True)


def sort_by_title(movies):
    def ignore_leading_words(title):
        ignored_words = ["A", "An", "The"]
        words = title.split(" ")
        if words[0] in ignored_words:
            return " ".join(words[1:])
        return title

    return sorted(movies, key=lambda movie: ignore_leading_words(movie["title"]))


def compare_years(movie1, movie2):
    return movie2["year"] - movie1["year"]


def compare_titles(movie1, movie2):
    def ignore_leading_words(title):
        ignored_words = ["A", "An", "The"]
        words = title.split(" ")
        if words[0] in ignored_words:
            return " ".join(words[1:])
        return title

    title1 = ignore_leading_words(movie1["title"])
    title2 = ignore_leading_words(movie2["title"])
    return title1.casefold() < title2.casefold()


def run_comparator_tests():
    movie1 = {"title": "The Dark Knight", "year": 2008}
    movie2 = {"title": "An Inception", "year": 2010}
    movie3 = {"title": "The Avengers", "year": 2012}

    print(compare_years(movie1, movie2))  
    print(compare_years(movie2, movie3))  

    print(compare_titles(movie1, movie2))  
    print(compare_titles(movie2, movie3))  

# Test the sorting functions
def run_sorting_tests():
    movies = [
        {"title": "An Inception", "year": 2010},
        {"title": "The Dark Knight", "year": 2008},
        {"title": "The Avengers", "year": 2012},
    ]

    print(sort_by_year(movies))  

    print(sort_by_title(movies))  


run_comparator_tests()
run_sorting_tests()
