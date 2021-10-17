import os
import multiprocessing

def scrap(file_path):
    with open(file_path, "r", encoding='utf-8') as f:
        with open(file_path+'output', "w", encoding='utf-8') as f_w:
            texts = []       
            for line in f:
                ##이름바꾸기 찾아
                text = line.split("{\"text\": [")[1].split("], \"corpus\"")[0]
                texts.append(text)

INPUT_DIR = "/home/donquixohtae/weekly-coding/data"

jobs = []

for filename in os.listdir(INPUT_DIR):
    file_path = os.path.join(INPUT_DIR, filename)

    job = multiprocessing.Process(target=scrap, args=(file_path,))
    jobs.append(job)
    job.start()

for job in jobs:
    job.join()








