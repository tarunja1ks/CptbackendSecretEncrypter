class encrypter:
    def __init__(self,text):
        self.text=text
    
    def encrypt(self): # this is the encryption algorithim of the text
        text=self.text.split() # First split all the text by the spaces into a list containing each word of the text
        encrypttext=""
        for word in text: # I iterate through each word in the sentence/text
            for character in word: # I go through each character in the world 
                encrypttext+=str(bin(ord(character)))[2:].zfill(8) # I add a 8 digit binary number, representing the character
            encrypttext+="~" # seperation character for each word
        self.text=encrypttext
        return encrypttext
    def decrypt(self, text): # This is decrypting the binary into english for a given shift combination
        decrypted=""
        for word in text.split('~'): # I first remove the seperation character of each word 
            for index in range(0,len(word),8): # I go through each digit in the binary version of the character and check if the decimal value outputs a character on the ASCII table
                if(int(word[index:index+8],2)>=32 and int(word[index:index+8],2)<=126):
                    decrypted+=chr(int(word[index:index+8],2))
                else:
                    return '' # if at any time it decrypts to a non-alphanumeirc character on the ASCII table then I stop decrypting and say this is a bad shift combination
                    
            decrypted+=" "

        return decrypted
        
enc=encrypter('i love to eat food')
enc.encrypt()

print(enc.decrypt('01101001~01101100011011110111011001100101~01100110011011110110111101100100~'))
    

            
                