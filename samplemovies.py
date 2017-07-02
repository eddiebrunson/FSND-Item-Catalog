#!/usr/bin/python

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Genre, Base, Movie, User

engine = create_engine('sqlite:///samplemovies.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()

session = DBSession()


# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Movies for Crime Genre
Crime = Genre(user_id=1, name="Crime")

session.add(Crime)
session.commit()

movie1 = Movie( name="The Shawshank Redemption",
                cover_url="http://www.imdb.com/title/tt0111161/mediaviewer/rm3597327872",
                release_date="1994", 
                MPAA_film_rating="R",
                runtime="142 min",
                description="Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
                IMDb_rating="9.3/10", 
                youtube_url="https://www.youtube.com/watch?v=6hB3S9bIaco", 
                gross="$28.34M",
                genre=Genre(name="Crime"), 
                user_id=1)

session.add(movie1)
session.commit()


movie2 = Movie( name="The Godfather",
                release_date="1972", 
                MPAA_film_rating="R",
                runtime="175 min",
                description="The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
                IMDb_rating="9.2/10", 
                youtube_url="https://www.youtube.com/watch?v=sY1S34973zA", 
                gross="$134.82M",
                genre=Genre(name="Crime"),
                user_id=1)

session.add(movie2)
session.commit()

movie3 = Movie( name="The Dark Knight",
                release_date="2008", 
                MPAA_film_rating="PG-13",
                runtime="152 min",
                description="When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham, the Dark Knight must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
                IMDb_rating="9.0/10", 
                youtube_url="https://www.youtube.com/watch?v=TQfATDZY5Y4", 
                gross="$533.32M",
                genre=Genre(name="Crime"), 
                user_id=1)

session.add(movie3)
session.commit()

movie4 = Movie( name="The Goodfather: Part II",
                release_date="1974", 
                MPAA_film_rating="R",
                runtime="202 min",
                description="The early life and career of Vito Corleone in 1920s New York is portrayed while his son, Michael, expands and tightens his grip on the family crime syndicate.",
                IMDb_rating="9.0/10", 
                youtube_url="https://www.youtube.com/watch?v=OA1ij0alE0w", 
                gross="$57.30M",
                genre=Genre(name="Crime"),
                user_id=1)

session.add(movie4)
session.commit()

movie5 = Movie( name="Pulp Fiction",
                release_date="1994", 
                MPAA_film_rating="R",
                runtime="154 min",
                description="The lives of two mob hit men, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
                IMDb_rating="9.3/10", 
                youtube_url="https://www.youtube.com/watch?v=ewlwcEBTvcg", 
                gross="$107.93M",
                genre=Genre(name="Crime"), 
                user_id=1)

session.add(movie5)
session.commit()

movie6 = Movie( name="12 Angry Men",
                release_date="1957", 
                MPAA_film_rating="Approved",
                runtime="96 min",
                description="A jury holdout attempts to prevent a miscarriage of justice by forcing his colleagues to reconsider the evidence.",
                IMDb_rating="8.9/10", 
                youtube_url="https://www.youtube.com/watch?v=Dosg0p7LAB4", 
                gross="N/A",
                genre=Genre(name="Crime"), 
                user_id=1)

session.add(movie6)
session.commit()

movie7 = Movie( name="Goodfellas",
                release_date="1990", 
                MPAA_film_rating="R",
                runtime="146 min",
                description="The story of Henry Hill and his life through the teen years into the years of mafia, covering his relationship with wife Karen Hill and his Mob partners Jimmy Conway and Tommy DeVitto in the Italian-American crime syndicate.",
                IMDb_rating="8.7/10", 
                youtube_url="https://www.youtube.com/watch?v=OwZwm5MWSJw", 
                gross="$46.84M",
                genre=Genre(name="Crime"), 
                user_id=1)

session.add(movie7)
session.commit()

movie8 = Movie( name="City of God",
                release_date="2002", 
                MPAA_film_rating="R",
                runtime="130 min",
                description="Two boys growing up in a violent neighborhood of Rio de Janeiro take different paths: one becomes a photographer, the other a drug dealer.",
                IMDb_rating="8.7/10", 
                youtube_url="https://www.youtube.com/watch?v=dcUOO4Itgmw", 
                gross="$7.56M",
                genre=Genre(name="Crime"), 
                user_id=1)

session.add(movie8)
session.commit()

movie9 = Movie( name="The Silence of the Lambs",
                release_date="1991", 
                MPAA_film_rating="R",
                runtime="118 min",
                description="A young F.B.I. cadet must confide in an incarcerated and manipulative killer to receive his help on catching another serial killer who skins his victims.",
                IMDb_rating="8.6/10", 
                youtube_url="https://www.youtube.com/watch?v=W6Mm8Sbe__o", 
                gross="$130.73M",
                genre=Genre(name="Crime"), 
                user_id=1)
              
session.add(movie9)
session.commit()

movie10 = Movie( name="Leon: The Professional",
                 release_date="1994", 
                 MPAA_film_rating="R",
                 runtime="110 min",
                 description="Mathilda, a 12-year-old girl, is reluctantly taken in by Leon, a professional assassin, after her family is murdered. Leon and Mathilda form an unusual relationship, as she becomes his protgege and learns the assassin's trade.",
                 IMDb_rating="8.6/10", 
                 youtube_url="https://www.youtube.com/watch?v=W6Mm8Sbe__o", 
                 gross="$32.35M",
                 genre=Genre(name="Crime"), 
                 user_id=1)
              
session.add(movie10)
session.commit()



# Movies for Action Genre
Action = Genre(user_id=1, name="Action")

session.add(Action)
session.commit()

movie11 = Movie( name="The Dark Knight",
                release_date="2008", 
                MPAA_film_rating="PG-13",
                runtime="152 min",
                description="When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham, the Dark Knight must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
                IMDb_rating="9.0/10", 
                youtube_url="https://www.youtube.com/watch?v=TQfATDZY5Y4", 
                gross="$533.32M",
                genre=Genre(name="Action"), 
                user_id=1)

session.add(movie11)
session.commit()


movie12 = Movie( name="Baahubali 2: The Conclusion",
                release_date="2017", 
                MPAA_film_rating="N/A",
                runtime="167 min",
                description="When Shiva, the son of Bahubali, learns about his heritage, he begins to look for answers. His story is juxtaposed with past events that unfolded in the Mahishmati Kingdom.",
                IMDb_rating="9.2/10", 
                youtube_url="https://www.youtube.com/watch?v=94BzBOpv42g", 
                gross="$18.98M",
                genre=Genre(name="Action"), 
                user_id=1)

session.add(movie12)
session.commit()

movie13 = Movie( name="Inception",
                release_date="2010", 
                MPAA_film_rating="Unrated",
                runtime="161 min",
                description="A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.",
                IMDb_rating="8.8/10", 
                youtube_url="https://www.youtube.com/watch?v=8hP9D6kZseM", 
                gross="$292.57M",
                genre=Genre(name="Action"), 
                user_id=1)

session.add(movie13)
session.commit()

movie14 = Movie( name="Dangal",
                release_date="2016", 
                MPAA_film_rating="R",
                runtime="202 min",
                description="Former wrestler Mahavir Singh Phogat and his two wrestler daughters struggle towards glory at the Commonwealth Games in the face of societal oppression.",
                IMDb_rating="8.8/10", 
                youtube_url="https://www.youtube.com/watch?v=x_7YlGv9u1g", 
                gross="$11.15M",
                genre=Genre(name="Action"), 
                user_id=1)

session.add(movie14)
session.commit()

movie15 = Movie( name="Star Wars: Episode V - The Empire Strikes Back",
                release_date="1980", 
                MPAA_film_rating="PG",
                runtime="124 min",
                description="After the rebels are overpowered by the Empire on their newly established base, Luke Skywalker begins Jedi training with Master Yoda. His friends accept shelter from a questionable ally as Darth Vader hunts them in a plan to capture Luke.",
                IMDb_rating="8.8/10", 
                youtube_url="https://www.youtube.com/watch?v=8pg1obK0Qfo", 
                gross="$290.16M",
                genre=Genre(name="Action"),  
                user_id=1)

session.add(movie15)
session.commit()

movie16 = Movie( name="Star Wars: Episode IV - A New Hope",
                release_date="1977", 
                MPAA_film_rating="PG",
                runtime="121 min",
                description="Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a wookiee and two droids to save the galaxy from the Empire's world-destroying battle-station, while also attempting to rescue Princess Leia from the evil Darth Vader.",
                IMDb_rating="8.7/10", 
                youtube_url="https://www.youtube.com/watch?v=oVxcQQXXxGQ", 
                gross="$460.94M",
                genre=Genre(name="Action"),  
                user_id=1)

session.add(movie16)
session.commit()

movie17 = Movie( name="The Matrix",
                release_date="1999", 
                MPAA_film_rating="R",
                runtime="136 min",
                description="A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
                IMDb_rating="8.5/10", 
                youtube_url="https://www.youtube.com/watch?v=m8e-FF8MsqU", 
                gross="$171.38M",
                genre=Genre(name="Action"),  
                user_id=1)

session.add(movie17)
session.commit()

movie18 = Movie( name="The Dark Knight Rises",
                release_date="2012", 
                MPAA_film_rating="PG-13",
                runtime="164 min",
                description="Eight years after the Joker's reign of anarchy, the Dark Knight, with the help of the enigmatic Selina, is forced from his imposed exile to save Gotham City, now on the edge of total annihilation, from the brutal guerrilla terrorist Bane.",
                IMDb_rating="8.7/10", 
                youtube_url="https://www.youtube.com/watch?v=z5Humz3ONgk", 
                gross="$448.13M",
                genre=Genre(name="Action"),  
                user_id=1)

session.add(movie18)
session.commit()

movie19 = Movie( name="Gladiator",
                release_date="2000", 
                MPAA_film_rating="R",
                runtime="155 min",
                description="When a Roman general is betrayed and his family murdered by an emperor's corrupt son, he comes to Rome as a gladiator to seek revenge.",
                IMDb_rating="8.5/10", 
                youtube_url="https://www.youtube.com/watch?v=Q-b7B8tOAQU", 
                gross="$187.67M",
                genre=Genre(name="Action"),  
                user_id=1)
              
session.add(movie19)
session.commit()

movie20 = Movie( name="Raider of the Lost Ark",
                release_date="1981", 
                MPAA_film_rating="PG",
                runtime="115 min",
                description="Archaeologist and adventurer Indiana Jones is hired by the U.S. government to find the Ark of the Covenant before the Nazis.",
                IMDb_rating="8.5/10", 
                youtube_url="https://www.youtube.com/watch?v=2Km8dhhIlPI", 
                gross="$242.37M",
                genre=Genre(name="Action"),  
                user_id=1)
              
session.add(movie20)
session.commit()


# Movies for Animation Genre
Animation = Genre(user_id=1, name="Animation")

session.add(Animation)
session.commit()

movie21 = Movie( name="Your Name",
                release_date="2016", 
                MPAA_film_rating="PG",
                runtime="106 min",
                description="Two strangers find themselves linked in a bizarre way. When a connection forms, will distance be the only thing to keep them apart?",
                IMDb_rating="8.6/10", 
                youtube_url="https://www.youtube.com/watch?v=xU47nhruN-Q", 
                gross="$4.68M",
                genre=Genre(name="Animation"), 
                user_id=1)

session.add(movie21)
session.commit()


movie22 = Movie( name="Spirited Away",
                release_date="2001", 
                MPAA_film_rating="PG",
                runtime="125 min",
                description="During her family's move to the suburbs, a sullen 10-year-old girl wanders into a world ruled by gods, witches, and spirits, and where humans are changed into beasts.",
                IMDb_rating="8.6/10", 
                youtube_url="https://www.youtube.com/watch?v=gOSP8sm_NoQ", 
                gross="$10.05M",
                genre=Genre(name="Animation"),
                user_id=1)

session.add(movie22)
session.commit()

movie23 = Movie( name="The Lion King",
                release_date="1994", 
                MPAA_film_rating="G",
                runtime="88 min",
                description="Lion cub and future king Simba searches for his identity. His eagerness to please others and penchant for testing his boundaries sometimes gets him into trouble.",
                IMDb_rating="8.5/10", 
                youtube_url="https://www.youtube.com/watch?v=4sj1MT05lAA", 
                gross="$422.78M",
                genre=Genre(name="Animation"),
                user_id=1)

session.add(movie23)
session.commit()

movie24 = Movie( name="Grave of the Fireflies",
                release_date="1988", 
                MPAA_film_rating="Unrated",
                runtime="89 min",
                description="A young boy and his little sister struggle to survive in Japan during World War II.",
                IMDb_rating="8.5/10", 
                youtube_url="https://www.youtube.com/watch?v=4vPeTSRd580", 
                gross="N/A",
                genre=Genre(name="Animation"), 
                user_id=1)

session.add(movie24)
session.commit()

movie25 = Movie( name="Princess Mononoke",
                release_date="1997", 
                MPAA_film_rating="PG-13",
                runtime="134 min",
                description="On a journey to find the cure for a Tatarigami's curse, Ashitaka finds himself in the middle of a war between the forest gods and Tatara, a mining colony. In this quest he also meets San, the Mononoke Hime.",
                IMDb_rating="8.4/10", 
                youtube_url="https://www.youtube.com/watch?v=4OiMOHRDs14", 
                gross="$2.30M",
                genre=Genre(name="Animation"), 
                user_id=1)

session.add(movie25)
session.commit()

movie26 = Movie( name="Wall-E",
                release_date="2008", 
                MPAA_film_rating="G",
                runtime="98 min",
                description="In the distant future, a small waste-collecting robot inadvertently embarks on a space journey that will ultimately decide the fate of mankind.",
                IMDb_rating="8.4/10", 
                youtube_url="https://www.youtube.com/watch?v=8-_9n5DtKOc", 
                gross="223.81M",
                genre=Genre(name="Animation"), 
                user_id=1)

session.add(movie26)
session.commit()

movie27 = Movie( name="Toy Story",
                release_date="1995", 
                MPAA_film_rating="R",
                runtime="81 min",
                description="A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.",
                IMDb_rating="8.3/10", 
                youtube_url="https://www.youtube.com/watch?v=4KPTXpQehio", 
                gross="$191.80M",
                genre=Genre(name="Animation"), 
                user_id=1)

session.add(movie27)
session.commit()

movie28 = Movie( name="Up",
                release_date="2009", 
                MPAA_film_rating="PG",
                runtime="96 min",
                description="Seventy-eight year old Carl Fredricksen travels to Paradise Falls in his home equipped with balloons, inadvertently taking a young stowaway.",
                IMDb_rating="8.3/10", 
                youtube_url="https://www.youtube.com/watch?v=qas5lWp7_R0", 
                gross="$292.98M",
                genre=Genre(name="Animation"), 
                user_id=1)
genre=Genre(name="Animation"),
session.add(movie28)
session.commit()

movie29 = Movie( name="Toy Story 3",
                release_date="2010", 
                MPAA_film_rating="G",
                runtime="155 min",
                description="When a Roman general is betrayed and his family murdered by an emperor's corrupt son, he comes to Rome as a gladiator to seek revenge.",
                IMDb_rating="8.3/10", 
                youtube_url="https://www.youtube.com/watch?v=ZZv1vki4ou4", 
                gross="$414.98M",
              genre=Genre(name="Animation"),
                user_id=1)
              
session.add(movie29)
session.commit()

movie30 = Movie( name="Inside Out",
                 release_date="2015", 
                 MPAA_film_rating="PG",
                 runtime="95 min",
                 description="After young Riley is uprooted from her Midwest life and moved to San Francisco, her emotions - Joy, Fear, Anger, Disgust and Sadness - conflict on how best to navigate a new city, house, and school.",
                 IMDb_rating="8.2/10", 
                 youtube_url="https://www.youtube.com/watch?v=WIDYqBMFzfg", 
                 gross="$356.45M",
                 genre=Genre(name="Animation"),
                 user_id=1)
              
session.add(movie30)
session.commit()


print "added movies!"