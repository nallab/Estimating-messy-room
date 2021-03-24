import csv
import glob
import pandas as pd
import numpy as np

all_path = glob.glob('./total/investigate*')
sum = 0
for path in all_path:
    #df = pd.read_csv(path, header=1, index_col=0)
    df = pd.read_csv(path, index_col=0)
    #df2 = df.dropna(how='all')
    #df2 = df.drop(df.index[[22,31,44,76,84,92,101,121,122,125,147,148,152,153,194,200,211,222,229,234,237,241,242,244,246,248,252,257,263,270,279,291]])
    df2 = df.drop(df.index[[0,3,7,9,10,11,13,15,16,18,19,20,22,23,24,25,27,28,29,30,31,35,38,39,40,
                            41,44,45,46,47,49,54,58,65,74,52,76,80,82,84,85,86,87,89,92,94,97,101,103,
                            107,114,119,120,121,122,123,125,133,138,141,142,144,146,147,148,152,153,
                            155,158,161,162,163,164,166,167,171,174,176,177,183,187,188,189,190,191,
                            194,196,200,203,206,207,208,209,210,211,218,219,222,224,226,228,229,230,
                            231,233,234,235,237,240,241,242,243,244,245,246,247,248,251,252,253,257,
                            260,261,263,265,266,269,270,271,272,274,275,276,278,279,280,282,289,291,294,
                            295,296,297,299]])
    #df2 = df.drop(df.index[[22,84,92,122,125,148,152,194,200,211,222,234,237,241,244,257,263,270,279]])
    df3 = pd.DataFrame(df2.iloc[:, :1], dtype='int64')
    df4 = df3.to_numpy()
    #print(df4.shape)
        
    sum = sum + df4
    
label = []
#print(sum)
for s in sum:
    if s >= 3:
        #print('hoge')
        label.append(1)
    else:
        #print(s)
        label.append(0)

#print(len(label))
print(label[87])
count = 0
zero = 0
for lab in label:
    if lab == 1:
        count += 1
    else:
        zero += 1

print(count)
print(zero)
np_label = np.array(label)
print(np_label.shape)
print(len(np_label))
np.save('./labels4', np_label)
