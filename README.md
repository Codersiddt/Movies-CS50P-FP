# MOVIES
URL: https://youtu.be/3V_wfzj6Mi4

## Overall Description
Have you struggled to look for a new movie to watch? Looking through thousands of websites , digging through descriptions , searching for ratings?!
Well here's a solution!
My project is an interactive python code which requests users for a movie input , so that it can outptut the movie's plot,actors,title,Imdb Rating and genre, as well as the movies poster which automatically gets saved into a jpeg file. All in a matter of seconds! No more endless searching , just enter a movie name and get everything you need right at your fingertips.

## Libraries, Modules
- **Requests** : Used to make HTTP requests , for API calls etc.
- **PIL** : Python Image Library , used to manipulate , edit images of different file formats.
- **io** : Python module to handle various input , output operations
- **sys** : Python module which provides access to system-specific functions and variables used by the python interpreter
- **csv** : Built in Python module used to read from and write to CSV
- **Tabulate** : Python library used to display data in tabular format

## Home-made Functions

### Get_Movie_Info()
This function uses one argument (title), which is the movie title inputted by the user. The function aims to retrieve the movies data from the <https://www.omdbapi.com/> website using an api and converting it into json.

`` url = f"http://www.omdbapi.com/?t={title}&apikey=6dd245b"
movie = requests.get(url)
data = movie.json()``

In this function the data is only returned if it falls in the category of movie:

``if data["Type"] == "movie":
    return data``

### Get_Movie_Poster()
This function uses one argument (title), which is the movie title inputted by the user.
Using the data from Get_Movie_Info(), Get_Movie_Poster() uses ``BytesIO()`` from io module to open the movie poster directly from it's raw form. The function further saves the poster image into **Poster_out.jpg*.

``img = Image.open(BytesIO(image_response.content))
img.convert("RGB").save("Poster_out.jpeg")``

### Enter_Into_Csv()
This function uses one argument (data), which is the data of the movie returned from Get_Movie_Info(). The function writes the movies plot into a csv called **csv_plot.csv* and other data (Title, Genre, Actors, Imdb Rating) into a csv file called **movie_content.csv*. This is done so that the data can be read from the csv and tabulated in the future as output. The plot and other contents are done separately because they are outputted seperately for a more appealing look.

``fieldnames = ["Plot"]
with open("csv_plot.csv", "a", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames, extrasaction="ignore")
    writer.writeheader()
    writer.writerow(data)``

`fieldnames = ["Title", "Genre", "Actors", "imdbRating"]
with open("movie_content.csv", "a", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames,extrasaction="ignore")
    writer.writeheader()
    writer.writerow(data)``

At the start of the function both **csv_plot.csv* and **movie_content.csv* are truncated so that the csv file is blank everytime the program is run for a fresh output.

``with open("movie_content.csv", "w") as file:
    file.truncate()``
``with open("csv_plot.csv", "w") as file:
    file.truncate()``



### Make_Table()
The function reads the data from **csv_plot.csv* and **movie_content.csv* respectively and tabulates them into a table format for a snazzy output. The plot is too long to fit in the table thus it is being output in simple format so it looks nice, whereas the other components are short enough to tabulated.

``plot = tabulate(table[1:], table[0], tablefmt="simple")``
``other = tabulate(table[1:], table[0], tablefmt="fancy_grid")``





