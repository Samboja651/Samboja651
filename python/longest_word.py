# Follow the instructions in the tab to the right
# Write your code below
# count = 0
word = []

print("Enter five words")
for i in range(5):
  word_enter = input("Enter a word: ")
  word.append(word_enter)
  word_length = len(word[0])
  if word_length < i:
    word_length = i
    

print(word_length)
# i don't understand how to print the longest word it just keeps printing the length of longest word
