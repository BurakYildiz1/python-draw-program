import random

# Kura çekilecek liste
names = ["", "", "", "", "","","","","","","",""]
teams = ["",""]
# Kura çekilenlerin tutulduğu liste
drawn = []

#listeleri karıştır
random.shuffle(names)
random.shuffle(teams)

while len(names) > 0:
  # Rastgele bir öğe seç
  name = random.choice(names)
  team = random.choice(teams)

  # Öğeyi listeden çıkar
  names.remove(name)
  teams.remove(team)

  # Öğeyi daha önce çekilip çekilmediğini kontrol et
  if name in drawn:
    print(f"{name} daha önce çekildi, tekrar çekilemez.")
    print(f"{team} daha önce çekildi, tekrar çekilemez.")
  else:
    # Öğeyi ekrana yazdır
    print("====================================")
    print(f"Çekilen isim: {name}")
    print(f"Çekilen isim: {team}")
    print("====================================")

    # Öğeyi çekilenler listesine ekle
    drawn.append(name)
    drawn.append(team)
    
print("Kura çekme işlemi tamamlandi.")