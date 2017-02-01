import random

def getWord():
   """Get a word from the dictionary text file - done once. Words are held in list for all later games""" 
   f = open("wordsEn.txt")
   words = []
   for word in f:
      if len(word) > 2: #only add words of 3 characters or more
         words.append(word.rstrip('\n')) #strip the end of line from each word
   return words

def guessLetter(word):
    """Main guessing game"""
    usedLetters = [] #list of used letters
    miss = 0 #counts the number of missed letters
    displayWord = [] #displays the word being guessed
    for i in range(len(word)):
       displayWord.append("-") #initially sets the displayed word's letters as hyphens
   
    while miss != 8: #game will loop until number of misses is 8 
       for i in displayWord: #displays the word to guess '-' if letter not found
          print(i,end="")
       print()
       print("Used Letters = ",end="")

       for i in usedLetters: #display used letters
          print(i,end="")
       print()
       print("Misses = ",miss)#diplay misses
       
       guess = input("Guess a Letter? ",) 

       found = False #marks if the guessed letter has been found in the word   

       if guess in usedLetters:
          print("You have used that letter before")
              
       elif found == False:
          miss = miss + 1
          usedLetters.append(guess)
          usedLetters.sort() 
       charPosition = 0

       for i in word:
          if guess == i:
             displayWord[charPosition] = i
             found = True
          charPosition = charPosition + 1

       # Have you guessed the word correctly
       displayWordStr = "" #convert the displayWord list into a string
       for i in displayWord:
          displayWordStr = displayWordStr + i
         
       if miss == 8:
          print("YOU HAVE LOST")
         
       if displayWordStr == word: #see if the displayWordStr matches the word
          print("YOU HAVE WON")
  

words = getWord() # gets words
randomWord = random.choice(words) #chooses a random word to guess
guessLetter(randomWord)
