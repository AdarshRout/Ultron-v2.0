import speech_recognition as sr

def speech_to_txt():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening... Please speak now.")  # Indicate that listening is in progress
            audio = r.listen(source)
            print("Processing...")  # Indicate that processing is happening
            voice_data = r.recognize_google(audio)
            print("You said: " + voice_data)  # Print the recognized text
            return voice_data
    except sr.UnknownValueError:
        print("Error: Could not understand audio")
    except sr.RequestError as e:
        print(f"Error: Could not request results from Google Speech Recognition service; {e}")
    except Exception as e:
        print(f"Error: {e}")  # General error catching

