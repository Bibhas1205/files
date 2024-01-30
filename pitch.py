from pydub import AudioSegment
from pydub.playback import play
import sys


if(len(sys.argv)!=3):
    print("Use python3 ",sys.argv[0]," <input mp3 file> <pitch rate 0.0-3.0>")
    exit()


# Convert MP3 to WAV
mp3_file = sys.argv[1]

# Load the sound as an AudioSegment
sound = AudioSegment.from_file(mp3_file)

# Change the pitch (decrease by 20%) to simulate old man's voice
pitch_shift = float(sys.argv[2])  # Decrease pitch by 20% (change this value as desired)
new_sound = sound._spawn(sound.raw_data, overrides={
    "frame_rate": int(sound.frame_rate * pitch_shift)
})

# Play the new sound with the changed pitch
play(new_sound)
