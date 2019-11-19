import speech_recognition as sr
r = sr.Recognizer()
harvard = sr.AudioFile('1_1.wav')
with harvard as source:
    audio = r.record(source)
try:
    print("Sphinx thinks you said:"+r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error;{0}".format(e))