import pandas as pd
import csv

new_row = [['Text', 'IsEnc']]
with open('datatrainisenglish.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(new_row)
    file2 = open("englishsentences.txt", 'r')
    Lines = file2.readlines()
    file2.close()
    for i in Lines:
        new_row = [str(i[:len(i) - 1]), '0']
        writer.writerow(new_row)

    df=pd.read_csv('data.csv',sep=',')
    Texts=list(df['Text'])
    for i in Texts:
        new_row = [i, '1']
        writer.writerow(new_row)
        
    df2=pd.read_csv('tweet_emotions.csv')
    Texts=list(df2['content'])
    for i in Texts:
        new_row = [i, '0']
        writer.writerow(new_row)
