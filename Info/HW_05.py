from statistics import mean
from random import randint
class Elevi():
  def __init__(self, ID, note):
    self.ID = ID  # ID-ul elevului
    self.note = note  # Lista notelor elevului

  def verifica_promovarea(self):
    
    
    media = mean(self.note)
    if media < 5:
      return False
    else:
      return True

  def afiseaza_rezultatul(self):
    if self.verifica_promovarea():
      print(f"{self.ID} - promovat")
      return True
    else:
      print(f"{self.ID} - picat")
      return False
list_Elevi = []
list_ID = []
nr_elevi = 17
for I in range (nr_elevi):
    ID = randint (1000, 9999)
    temp_note = []
    while ID in list_ID:
      ID = randint (1000, 9999)
    nr_note = randint(3,12)
    for J in range (nr_note):
      nota = randint (1,10)
      temp_note.append(nota)
    temp_elev = Elevi(ID,temp_note)
    list_Elevi.append(temp_elev)
    list_ID.append(ID)
count_promoF = 0
count_promoB = 0
totalB=0
totalF=0
for elev in list_Elevi:
  print("nume",elev.ID)
  print('note',elev.note)
  val = elev.afiseaza_rezultatul()
  if val:
    if (elev.ID // 1000) % 2 == 0:
      count_promoF += 1
    else: 
      count_promoB += 1
  if (elev.ID // 1000) % 2 == 0:
    totalF += 1
  else: 
    totalB += 1
print("promovabilitate:",((count_promoF + count_promoB) / len(list_Elevi)) * 100)
print("promovabilitateF:",((count_promoF ) / totalF) * 100)
print("promovabilitateF:",((count_promoB ) / totalB) * 100)