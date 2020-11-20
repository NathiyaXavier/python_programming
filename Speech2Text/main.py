# install Speech Recognition module(pip install SpeechRecognition
# pip install pipwin
# pipwin install PyAudio

import speech_recognition as sr


def main():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("Please say something")

        audio = r.listen(source)

        print("Audio recording in progress")

        try:
            content = r.recognize_google(audio)
            print("you have said: \n" + content)
        except AttributeError:
            print("Error")

        with open("recorded_audio.wav","wb") as f:
            f.write(audio.get_wav_data())

        # exporting the result
        with open('test.txt', mode='w') as file:
            file.write("Recognized text:")
            file.write("\n")
            file.write(content)
            print("ready!")


if __name__ == "__main__":
    main()


