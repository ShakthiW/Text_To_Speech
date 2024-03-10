import wave

# audio signal parameters
# - number of channels
# - sample width
# - frame rate/ sample rate or sample frequency : 44,100Hz - standard sample rate for audio CDs
# - number of frames
# - values of a frame: in binary format

# open the file for reading (read binary)
obj = wave.open('output.wav', "rb")

# print
print("Number of channels: ", obj.getnchannels())
print("Sample width: ", obj.getsampwidth())
print("Frame rate: ", obj.getframerate())
print("Number of frames: ", obj.getnframes())
print("Parameters: ", obj.getparams())

time_audio = obj.getnframes() / obj.getframerate()
print("Time: ", time_audio)

# read all the frames - can also use onj.getnframes() to read all the frames
frames = obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames))
# close the file
obj.close()


# write wave file
sample_rate = 16000.0 # hertz

# open the file for writing (write binary)
obj = wave.open("new_output.wav",'wb')

# set parameters based on the audio signal we analysed earlier
obj.setnchannels(1) # mono
obj.setsampwidth(2)
obj.setframerate(sample_rate)

# write the frames - basically duplicating the audio signal
obj.writeframes(frames)
# close the file
obj.close()