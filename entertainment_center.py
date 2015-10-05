import fresh_tomatoes
import media

# List of favorite movies for the website

dumb_and_dumber = media.Movie(
    "Dumb and Dumber",
    "Two men go to Aspen",
    "https://upload.wikimedia.org/wikipedia/en/6/64/Dumbanddumber.jpg",
    "https://www.youtube.com/watch?v=J5pZCQT7JkM",
    7.3)

forrest_gump = media.Movie(
    "Forrest Gump",
    "A story of a man's life.",
    "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
    "https://www.youtube.com/watch?v=uPIEn0M8su0",
    8.8)

zoolander = media.Movie(
    "Zoolander",
    "A model with a world crisis on his hands.",   
    "https://upload.wikimedia.org/wikipedia/en/7/7c/Movie_poster_zoolander.jpg",
    "https://www.youtube.com/watch?v=YtQq0T3ExLs",
    6.6)

bridesmaids = media.Movie(
    "Bridesmaids",
    "A best friend is getting married, hilarity ensues",
    "https://upload.wikimedia.org/wikipedia/en/d/df/BridesmaidsPoster.jpg",
    "https://www.youtube.com/watch?v=FNppLrmdyug",
    6.8)

dr_strangelove = media.Movie(
    "Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb",
    "Satire about the Cold War fears of a nuclear conflict",
    "https://upload.wikimedia.org/wikipedia/en/e/e6/Dr._Strangelove_poster.jpg",
    "https://www.youtube.com/watch?v=1gXY3kuDvSU",
    8.5)

life_of_brian = media.Movie(
    "Life of Brian",
    "A man born in the stable next door to Jesus",
    "https://upload.wikimedia.org/wikipedia/en/1/18/Lifeofbrianfilmposter.jpg",
    "https://www.youtube.com/watch?v=tOOVm4kY4lE",
    8.1)

movies = [forrest_gump, zoolander, bridesmaids, dr_strangelove,
          dumb_and_dumber, life_of_brian]

# Open the website with the list of movies
fresh_tomatoes.open_movies_page(movies)  
