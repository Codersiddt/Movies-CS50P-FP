import requests
from PIL import Image
from io import BytesIO
import sys
import csv
from tabulate import tabulate


def main():
    movie = input("Enter the movie of your choice")
    stuff = get_movie_info(movie)
    if stuff != None:
        try:
            enter_into_csv(stuff)
            print(" ")
            print(f"{make_table()}")
            print(get_movie_poster(movie))
        except:
            sys.exit("Doesnt exist or maybe a spelling error?")
    else:
        print("Not a movie")



def make_table():
    with open("csv_plot.csv", "r") as doc2:
        # Tabulating the data

        lines = csv.reader(doc2)
        table = []
        for line in lines:
            table.append(line)

        plot = tabulate(table[1:], table[0], tablefmt="simple")
    with open("movie_content.csv", "r") as doc:

        lines = csv.reader(doc)
        table = []
        for line in lines:
            table.append(line)

        other = tabulate(table[1:], table[0], tablefmt="fancy_grid")
    return f"{plot}\n{other}\n"


def enter_into_csv(data):
    # Learned from chatgpt To clear csv file when new new movie is input

    try:
        with open("movie_content.csv", "w") as file:
            file.truncate()
        with open("csv_plot.csv", "w") as file:
            file.truncate()

        # content from json input into csv

        fieldnames = ["Plot"]
        with open("csv_plot.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames, extrasaction="ignore")
            writer.writeheader()
            writer.writerow(data)

        fieldnames = ["Title", "Genre", "Actors", "imdbRating"]
        with open("movie_content.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames, extrasaction="ignore")
            writer.writeheader()
            writer.writerow(data)

    except:
        sys.exit("Error")
    else:
        return "Done"


def get_movie_info(title):
    # Getting movie content from ombdapi
    try:
        url = f"http://www.omdbapi.com/?t={title}&apikey=6dd245b"
        movie = requests.get(url)
        data = movie.json()
        if data["Response"] == "True":
            if data["Type"] == "movie":
                return data
        else:
            return f"Not a movie"
    except:
        sys.exit("Incorrect Input")


def get_movie_poster(title):

    try:
        url = f"http://www.omdbapi.com/?t={title}&apikey=6dd245b"
        response = requests.get(url)
        data = response.json()
        if data["Type"] == "movie":
            if data["Response"] == "True" and data["Poster"] != "N/A":
                # Getting poster from api and entering it into a csv
                poster_url = data["Poster"]
                image_response = requests.get(poster_url)
                # Bytes IO learned and obtained from chatgpt
                img = Image.open(BytesIO(image_response.content))
                img.convert("RGB").save("Poster_out.jpeg")
                return f"Saved poster in Poster_out.jpg"
            else:
                return f"Poster not found for '{title}'"
        else:
            return f"Not a Movie"

    except:
        sys.exit("Cant find poster")


if __name__ == "__main__":
    main()
