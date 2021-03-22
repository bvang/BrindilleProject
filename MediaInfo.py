from pprint import pprint
from pymediainfo import MediaInfo
import os, shutil

media_info = MediaInfo.parse("C:/Users/sasuk/Downloads/J13_21082020.mp4")
for track in media_info.tracks:
    if track.track_type == "Video":
        print("Bit rate: {t.bit_rate}, Frame rate: {t.frame_rate}, "
              "Format: {t.format}".format(t=track)
        )
        print("Duration (raw value):", track.duration)
        print("Duration (other values:")
        pprint(track.other_duration)
    elif track.track_type == "Audio":
        print("Track data:")
        pprint(track.to_data())

os.chdir("C:/Users/sasuk/Downloads/")