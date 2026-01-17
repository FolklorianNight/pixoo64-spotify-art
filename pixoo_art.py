import time
import base64
import requests
from io import BytesIO
from PIL import Image
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# CONFIGURATION 
PIXOO_IP = "192.168.1.xxx"  # <--- Pixoo local ip
SPOTIFY_CLIENT_ID = "ID"  # <--- Get from dev dashboard
SPOTIFY_CLIENT_SECRET = "ID"  # <--- Get from dev dashboard
REDIRECT_URI = "http://127.0.0.1:8888/callback" 

def reset_pixoo_cache():
    try:
        payload = {"Command": "Draw/ResetHttpGifId", "PicID": 1}
        requests.post(f"http://{PIXOO_IP}/post", json=payload)
    except Exception as e:
        print(f"Reset warning: {e}")

def send_to_pixoo(image_url):
    try:
        response = requests.get(image_url)
        response.raise_for_status()
        
        img = Image.open(BytesIO(response.content))
        img = img.convert("RGB")
        img = img.resize((64, 64), Image.Resampling.LANCZOS)
        
        pixels = [x for p in list(img.getdata()) for x in p]
        
        img_base64 = base64.b64encode(bytearray(pixels)).decode('utf-8')

        payload = {
            "Command": "Draw/SendHttpGif",
            "PicNum": 1,
            "PicWidth": 64,
            "PicOffset": 0,
            "PicID": 1,   
            "PicSpeed": 1000,
            "PicData": img_base64
        }

        r = requests.post(f"http://{PIXOO_IP}/post", json=payload)
        r.raise_for_status()
        print(f"Updated: {image_url}")

    except Exception as e:
        print(f"Error sending to Pixoo: {e}")

def main():
    print("Starting Spotify -> Pixoo Bridge...")
    
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope="user-read-currently-playing"
    ))

    last_track_id = None

    while True:
        try:
            current_track = sp.current_user_playing_track()
            
            if current_track is not None and current_track['is_playing']:
                track_id = current_track['item']['id']
                
                if track_id != last_track_id:
                    print(f"Now Playing: {current_track['item']['name']}")
                    
                    images = current_track['item']['album']['images']
                    if images:
                        reset_pixoo_cache() 
                        
                        image_url = images[0]['url']
                        send_to_pixoo(image_url) 
                        
                        last_track_id = track_id
            else:
                print("No song playing...", end='\r')

            time.sleep(1) # Checks spotify every x seconds

        except Exception as e:
            print(f"Error in loop: {e}")
            time.sleep(2)

if __name__ == "__main__":
    main()
