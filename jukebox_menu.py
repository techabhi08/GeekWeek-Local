from nested_data import albums

SONG_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

while True:
    print("please choose your album (invalid choice exist):")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}".format(index + 1, title))

    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][SONG_LIST_INDEX]
    else:
        break

    print("please choose your song:")
    for index, (title_number, song) in enumerate(songs_list):
        print("{}: {}".format(index+1, song))

    songs_choice = int(input())
    if 1<= songs_choice <= len(songs_list):
        title = songs_list[songs_choice-1][SONG_TITLE_INDEX]
        print("playing {}".format(title))

    else:
        print("please choose your album")
