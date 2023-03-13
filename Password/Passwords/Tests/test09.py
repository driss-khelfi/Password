def password():
 all_specials = ['!', '@', '#', '$', '%', '^', '&', '*']
 all_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
 all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
                'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y' ,'z']
 res = False


string = input("Veuillez entrez votre mot de passe: ")
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
 upperx=0
 lowerx=0
 digitx=0
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
   quit()
 elif digitx==0:
  print("Erreur: Votre mot de passe doit contenir au moins un chiffre")
 elif upperx!=0 and lowerx==0:
   print ("Erreur: Votre mot de passe ne contient pas de minuscules")
 elif upperx==0 and lowerx!=0:
  print("Erreur: Votre mot de passe ne contient pas de majuscules")
 elif specialx==0:
  print("Erreur: Votre mot de passe doit contenir au moins un caractère spécial ")