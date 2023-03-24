# See the full instructions in the instructions tab

print("Generate the scrabble score for a word. ")

# Get a word as input
word = input("Enter a word: ")

# Start the score at 0
score = 0
for letter in word:
  if letter in 'aeilnorstu':
    score +=1
  elif letter in 'dg':
    score +=2
  elif letter in 'bcmp':
    score +=3
  elif letter in 'fhvwy':
    score +=4
  elif letter in 'k':
    score +=5
  elif letter in 'jx':
    score +=8
  elif letter in 'qz':
    score +=10
# INSTRUCTIONS:
# Loop over the letters in the word
## At each step in the loop, add the value for that letter
## To find the letter value, check if the letter is in the set of letters for each score, like this:

  # if letter in 'aeilnorstu':
  #   score += 1
  # elif letter in 'dg':
  #   score += 2

## See the full table of letter values in the Instructions.

## Print out the score
print(f"{word} has a scrabble score of {score}")