print("start")

import os 
from os import listdir
from os.path import isfile, join
import time 

def VerifiDirs(directory):
    # Check and create a folder if it does not exist

    if not os.path.exists(directory):
        os.makedirs(directory)
        return True
    return False

source_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"Source")
export_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"Export")
VerifiDirs(source_path)
VerifiDirs(export_path)

files = [f for f in listdir(source_path) if isfile(join(source_path, f))] #Get all files

def convert(fileName):

	SourceFile = os.path.join(source_path, fileName)
	newFileName = fileName
	#newFileName = newFileName[32:] #Lenge of vlc-record-2019-12-31-03h03m48s-
	newFileName = newFileName[:-4]
	#newFileName = newFileName+str(time.time())
	newFileName = newFileName+".mov"
	ExportFile = os.path.join(export_path, newFileName)
	
	com = "cmd /k 'ffmpeg -i  \""+SourceFile+"\" -vcodec mjpeg -q:v 2 -acodec pcm_s16be -q:a 0 -f mov \""+ExportFile+"\"'"
	com = "cmd /c ffmpeg -i  \""+SourceFile+"\" -vcodec mjpeg -q:v 2 -acodec pcm_s16be -q:a 0 -f mov \""+ExportFile+"\""
	#com = 'cmd /c "ffmpeg"'
	print(com)
	os.system(com)

	#video = moviepy.VideoFileClip(SourceFile)
	#video.write_videofile(os.path.join(ExportFile),fps=24, codec='libx264', audio_codec='m4a')
	#video.audio.write_audiofile(os.path.join(os.path.join(export_path, "sound"+".m4a")))
	

for file in files:
	print(file)
	convert(file)
