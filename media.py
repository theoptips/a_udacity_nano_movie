#define the Movie class to store movie title, poster image url and trailer url
class Movie():
	def __init__(self, title, poster_image_url, trailer_youtube_url):
		#Movie constructor for initating instances of Movie
		#argument type should be string e.g. "http://url.com"
		self.title = title
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url

