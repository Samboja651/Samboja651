# See the Instructions tab.
# Scroll down to see where you should write your solution
roster = [
  "Thibaut Courtois",
  "Dani Carvajal",
  "Brahim Díaz",
  "Éder Militão",
  "Jesús Vallejo",
  "Nacho",
  "Eden Hazard",
  "Toni Kroos",
  "Karim Benzema",
  "Takefusa Kubo",
  "Álvaro Odriozola",
  "Luka Modrić",
  "Marco Asensio",
  "Marcelo",
  "Andriy Lunin",
  "Martin Ødegaard",
  "Casemiro",
  "Federico Valverde",
  "Luka Jović",
  "Sergio Ramos",
  "Lucas Vázquez",
  "Gareth Bale",
  "Dani Ceballos",
  "Vinícius Júnior",
  "Raphaël Varane",
  "Rodrygo",
  "Isco",
  "Ferland Mendy",
  "Mariano"
]

# Write your solution below

print("\nThe current Real Madrid roster:\n")
# Print the current roster using a for loop
# for (i,rosters) in enumerate(roster):
#   print(f"{i+1}.{rosters}")
for i in roster:
  print(i)

# Remove players using pop()
roster.pop(2)
roster.pop((9-1))
roster.pop((10-2))
roster.pop((15-3))
roster.pop((19-4))
roster.pop((24-5))
  
# Add players using append()
roster.append('Eduardo Camavinga')
roster.append('David Alaba')

print("\n------")
print("\nThe new Real Madrid roster:\n")
# Print the new roster using a for loop
# for (a,rosters) in enumerate(roster):
#   print(f"{a+1}.{rosters}")
for a in roster:
  print(a)
  