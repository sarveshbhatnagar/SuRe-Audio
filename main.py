import transcribe_agent.transcribe as tr
import summary_agent.summarize as sm
import completeness_agent.complete as cm
import numpy as np

if __name__ == '__main__':
    th = tr.Transcriber("oPzyIShVmvw")
    # th.transcribe()
    # th.save_transcript("edgecomputing")
    th.load_transcript("edgecomputing")
    divide = 20  # Optimization parameter for % compression.
    parts = len(th.transcript) // divide
    parts_list = [th.transcript[i:i + parts]
                  for i in range(0, len(th.transcript), parts)]
    main_scores = []
    main_ttxts = []

    important_tindx = []
    total_duration = 0
    complete_duration = 0
    # Find important index in parts_list

    final_text = ""

    for i in range(len(parts_list)):
        tt = tr.TTexts(parts_list[i])
        summarizer = sm.Summarize(tt)

        scores, ttxts = summarizer.get_scores()
        cmp = cm.CompletenessAgent(scores, ttxts)
        main_scores.append(scores)
        main_ttxts.append(ttxts)
        val = np.percentile(scores, 90)
        cur_tindx = []
        for j in range(len(scores)):
            cur_tindx.append(j)
            complete_duration += ttxts.transcripts[j].duration
            if(scores[j] > val):
                # important_tindx.append((i, j))
                total_duration += ttxts.transcripts[j].duration
                # print(ttxts.transcripts[j].text)
                # print(cmp.get_complete_sentence(j))
                res = cmp.get_complete_sentence(j)
                final_text += res[0]
                important_tindx.append((i, res))

                # print(res)

    # print(important_tindx)
    # print(len(important_tindx))
    print(final_text)
    # print(len(final_text))
    # tt = tr.TTexts(th.transcript)
    # original_text = tt.get_complete_text()
    # print(len(original_text))
    # print("Reduced to: ", len(final_text) / len(original_text))

    # print("Total duration: ", total_duration)

    print(important_tindx)
    # print(main_ttxts[2].transcripts[18].get_start(),
    #       main_ttxts[2].transcripts[18].get_end())
    # print(original_text)
    # print("Actual: ", th.duration)

    # print("Complete duration: ", complete_duration)
