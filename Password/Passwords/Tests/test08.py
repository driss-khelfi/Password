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
 res = False
 for i in string:
  res = False
  if i.isupper():
      res = True
      print("Votre mot de passe semble correct")
      quit()
  else:
    res = False
print("Erreur: Votre mot de passe ne contient pas de majuscules")

    
    
 
 
password()