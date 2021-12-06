
'''an attempt to complete the last task i.e. to join the audio provided
the start and end time in seconds'''
from pydub import AudioSegment

files_path=''
file_name=''

startMin=9
startSec=50

endMin=13
endSec=30

# time to miliseconds

startTime=startMin*60*1000+startSec*1000

endTime=endMin*60*1000+endSec*1000

# opening file and extracting the segment

song=AudioSegment.from_mp3(files_path+files_path+'.mp3')
extract=song[startTime:endTime]

# saving the trimmed file

extract.export(file_name+'-extract.mp3', format="mp3")
