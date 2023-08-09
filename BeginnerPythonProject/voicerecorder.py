import sounddevice 
from scipy.io.wavfile import write

frequency  = 48000
seconds = int(input("Enter the recording number of seconds :"))
print("We are recording....\n")
voice_capture = sounddevice.rec(int(seconds * frequency),samplerate=frequency,channels=2)
sounddevice.wait()
write("voice capture",frequency,voice_capture)
print("voice capture is done successfully check your folder to listen recording")
