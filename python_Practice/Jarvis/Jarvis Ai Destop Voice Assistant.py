import speech_recognition as sr
import os
import pyttsx3
import webbrowser as wb
import datetime as DT
import subprocess


def say(text):
    # Use the 'say' command on macOS to make the computer speak the provided text
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    # os.system(f"say {text}")
def takecommond():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        audio = r.listen(source)
        try :
            query = r.recognize_google(audio,language='en-US')
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "your audio is not understand"
        

if __name__ == "__main__":
    print("Python vscode")
    say("Jarvis A.I.")
    while True:
        print("listening...")
        query = takecommond()
        sites = [["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedis.com"],["google","https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                wb.open(site[1])
        if "open music" in query:
            musicPath = "C:/Users/abdul/Downloads/silicon-valley-123990.mp3"
            os.startfile(musicPath)
        
        if "the time" in query:
            strftime = DT.datetime.now().strftime("%H:%M:%S")
            say(f"Sir the time{strftime}" )
        
        if "open camera".lower() in query:
            subprocess.run(["start", "microsoft.windows.camera:"], shell=True)
        
        if "open folder".lower() in query.lower():
            folder = r"C:\Users\abdul\OneDrive\Desktop\hozafa"
            os.system(f"start {folder}")
        
        
        if "open Control Panel".lower() in query:
            try:
                subprocess.Popen(["control.exe"])
            except FileNotFoundError:
                print("Control Panel not found. Please check your system.")
            except Exception as e:
                print(f"An error occurred: {e}")
                
        
        # say(query)
