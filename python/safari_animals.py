# Know the big 5 animals

animals = ["Lion", "Elephant", "Leopard", "Rhino", "Buffalo"]

print("Enter a number to read a description of an animal.")
for (i, animal) in enumerate(animals):#[(1, Lion), (2,Elephant), ].  [1,2,3,4]
  print(f"{i+1}. {animal}")

descriptions = [
  "The lion (Panthera leo) is a large mammal of the Felidae (cat) family. Some large males weigh over 250 kg (550 lb). Today, wild lions live in sub-Saharan Africa and in Asia. Lions are adapted for life in grasslands and mixed areas with trees and grass. The relatively small females are fast runners over short distances, and coordinate their hunting of herd animals.",
  "Elephants are the largest existing land animals. Three living species are currently recognised: the African bush elephant, the African forest elephant, and the Asian elephant. They are an informal grouping within the proboscidean family Elephantidae. Elephantidae is the only surviving family of proboscideans; extinct members include the mastodons. Elephantidae also contains several extinct groups, including the mammoths and straight-tusked elephants. African elephants have larger ears and concave backs, whereas Asian elephants have smaller ears, and convex or level backs. The distinctive features of all elephants include a long proboscis called a trunk, tusks, large ear flaps, massive legs, and tough but sensitive skin. The trunk is used for breathing, bringing food and water to the mouth, and grasping objects. Tusks, which are derived from the incisor teeth, serve both as weapons and as tools for moving objects and digging. The large ear flaps assist in maintaining a constant body temperature as well as in communication. The pillar-like legs carry their great weight.",
  "The African leopard (Panthera pardus pardus) is the nominate subspecies of the leopard, native to many countries in Africa. It is widely distributed in most of sub-Saharan Africa, but the historical range has been fragmented in the course of habitat conversion. Leopards have also been recorded in North Africa as well.",
  "A rhinoceros (/raɪˈnɒsərəs/, from Greek rhinokerōs 'nose-horned', from rhis 'nose', and keras 'horn'), commonly abbreviated to rhino, is a member of any of the five extant species (or numerous extinct species) of odd-toed ungulates in the family Rhinocerotidae. (It can also refer to a member of any of the extinct species of the superfamily Rhinocerotoidea.) Two of the extant species are native to Africa, and three to South and Southeast Asia.",
  "The African buffalo (Syncerus caffer) is a large sub-Saharan African bovine. Syncerus caffer caffer, the Cape buffalo, is the typical subspecies, and the largest one, found in Southern and East Africa. S. c. nanus (the forest buffalo) is the smallest subspecies, common in forest areas of Central and West Africa, while S. c. brachyceros is in West Africa and S. c. aequinoctialis is in the savannas of East Africa. The adult African buffalo's horns are its characteristic feature: they have fused bases, forming a continuous bone shield across the top of the head referred to as a 'boss'. It is widely regarded as one of the most dangerous animals on the African continent, and according to some estimates it gores, tramples, and kills over 200 people every year."
]

while True:  
  try:
    number = int(input())
    if number > 0 and number < 6:
      print(animals[number-1])
      print(descriptions[number-1])
      break
    else:
      print("Enter a number from the given list")
      continue
  except:
    print("Enter a valid number")
    continue
    

