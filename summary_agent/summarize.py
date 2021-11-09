# import preprocessor
from summary_agent.preprocessor import PreProcess


class Summarize:
    def __init__(self, ttxts):
        self.ttxts = ttxts

    def get_scores(self):
        """
        Processes the text and returns a list of scores for each text.

        returns:
            list of scores, TTexts instance with scores installed.


        """
        full_text = self.ttxts.get_complete_text()
        sentence_list = self.ttxts.get_transcripts_text_list()

        # Preprocess the text
        pp = PreProcess(full_text)
        full_freq = pp.get_word_frequency()
        scores = []
        for sentence in sentence_list:
            scores.append(pp.tfIdf_score(sentence, full_freq))

        for i in range(len(self.ttxts.transcripts)):
            self.ttxts.transcripts[i].set_score(scores[i])

        return scores, self.ttxts
