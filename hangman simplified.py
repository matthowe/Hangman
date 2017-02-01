import random

def getWord():
   f = open("wordsEn.txt")
   words = []
   for word in f:
      if len(word) > 2: #only add words of 3 characters or more
         words.append(word.rstrip('\n')) #strip the end of line from each word
   randomWord = random.choice(words)
   return randomWord

def guessLetter(word): 
   usedLetters = []
   miss = 0
   displayWord = []
   for i in range(len(word)):
      displayWord.append("*")
   keepPlaying = True
   
   while keepPlaying == True:
      for i in displayWord:
         print(i,end="")
      print()
      print("Used Letters = ",end="")
      usedLetters.sort()
      for i in usedLetters:
         print(i,end="")
      print()
      print("Misses = ",miss)
      guess = input("Guess a Letter? ",)

      if guess in usedLetters:
         print("You have used that letter before")
         return(keepPlaying,displayWord, miss, usedLetters)
      
      charPosition = 0


      
      found = False
      for i in word:
         if guess == i:
            displayWord[charPosition] = i
            found = True
         charPosition = charPosition + 1
      if found == False:
         miss = miss + 1
         usedLetters.append(guess)
         

      # Have you guessed the word correctly
      displayWordStr = "" #convert the displayWord list into a string
      for i in displayWord:
         displayWordStr = displayWordStr + i

      if displayWordStr == word: #see if the displayWordStr matches the word
         print("YOU HAVE WON")
         keepPlaying = False

      if miss == 8:
         print("YOU HAVE LOST")
         keepPlaying = False

      
      
   
# generates our word to guess
word = getWord()
print(word)

# generates the guess word - starts all blanks
#displayWord = []  #displayWord is a list as we need to change the characters
                  #from blanks to guessed letters
                  #and strings are immuatable


#usedLetters = []
#keepPlaying = True
#miss = 0

guessLetter(word)


#while keepPlaying == True:
#   keepPlaying, displayWord, miss, usedLetters = guessLetter(word, displayWord, keepPlaying, miss, usedLetters)




   
