import speech_recognition as sr


def speech_to_txt():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try: 
        voice_data= ""
        voice_data= r.recognize_google(audio)
        print(voice_data)
        return voice_data
    except sr.UnknownValueError:
        print("Error, No voice found")
    except sr.RequestError:
        print("RequestError")