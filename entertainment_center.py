import media #where Movie class is defined
import fresh_tomatoes #fresh_tomatoes.open_movies_page()

#media.Movie() takes three arguments
#movie_tiles, poster_image_url, trailer_youtube_url
totoro = media.Movie(
	"Totoro",
	"http://upload.wikimedia.org/wikipedia/en/thumb/0/02/My_Neighbor_Totoro_-_Tonari_no_Totoro_%28Movie_Poster%29.jpg/220px-My_Neighbor_Totoro_-_Tonari_no_Totoro_%28Movie_Poster%29.jpg",
	"https://youtu.be/TuLX50_5UAI"
)

howlsmovingcastle = media.Movie(
	"Howl's Moving Castle",
	"http://upload.wikimedia.org/wikipedia/en/thumb/a/a0/Howls-moving-castleposter.jpg/220px-Howls-moving-castleposter.jpg",
	"https://youtu.be/UibodUGoL4M"
)

spiritedaway = media.Movie(
	"Spirited Away",
	"http://upload.wikimedia.org/wikipedia/en/thumb/3/30/Spirited_Away_poster.JPG/220px-Spirited_Away_poster.JPG",
	"https://www.youtube.com/watch?v=6az9wGfeSgM"
)

#open_movies_page() takes a list as argument
#store movies in a list
movies = [totoro, howlsmovingcastle, spiritedaway]
fresh_tomatoes.open_movies_page(movies)