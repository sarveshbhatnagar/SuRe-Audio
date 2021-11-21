import transcribe_agent.transcribe as tr
import csv
from collections import Counter
def get_text(video_ID):
    th = tr.Transcriber(video_ID)
    th.transcribe()
    tt = tr.TTexts(th.transcript)
    return tt.get_complete_text()

if __name__=="__main__":
    all_Transcript=[]
    print("hello")
    with open('data_analysis/course_video.csv','r') as csvfile:
        datareader=csv.reader(csvfile)
        header=next(datareader)
        print("hello")
        if header!=None:
            print("hello")
            for row in datareader:
                print("hello")
                video_ID=row[1]
                print("hello")
                all_Transcript.append(get_text(video_ID))
                with open("transcript.txt",'w+') as f:
                    f.writelines(all_Transcript.append(get_text(video_ID)))
                print("hello")
            # for i in range(0,len(all_Transcript)):
            #     words=all_Transcript[i].split()
            # for j in range(0,len(words)):
            #     if len(words[j])<=2:
            #         print(words[j],end=" ")
            # print(Counter(words))

print(all_Transcript)
# for i in all_Transcript:
#     if len(i)<=3:
#         print(i)


# def stop_words(all_transcript):
#     ''' it will first split the all_transcript list into each words 
#     and find all the words with length less than 3 and create a list
#      of such words then only filter the useless words from that list 
#      and create a new list of scu words'''
#     words=[]
#     for i in range(len(all_Transcript)):
#         if len(all_Transcript[i])<3:
#             words.append(all_Transcript[i])
#     return(words)

