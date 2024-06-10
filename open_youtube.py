

import webbrowser
from body.speak import Speak
from body.listen import MicExecution

def Play_youtube():

    text = MicExecution().lower()
    text1 = text.replace('play',"playing")
    Speak(text1)
    api_key = "AIzaSyBbMk2mzaJyuHquRt6C6DlOiuay5OvOqEc"
    from googleapiclient.discovery import build   
    text= text.split("play")
    search_5 = str(text[0: ])
    youtube = build("youtube" , "v3" , developerKey = api_key)
    req = youtube.search().list(q = search_5 ,part="id",type="video",fields="items/id") 
    res = req.execute()
    urlad = res['items'][0]['id']['videoId']    
    webbrowser.open("https://www.youtube.com/watch?v=" + urlad)

Play_youtube()