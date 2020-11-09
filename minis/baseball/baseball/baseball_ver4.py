import numpy as np
helper =[ [[0 for i in range(10)]for j in range(10)] for k in range(10)]

# for i in range(0,10):
#     for j in range(0,10):
#         for k in range(0,10):
#             if(i != j or i != k or j != k):
                # list[i].append(int(j))
for ones in range(0,10):
    for twos in range(0,10):
        for threes in range(0,10):
            if(ones != twos and ones != threes and twos != threes):
                helper[ones][twos]= threes
                print(threes,end="\t")
    print("")

