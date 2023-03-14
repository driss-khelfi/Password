import hashlib

def password():
 all_specials = ['!', '@', '#', '$', '%', '^', '&', '*']
 all_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
 all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
                'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y' ,'z']
 res = False


string = input("Veuillez entrez votre mot de passe: ")
string_to_hash = string
hash_object = hashlib.sha256()
def name(x):
  list=[]
  i=0
  for i in x.split(' '):
    list.append((i, len(i)))
    return list
word = string
word_len = len(string)
if word_len<=7:
   print("Erreur: votre mot de passe est trop court")
else:
 all_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
 all_specials = ['!', '@', '#', '$', '%', '^', '&', '*']
 encrypted_password_list = []
 encrypted_tester = []
 upperx=0
 lowerx=0
 digitx=0
 passwords=0
 specialx=0
 for i in string:
  res = False
  if i.isupper():
      upperx +=1
  elif i.islower():
    lowerx +=1
  elif i in all_digits:
    digitx+=1
  elif i in all_specials:
    specialx +=1
 if upperx!=0 and lowerx!=0 and digitx!=0 and specialx!=0:
   print("Votre mot de passe semble correct")
   hash_object.update(string_to_hash.encode())
   hex_hash = hash_object.hexdigest()
   string = hex_hash
   passwords +=1
   if passwords==0:
    nouveau = open("mot_de_passe_crypte.txt", "x")
    with open("mot_de_passe_crypte.txt", "a") as fichier:
      fichier.write("encrypted password: "+ string)
    encrypted_password_list.append(string)
    for i in encrypted_password_list:
     if i not in encrypted_tester:
      encrypted_tester.append(i)
      passwords +=1
      print("Votre mot de passe a été enregisté!")
   elif passwords!=0:
    with open("mot_de_passe_crypte.txt", "a") as fichier:
      fichier.write("\nencrypted password: "+ string)
      encrypted_password_list.append(string)
      for i in encrypted_password_list:
       if i not in encrypted_tester:
        encrypted_tester.append(i)
        passwords +=1
        print("Votre mot de passe a été enregistré!")
       
    
        
        
       elif i in encrypted_tester:
         print("Erreur: votre mot de passe est déjà existant, veuillez en sélectionner un autre!")
         
         
         
         

   
    
   print(hex_hash)
   quit()

 elif digitx==0:
  print("Erreur: Votre mot de passe doit contenir au moins un chiffre")
 elif upperx!=0 and lowerx==0:
   print ("Erreur: Votre mot de passe ne contient pas de minuscules")
 elif upperx==0 and lowerx!=0:
  print("Erreur: Votre mot de passe ne contient pas de majuscules")
 elif specialx==0:
  print("Erreur: Votre mot de passe doit contenir au moins un caractère spécial ")


  