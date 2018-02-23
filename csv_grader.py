import pandas as pd
import sys
import os
from numpy import median, mean


REVIEWS = "./peer_reviews/"
def send_mail(): 
    pass

def review_grade(): 
    wFile = open('grades.csv', 'a') 
    wFile.write('id, grade\n')
    rFile = open('reviews.csv')
    pdFile = pd.read_csv(rFile)
    listval = []
    scoreDict = dict()

    # this for loop covers scoring, you'll have to change it based on the rubric
    # listcols is the list of rubric criteria
    
    for index, row in pdFile.iterrows():
        listcols = [row["id"], row["1"], row["2"], row["3"],row["4"], row["5"], row["6"], row["7"], row["8"], row["9"], row["10"], row["11"], row["12"]]
        score = 0
        for i in range(0, len(listcols)): 
            if i == 0 and listcols[0] not in scoreDict:
                scoreDict[listcols[0]] = []
            elif i == 0 and listcols[0] in scoreDict: 
                pass
            elif i == 3: 
                if listcols[i] > 5: 
                    score += 5
                else: 
                    score += listcols[i]
            elif i == 4: 
                if listcols[i] > 5: 
                    score += 5
                else: 
                    score += listcols[i]
            elif i == 5: 
                if listcols[i] > 5: 
                    score += 5
                else: 
                    score += listcols[i]
            elif i == 6: 
                if listcols[i] > 5: 
                    score += 5
                else: 
                    score += listcols[i]
            else: 
               score += listcols[i]
        scoreDict[listcols[0]] += [score]
    for key, value in scoreDict.iteritems():
        scoreDict[key] = sorted(value, key=long)
        scoreDict[key] = median(scoreDict[key])
        listval += value

    for key, value in scoreDict.iteritems():
        wFile.write(str(key) + ',' + str(value) + '\n')
        

def assignment_grade(): 
    wFile = open('reviews.csv', 'a')
    wFile.write('id, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12\n')
    for file in os.listdir(REVIEWS):
        print file
        fpath = REVIEWS + file
        if file[-4:] == '.csv':
            f = open(fpath)
            pdfile = pd.read_csv(f)
            for index, row in pdfile.iterrows():
                try:
                    listcols = [str(row["id"]) + ',', str(row["1"]) + ',', str(row["2"]) + ',', str(row["3"]) + ',', str(row["4"]) + ',', str(row["5"]) + ',', str(row["6"]) + ',', str(row["7"]) + ',', str(row["8"]) + ',', str(row["9"]) + ',', str(row["10"]) + ',', str(row["11"]) + ',', str(row["12"]) + '\n']
                    for col in listcols: 
                        wFile.write(col)
                except Exception as e: 
                    print e
                    print 'this person formatted incorrectly: ' + file[:-4]
        else: 
            print 'this person submitted incorrectly: ' + file
    wFile.close()
    f.close()