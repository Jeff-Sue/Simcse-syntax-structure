import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
# with open('data/hans_train.csv_tree.csv','r') as f:
#     data = csv.reader(f,delimiter='\t')
#     with open('data/hans_train_triple_tree.csv','w',newline='',encoding='utf-8') as f1:
#         writer = csv.writer(f1)
#         writer.writerow(['sent0','sent1','hard_neg'])
#         for i in data:
#             if int(float(i[4])) == 0:
#                 writer.writerow([i[5],"",i[6]])
#             if int(float(i[4])) == 5:
#                 writer.writerow([i[5],i[6],""])
# with open('data/nli_for_simcse_tree.csv','r',newline='',encoding='utf-8') as f:
#     with open('data/hans_train_triple_tree.csv','r',newline='',encoding='utf-8') as f1:
#         data1 = csv.reader(f)
#         data2 = csv.reader(f1)
#         with open('data/train_tree.csv','w',newline='',encoding='utf-8') as f2:
#             writer = csv.writer(f2)
#             writer.writerow(['sent0','sent1','hard_neg'])
#             for i in data1:
#                 if i[0] == 'sent0':
#                     continue
#                 writer.writerow(i)
#             for i in data2:
#                 if i[0] == 'sent0':
#                     continue
#                 writer.writerow(i)
with open('data/templates.csv','r') as f:
    data = csv.reader(f,delimiter='\t')
    value1 = []
    for i in data:
        value1.append(i[0])
    t = np.arange(0,len(value1),1)
    linesList = plt.plot(t,value1)
    plt.show()
