# 8-6. City Names
def city_country(city, country):
    city_n_country = f"{city}, {country}"
    return city_n_country.title()

cityCountry1 = city_country('paris', 'france')
cityCountry2 = city_country('saigon', 'vietnam')
cityCountry3 = city_country('toronto', 'canada')

print(cityCountry1)
print(cityCountry2)
print(cityCountry3)

# Using user input
"""_city = input("What city? ")
_country = input("What country? ")
cityCountry = city_country(_city, _country)
print(cityCountry)"""


# 8-7. Album
def make_album(artist_name, album_title, num_of_songs = None):
    musician = {'name': artist_name, 'album': album_title}

    if num_of_songs is not None:
        album = f"\nThe album '{album_title.title()}' by {artist_name.title()} has {num_of_songs} songs."
    else:
        album = f"\nThe album '{album_title.title()}' by {artist_name.title()}."
    return album

album = make_album('the beatles', 'let it be')
# album = make_album('the beatles', 'let it be', 5) # with num of songs
print(album)

"""album1 = make_album(artist_name = 'the beatles', album_title = 'let it be')
album2 = make_album(artist_name = 'michael jackson', album_title = 'smooth criminal')
album3 = make_album(artist_name = 'backstreet boys', album_title = 'i want it that way')

print(album1)
print(album2)
print(album3)
"""


# 8-8. User Albums
def make_album(artist_name, album_title, num_of_songs = None):
    musician = {'name': artist_name, 'album': album_title}

    if num_of_songs is not None:
        album = f"The album '{album_title.title()}' by {artist_name.title()} has {num_of_songs} songs."
    else:
        album = f"The album '{album_title.title()}' by {artist_name.title()}."
    return album

while True:
    artist = input("\nEnter an album's artist: ")
    title = input("Enter the album's title: ")

    if artist == 'q':
        break
    elif title == 'q':
        break

    album = make_album(artist, title)
    print(album)
