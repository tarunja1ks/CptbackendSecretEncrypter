import pandas as pd
import csv
from encryption import encrypter




new_row = [['Text', 'IsEnc']]
with open('AIcodebyme/datatrainisenglish.csv', 'a', newline='') as file: # this is combining the data into a common csv file for training 
    
    
    
    writer = csv.writer(file)
    writer.writerows(new_row)
    file2 = open("AIcodebyme/englishsentences.txt", 'r')
    Lines = file2.readlines()
    file2.close()
    for i in Lines:
        new_row = [str(i[:len(i) - 1]), '0'] # I add all sentences in here as examples of english and into the dataset
        original=str(i[:len(i) - 1])
        writer.writerow(new_row)
    print("done")
        
        
        
        
    
    df2=pd.read_csv('AIcodebyme/tweet_emotions.csv')
    Texts=list(df2['content'])
    iteration=0
    for msg in Texts:
        new_row = [msg, '0'] # I first add the basic data, which is English and put in the dataset
        encdec=encrypter(msg)
        binary=encdec.encrypt() # I then run the encryption, and decryption algorithims and input into the database so I will have exmaples of incorrect english which is jumbled up and out of order
        length=len(binary)
        for shiftvalue in range(length): 
            decrypted=encdec.decrypt(binary)
            if(decrypted.isascii() and decrypted!=''):  
                shifted_row=[decrypted,'1']
                writer.writerow(shifted_row)
            binary=binary[1:]+binary[:1]
            
        writer.writerow(new_row)
        iteration+=1
        if(iteration==10000): # I break at 10,000 iterations of this due to hardware limitations and to avoid freezing or slowing down my computer
            break
