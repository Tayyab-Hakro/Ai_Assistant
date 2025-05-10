import pyttsx3
import speech_recognition as sr
import pywhatkit
import wikipedia
import datetime
import webbrowser


r = sr.Recognizer()

def speak(command):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    engine.say(command)
    engine.runAndWait()

def command():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Listening... ask now...")
            audioin = r.listen(source)
            my_text = r.recognize_google(audioin)
            my_text = my_text.lower()
            print(f"Recognized text: {my_text}")

            # Play song
            if 'play' in my_text:
                song = my_text.replace('play', '')
                speak('Playing ' + song)
                pywhatkit.playonyt(song)

            # Show date
            elif 'date' in my_text:
                today = datetime.date.today().strftime("%B %d, %Y")
                speak("Today's date is " + today)

            # Wikipedia search
            elif 'who is' in my_text:
                person = my_text.replace('who is', '')
                info = wikipedia.summary(person, 1)
                speak(info)

            # Custom response for "do you know tayyab"
            elif 'do you know tayyab' in my_text:
                info = 'Tayyab is a loser and he wants to become a billionaire.'
                speak(info)
            elif 'search image of' in my_text:
                query = my_text.replace('search image of', '')
                speak('Searching images of ' + query)
                webbrowser.open(f"https://www.google.com/search?tbm=isch&q={query}")


    except Exception as e:
        print(f"Error in capturing microphone: {e}")


        # Loop through 
while True:
 command()
