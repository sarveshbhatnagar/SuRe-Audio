

class CompletenessAgent:
    def __init__(self, scores, ttexts):
        self.scores = scores
        self.ttexts = ttexts

    def get_complete_sentence(self, index):
        """
        Returns a complete sentence based on "."
        """
        endsWell = False
        startsWell = False
        start_str = ""
        end_str = ""
        stind = index
        endind = index
        if(self.ttexts.transcripts[index].text.endswith(".")):
            endsWell = True
        try:
            if(self.ttexts.transcripts[index-1].text.endswith(".")):
                startsWell = True
        except IndexError:
            startsWell = True
        if(endsWell and startsWell):
            return " " + self.ttexts.transcripts[index].text + " ", stind, endind
        if(not startsWell):
            # Make it correct
            # start_str = ""
            count=0
            for i in range(index-1, -1, -1):
                if(self.ttexts.transcripts[i].text.endswith(".")):
                    stind = i+1
                    # print(self.ttexts.transcripts[i].text)
                    break

                start_str = self.ttexts.transcripts[i].text + " "+ start_str + " "
                tokens=start_str.split(" ")
                if len(tokens)>=7:
                    stind=i 
                    break

        if(not endsWell):
            # Make it correct
            # end_str = ""
            for i in range(index+1, len(self.ttexts.transcripts)):
                if(self.ttexts.transcripts[i].text.endswith(".")):
                    end_str += self.ttexts.transcripts[i].text + " "
                    endind = i
                    break
                end_str += self.ttexts.transcripts[i].text + " "
                tokens=end_str.split(" ")
                if len(tokens)>=7:
                    endind=i
                    break
        return start_str + self.ttexts.transcripts[index].text + end_str, stind, endind


# if __name__ == "__main__":
#     mystr = "Alright, I am sarvesh um and I will be teaching ah you about Natural Language Processing."
#     tokens = nltk.word_tokenize(mystr)
#     tagged = nltk.pos_tag(tokens)
#     print(tagged)
