# pixoo64-spotify-art
Simple python based script to display the currently playing song on spotify

!!IMPORTANT!!

Spotify's currently disabled the creation of new integrations which is required for this to work. Without an existing app this will not work. Check https://developer.spotify.com/dashboard to see if you have an existing app. Will update this if spotify removes the block


Some notes:

-AI was used to clean up the code and for the entire image formatting portion

-Image persists even if the song's paused or spotify's closed entierly, this was intentional, but calling the reset cache function after no song's detected should make the screen blank

-No plans to add more features or a ui

-Pixoo needs to be connected to wifi but shouldn't need internet access

-The script checks spotify every second for new songs and updates the display about 1 and a half seconds after a song starts

-Tested on macos 26 with apple silicon but should be fully compatible with windows and linux

-Relatively lightweight, stays at 0% CPU use when not converting images and around 1% when converting with similarly low network use

Instructions:

Go to https://developer.spotify.com/dashboard, create an app (if possible) or edit a current one to have http://127.0.0.1:8888/callback as a redirect URI, note down the client ID and client secret

<img width="525" height="893" alt="image" src="https://github.com/user-attachments/assets/ef62859b-22af-4b78-b6a8-d81f3e91feac" />

Install dependencies
```
pip install requests spotipy Pillow
```

Get device's ip, easiest way is through the divoom app (My devices -> device name -> settings)

Download the script and fill out the configuration portion

<img width="463" height="102" alt="image" src="https://github.com/user-attachments/assets/45edea9a-6b88-4fb6-aff7-5999bbc7e891" />

Run the script, it should start a browser login page for spotify to authenticate the app with your account

The display should just update with the currently playing spotify song now

Errors:

Only ones i've experienced personally are spotify authentication related

For INVALID_CLIENT: Invalid client: The client ID or secret in the script were likely put in incorrectly

For INVALID_CLIENT: Invalid redirect URI: Double check the redirect url on the dev dashboard, it needs to be http://127.0.0.1:8888/callback

Also check the url, make sure it looks like this with your client ID in it
<img width="1119" height="42" alt="image" src="https://github.com/user-attachments/assets/c2ff1cd5-1e6f-4fc1-b9ac-e6de1d6fb933" />
