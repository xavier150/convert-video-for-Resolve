import os 
import ffmpeg
from os import listdir
from os.path import isfile, join
import time 

source_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"Source")
export_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"Export")

def CheckPrerequisites ():
	print("Check prerequisites..")
	#time.sleep(1)
	VerifiDirs(source_path)
	VerifiDirs(export_path)
	print("Check prerequisites finished!")
	return True

def VerifiDirs(directory):
    # Check and create a folder if it does not exist

    if not os.path.exists(directory):
        os.makedirs(directory)
        return True
    return False
	
def ClearConsole():
	os.system('cls' if os.name=='nt' else 'clear')
	pass

class FileToConvert():
	def __init__(self, file_name):
		self.file_name = file_name 
		self.status = "Waiting"
		
	def ConvertFile(self):
		SourceFile = os.path.join(source_path, self.file_name)
		new_file_name = self.file_name
		new_file_name = new_file_name[:-4]
		new_file_name = new_file_name+".mov"
		ExportFile = os.path.join(export_path, new_file_name)
		
		stream = ffmpeg.input(SourceFile)
		vcodec = "mjpeg" #Video codec
		acodec = "pcm_s16be" #Audio codec
		stream = ffmpeg.output(stream, ExportFile, acodec=acodec, vcodec=vcodec)
		ffmpeg.run(stream)
		self.status = "Success"

	#video = moviepy.VideoFileClip(SourceFile)
	#video.write_videofile(os.path.join(ExportFile),fps=24, codec='libx264', audio_codec='m4a')
	#video.audio.write_audiofile(os.path.join(os.path.join(export_path, "sound"+".m4a")))
	
check_prerequisites = CheckPrerequisites()
ClearConsole()

print("This script convert video files for DaVinci Resolve! :D")
print("https://github.com/xavier150/convert-video-for-Resolve by Xavier Loux.")
print("")

if check_prerequisites:
	input('Place your video file(s) in "Source" folder and Enter to continue...')
	ClearConsole()
	
	files = [f for f in listdir(source_path) if isfile(join(source_path, f))] #Get all files
	print(str(len(files)) + ' file(s) found in "Source" folder!')
	for file in files:
		print("- " + file)
	input("Press Enter to continue...")
	ClearConsole()
	
	converted_files = []
	for file in files:
		convert = FileToConvert(file)
		convert.ConvertFile()
		converted_files.append(convert)
	
	ClearConsole()
	print(str(len(files)) + ' file(s) converted in "Converted" folder!')
	for x, converted_file in enumerate(converted_files):
		print(str(x+1) + '/' + str(len(converted_files)) + ' - ' + converted_file.file_name  + ' : ' + converted_file.status)
	print("Thanks for using my script! :D")
	print("https://github.com/xavier150/convert-video-for-Resolve by Xavier Loux.")
	print("")
	input("Press Enter to exit...")
	

