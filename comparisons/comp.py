def sort_by_year(movies):
    return sorted(movies, key=lambda movie: movie["year"], reverse=True)

def ignore_leading_words(title):
    ignored_words = ["A", "An", "The"]
    words = title.split(" ")
    if words[0] in ignored_words:
        return " ".join(words[1:])
    return title

def sort_by_title(movies):
    return sorted(movies, key=lambda movie: ignore_leading_words(movie["title"]))

