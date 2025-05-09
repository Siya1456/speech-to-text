import speech_recognition as sr
import pyttsx3
r = sr.Recognizer()
engine = pyttsx3.init()
def speak_text(command):
    """Convert text to speech."""
    engine.say(command)
    engine.runAndWait()

def listen_and_respond():
    """Listen to microphone input and respond."""
    try:
        with sr.Microphone() as source:
            print("Adjusting for ambient noise...")
            r.adjust_for_ambient_noise(source, duration=1) 
            print("Listening... Speak now!")
            
            audio = r.listen(source, timeout=5) 
            
            try:
                text = r.recognize_google(audio).lower()
                print(f"You said: {text}")
                speak_text(f"You said: {text}")
                
    
                if "exit" in text:
                    speak_text("Goodbye!")
                    return False
                
            except sr.UnknownValueError:
                print("Sorry, I didn't catch that. Please try again.")
                speak_text("Sorry, I didn't catch that. Please try again.")
                
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
                speak_text("There was an error with the speech service.")
                
    except Exception as e:
        print(f"Error: {e}")
        speak_text("An error occurred. Please check your microphone.")
    
    return True

if __name__ == "__main__":
    print("Speech Recognition Active. Say 'exit' to quit.")
    speak_text("Speech Recognition Active. Say 'exit' to quit.")
    
    running = True
    while running:
        running = listen_and_respond()