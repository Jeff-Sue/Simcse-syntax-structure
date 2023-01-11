# -*- coding: utf-8 -*-
import csv

import benepar, spacy
import sys

nlp = spacy.load('en_core_web_md')
if spacy.__version__.startswith('2'):
        nlp.add_pipe(benepar.BeneparComponent("benepar_en3"))
else:
    nlp.add_pipe("benepar", config={"model": "benepar_en3"})

path_name = "SentEval/data/downstream/STS/STSBenchmark/sts-test.csv"
# output_file = open(path_name+".benepar.en3.tree", "a", encoding='utf-8')
line_count = 0
with open(f'{path_name}_tree.csv','w',newline='',encoding='utf-8') as f:
    writer = csv.writer(f, delimiter= '\t')
    with open(path_name,'r') as f1:
        data = csv.reader(f1,delimiter='\t')
        for line in data:
            sent = []
            if line[0] == 'sent0':
                writer.writerow(line)
                continue
            #doc = nlp('The time for action is now. It is never too late to do something.')
            line_count += 1
            if line_count % 1000 == 0:
                print(line_count)

            # try:
            for cols in [5,6]:
                doc = nlp(line[cols].strip())
                line[cols] = list(doc.sents)[0]._.parse_string
            writer.writerow(line)

            # except:
            #     print('Sentence is too long: ', line_count, line)
            #     for cols in range(3):
            #         doc = nlp(line.strip()[:512])
            #         sent.append(list(doc.sents)[0])
            #     writer.writerow(sent)