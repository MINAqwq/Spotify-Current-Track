import requests
import time
import os
import platform
import sys

def clear():
    if(platform.system()) == "Linux":
        os.system("clear")
    
    if (platform.system()) == "Windows":
        os.system("cls")
    
    if (platform.system()) == "Darwin":
        os.system("clear")



def get_current_track(access_token):

    try:
        try:

            url = "https://api.spotify.com/v1/me/player/currently-playing"

            response = requests.get(
                url,
                headers={
                    "Authorization": f"Bearer {access_token}"
                }
            )
            json_resp = response.json()

            track_name = json_resp['item']['name']
            artists = [artist for artist in json_resp['item']['artists']]

            artist_names = ', '.join([artist['name'] for artist in artists])

            current_track_info = str(track_name) + " - " + str(artist_names)

        except KeyError:
            print("\nInvalid Token (Press Enter)")
            input("")
            clear()
            main()

    except TypeError:
        clear()
        print("Request Error")
        time.sleep(0.5)
        print("To avoid this use Spotify web in your Browser (Press Enter)")
        input("")
        clear()
        main()

    return current_track_info


def main():

    print("access token:")
    token = str(input(""))
    clear()
    print("Starting...")

    current = get_current_track(token)

    if os.path.isdir("currentsong") == False:
        os.mkdir("currentsong")
    clear()

    print("Listening... (stop with ctrl + c)")

    i = 0
    try:
        while i < 1:
            f = open("currentsong/current.txt", "w")
            current = get_current_track(token)
            f.write(str(current))
    except KeyboardInterrupt:
        f.close()
        print("\nStoped!")



main()
