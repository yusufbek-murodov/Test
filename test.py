import wave

from pydub import AudioSegment

audio = AudioSegment.from_file("test_audio.mp3")
audio.export("test_audio.wav", format='wav')


#wave
audio = wave.open('test_audio.wav', 'rb')
channels = audio.getnchannels()
sample_width = audio.getsampwidth()
frequency = audio.getframerate()
num_of_frames = audio.getnframes()

print("Channels:", channels)
print("Sample width:", sample_width, "Bytes")
print("Frequency:", frequency)
print("Number of frames:", num_of_frames)
print(num_of_frames / frequency)



samples = audio.readframes(num_of_frames)
print(len(samples))
