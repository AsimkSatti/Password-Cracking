import hashlib

def Cracker():
    #Read into file of common passwords
    #Hash it with SHA-256
    #If True Write to a file (RealPassowrd,Its Matched)

    CrackedPasswords = open("CrackedPasswords2.txt",'a')
    CommonPasswordsfile = open("LikelyPasswords.txt","r")
    fobj = open('formspring.txt')
    cracked = fobj.read().strip().split()
    count=0
    found =0
    for Cline in CommonPasswordsfile:    
            for ptr in range(0,99):
                
                if(ptr<10):
                    salted_word = str(0) + str(ptr) + Cline.strip()
                else:
                    salted_word = str(ptr)+Cline.strip()

            
                hasher = hashlib.sha256()
                hasher.update(salted_word.encode('utf-8'))
                NewHash = hasher.hexdigest()
          
                NewHash=str(NewHash.strip())
                print(salted_word,NewHash)

                if NewHash in cracked and not in CrackedPasswords:
                    print ( NewHash,salted_word, file=CrackedPasswords2 )
               
                    CrackedPasswords.flush()
                    print("Password Cracked: ", NewHash)
     

                fobj.seek(0)        



if __name__ == "__main__":
    
    Cracker()
