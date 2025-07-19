from project import get_movie_info, get_movie_poster, enter_into_csv
import pytest


def main():
    test_get_movie_info()
    test_get_movie_poster()
    test_enter_into_csv()


def test_get_movie_info():
    assert get_movie_info("F1 the movie") == {'Title': 'F1: The Movie', 'Year': '2025', 'Rated': 'PG-13', 'Released': '27 Jun 2025', 'Runtime': '155 min', 'Genre': 'Action, Drama, Sport', 'Director': 'Joseph Kosinski', 'Writer': 'Ehren Kruger, Joseph Kosinski', 'Actors': 'Brad Pitt, Damson Idris, Javier Bardem', 'Plot': 'A Formula One driver comes out of retirement to mentor and team up with a younger driver.', 'Language': 'English', 'Country': 'United States', 'Awards': '7 nominations total', 'Poster': 'https://m.media-amazon.com/images/M/MV5BZTYwYjJhNzYtY2ZiZS00ZmYxLWJkZjctYjRlNGIxYjI3ZTU0XkEyXkFqcGc@._V1_SX300.jpg', 'Ratings': [{'Source': 'Internet Movie Database', 'Value': '7.9/10'}, {'Source': 'Rotten Tomatoes', 'Value': '83%'}, {'Source': 'Metacritic', 'Value': '68/100'}], 'Metascore': '68', 'imdbRating': '7.9', 'imdbVotes': '109,496', 'imdbID': 'tt16311594', 'Type': 'movie', 'DVD': 'N/A', 'BoxOffice': '$142,281,913', 'Production': 'N/A', 'Website': 'N/A', 'Response': 'True'}
    assert get_movie_info("Fnius and Ferb") == ("Not a movie")
    assert get_movie_info("") == ("Not a movie")

    ...


def test_get_movie_poster():
    assert get_movie_poster("Inception") == ("Saved poster in Poster_out.jpg")
    with pytest.raises(SystemExit):
        get_movie_poster("stab")


def test_enter_into_csv():
    assert (
        enter_into_csv(
            {
                "Title": "F1: The Movie",
                "Year": "2025",
                "Rated": "PG-13",
                "Released": "27 Jun 2025",
                "Runtime": "155 min",
                "Genre": "Action, Drama, Sport",
                "Director": "Joseph Kosinski",
                "Writer": "Joseph Kosinski, Ehren Kruger",
                "Actors": "Brad Pitt, Javier Bardem, Kerry Condon",
                "Plot": "A Formula One driver comes out of retirement to mentor and team up with a younger driver.",
                "Language": "English",
                "Country": "United States",
                "Awards": "N/A",
                "Poster": "https://m.media-amazon.com/images/M/MV5BOWRiOThkM2YtYzI4NS00OWViLTk0ODMtMjNlNDYyZWQ3MzNjXkEyXkFqcGc@._V1_SX300.jpg",
                "Ratings": [{"Source": "Rotten Tomatoes", "Value": "83%"}],
                "Metascore": "N/A",
                "imdbRating": "N/A",
                "imdbVotes": "N/A",
                "imdbID": "tt16311594",
                "Type": "movie",
                "DVD": "N/A",
                "BoxOffice": "N/A",
                "Production": "N/A",
                "Website": "N/A",
                "Response": "True",
            }
        )
        == "Done"
    )
    with pytest.raises(SystemExit):
        enter_into_csv("n/a")

    ...


if __name__ == "__main__":
    main()
