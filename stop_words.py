import transcribe_agent.transcribe as tr
import csv
from collections import Counter
import pickle
# import nltk
'''only use for generating transcript only once'''
# def get_text(video_ID):
#     th = tr.Transcriber(video_ID)
#     th.transcribe()
#     tt = tr.TTexts(th.transcript)
#     return tt.get_complete_text()

stopwords={"i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"}
if __name__=="__main__":
    all_Transcript=[]
    # print("hello")
    with open('data_analysis/course_video.csv','r') as csvfile:
        datareader=csv.reader(csvfile)
        header=next(datareader)
        # print("hello")
        if header!=None:
            # print("hello")
            for row in datareader:
                # print("hello")
                video_ID=row[1]
                # print(video_ID)




                '''only use for generating transcript ans saving it only once'''

                # all_Transcript.append(get_text(video_ID))
                # with open("transcript007.txt",'w+') as f:
                #     f.writelines(all_Transcript.append(get_text(video_ID)))
                # print("hello")

                # with open("transcript007", 'wb') as f:
                #     pickle.dump(all_Transcript.transcrip, f)
                # with open('transcript007', 'wb') as f:
                #     pickle.dump(all_Transcript, f)
                # print("hello")
            



            '''use this after generating transcript and storing it'''
            with open('transcript007', 'rb') as f:
                transcript007=pickle.load(f)
                # print(transcript007)
            transcript=" ".join(transcript007)
            transcript=transcript.lower()
            transcript=transcript.split()
            new=[word for word in transcript if word not in stopwords]
            # print(new)
            new=[word for word in new if len(word)<=3]
            # print(new)
            count=Counter(new)
            print(count)


            

# print(all_Transcript)
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

