import txt_to_speech
import speech_to_txt
import datetime
import webbrowser
import weather


def Action(data):
    user_data = data.lower()

    if "what is your name" in user_data:
        txt_to_speech.txt_to_speech("Ultron version 2 point o")
        return "Ultron version 2.o"

    elif "hello" in user_data or "hi" in user_data:
        txt_to_speech.txt_to_speech("Hello Master, what service can I do for you")
        return "Hello Master, what service can I do for you"

    elif "good morning" in user_data:
        txt_to_speech.txt_to_speech("Good Morning Master")
        return "Good Morning Master"

    elif "what's the time" in user_data:
        current_time = datetime.datetime.now()
        Time = (str)(current_time) + "Hour:" , (str)(current_time.minute) + "Minute"
        txt_to_speech.txt_to_speech(Time)
        return Time
        
    elif "shutdown" in user_data:
        txt_to_speech.txt_to_speech("Oh okay Master")
        return "Oh okay Master"

    elif "play music" in user_data:
        webbrowser.open("https://spotify.com/")
        txt_to_speech.txt_to_speech("spotify.com is now ready for use Master")
        return "spotify.com is now ready for use Master"

    elif "youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        txt_to_speech.txt_to_speech("Opening Youtube")
        return "Opening Youtube"
    elif "open google" in user_data:
        webbrowser.open("https://google.com/")
        txt_to_speech.txt_to_speech("Opening Google")
        return "Opening Google"

    elif "weather today" in user_data:
        ans = weather.weather()
        txt_to_speech.txt_to_speech("Its"+ans+" in Bhubaneswar")
        return "Its"+ans+" in Bhubaneswar"
        

    else :
        txt_to_speech.txt_to_speech("Thats out of my bounds")
        return "Thats out of my bounds"