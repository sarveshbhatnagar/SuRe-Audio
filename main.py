import transcribe_agent.transcribe as tr
import summary_agent.summarize as sm


if __name__ == '__main__':
    th = tr.Transcriber("J8Eh7RqggsU")
    th.transcribe()
    tt = tr.TTexts(th.transcript)

    summarizer = sm.Summarize(tt)
    scores, ttxts = summarizer.get_scores()

    # print(scores)
    total_duration = 0
    for i in range(len(scores)):
        if(scores[i] > 0.4):
            if(i-1 >= 0 and i+1 < len(scores)):
                print(
                    ttxts.transcripts[i-1].text, ttxts.transcripts[i].text, ttxts.transcripts[i+1].text)
                total_duration += ttxts.transcripts[i].duration
                total_duration += ttxts.transcripts[i-1].duration
                total_duration += ttxts.transcripts[i+1].duration
            else:
                print(ttxts.transcripts[i].text)
                total_duration += ttxts.transcripts[i].duration

    print("Total duration: ", total_duration)
    # print("Actual: ", th.duration)

    ttdur = 0
    for i in range(len(scores)):
        ttdur += ttxts.transcripts[i].duration

    print("Complete duration: ", ttdur)
