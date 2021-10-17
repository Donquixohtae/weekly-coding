import os
texts = []

with open("naver_news_2020.jsonl", "r", encoding="utf-8") as f:
   with open("output_1.txt", "w", encoding="utf-8") as f_w:
      for line in f:
         text = line.split("{\"text\": [")[1].split("], \"corpus\"")[0]
         texts.append(text)
      f_w.write(", ".join(texts))