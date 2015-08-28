import media
import fresh_tomatoes

#creates a new instance of media object
bad_boys = (media.movie("Bad Boys", "Two cops with the help of a female witness track a huge drug lord",
"https://upload.wikimedia.org/wikipedia/en/a/a8/Bad_Boys.jpg", "https://www.youtube.com/watch?v=6GaPkMqAS44"))

#creates a new instance of media object
popeye = (media.movie("Popeye", "Animated Movie of Popeye", "http://i.ytimg.com/vi/i4tNuM9XttM/maxresdefault.jpg", 
"https://www.youtube.com/watch?v=i4tNuM9XttM"))

#creates a new instance of media object
teenage_mutant_ninja_turtles = (media.movie("Teenage Mutant Ninja Turtles", "Lean mean green machines", 
"http://www.gstatic.com/tv/thumb/movieposters/12217/p12217_p_v7_ac.jpg", "https://www.youtube.com/watch?v=6WEdwZ0_ido"))

#creates a new instance of media object
mortal_kombat = (media.movie("MOrtal Kombat", "A Tournament to Save Earth", 
"http://channelawesome.com/forums/attachments/1995-mortal-kombat-the-  movie-poster-jpg.2867/", "https://www.youtube.com/watch?v=JHIfHL5UgFs"))

#creates a new instance of media object
ghostbusters_II = (media.movie("GhostBusters II", "4 Scientists battle the paranormal", 
"https://upload.wikimedia.org/wikipedia/en/0/01/Ghostbusters_ii_poster.jpg", "https://www.youtube.com/watch?v=UnzH75FlwvU"))

#creates a new instance of media object
blues_brothers = (media.movie("Blues Brothers", "Two Brothers get the Band back together", 
"http://3k27vp2gptse3d62r82kc6x1.wpengine.netdna-cdn.com/wp-content/uploads/2014/09/TheBluesBrothers.jpg","https://www.youtube.com/watch?v=asM2-YAMWxg"))

#stores movie objects into an array list and passes that array object to fresh_tomatoes object to display trailers in html
movies = [bad_boys, popeye, teenage_mutant_ninja_turtles, mortal_kombat, ghostbusters_II, blues_brothers]
fresh_tomatoes.open_movies_page(movies)


