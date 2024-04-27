import pandas as pd
import csv
from encryption import encrypter




new_row = [['Text', 'IsEnc']]
with open('AIcodebyme/datatrainisenglish.csv', 'a', newline='') as file:
    
    
    
    writer = csv.writer(file)
    writer.writerows(new_row)
    file2 = open("AIcodebyme/englishsentences.txt", 'r')
    Lines = file2.readlines()
    file2.close()
    for i in Lines:
        new_row = [str(i[:len(i) - 1]), '0']
        original=str(i[:len(i) - 1])
        writer.writerow(new_row)
    print("done")
        
        
        
        
    
    df2=pd.read_csv('AIcodebyme/tweet_emotions.csv')
    Texts=list(df2['content'])
    iteration=0
    for msg in Texts:
        new_row = [msg, '0']
        encdec=encrypter(msg)
        binary=encdec.encrypt()
        length=len(binary)
        for shiftvalue in range(length):
            decrypted=encdec.decrypt(binary)
            if(decrypted.isascii() and decrypted!=''):  
                shifted_row=[decrypted,'1']
                writer.writerow(shifted_row)
            binary=binary[1:]+binary[:1]
            
        writer.writerow(new_row)
        iteration+=1
        if(iteration==10000):
            break
