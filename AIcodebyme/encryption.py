class encrypter:
    def __init__(self,text):
        self.text=text
    
    def encrypt(self):
        text=self.text.split()
        encrypttext=""
        for word in text:
            for character in word:
                encrypttext+=str(bin(ord(character)))[2:].zfill(8)
            encrypttext+="~"
        self.text=encrypttext
        return encrypttext
    def decrypt(self, text):
        decrypted=""
        for word in text.split('~'):
            for index in range(0,len(word),8):
                if(int(word[index:index+8],2)>=32 and int(word[index:index+8],2)<=126):
                    decrypted+=chr(int(word[index:index+8],2))
                else:
                    return ''
                    
            decrypted+=" "

        return decrypted
        
enc=encrypter('i love to eat food')
enc.encrypt()

print(enc.decrypt('01101001~01101100011011110111011001100101~01100110011011110110111101100100~'))
    

            
                