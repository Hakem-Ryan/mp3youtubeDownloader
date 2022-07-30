#script by Hakem Rayan
import os

print('Enter your Link:')
link = input()
print('Would you like to include the thumbnail y/n ?' )
thumbnail = input()

if thumbnail == "y":
  print("correct")
  os.system('youtube-dl --prefer-ffmpeg --extract-audio --audio-format mp3 --audio-quality 0 --embed-thumbnail ' + link)

elif thumbnail != "y" and thumbnail != "n":
  print("type 'y' for yes and 'n' or no")

else:
  print("false")
  os.system('youtube-dl --extract-audio --audio-format mp3 ' + link)
