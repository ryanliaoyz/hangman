import random


play = True
GuessAttempts = 0
RightWrong = 0
GuessStatus = []
CorrectAnswer = []
#UsedGuess = []

fp=open("WordBank.txt")
WordPool = fp.readlines()
#print(WordPool)

word = WordPool[random.randint(0,100)]
#print(word)
#word.replace("\n","")
Wordlength = len(word) - 1
for Wordlength in range(0,Wordlength):
#$    print(Wordlength)
#$for letter in word:
    GuessStatus.append('_')
    CorrectAnswer.append(word[Wordlength])
print(GuessStatus)
#print(CorrectAnswer)

#$word = "procrastinating"
#$GuessStatus = ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'] #GuessStatus[0-14]
#$CorrectAnswer = ['p','r','o','c','r','a','s','t','i','n','a','t','i','n','g']

HangmanPic = ('''
--------
|   
|  
|  
|  
|________''','''
--------
|   |
|   
|  
|  
|________''','''
--------
|   |
|   O
|  
|  
|________''','''
--------
|   |
|   O
|   |
|  
|________''','''
--------
|   |
|   O
|  [|
|  
|________''','''
--------
|   |
|   O
|  [|]
|  
|________''','''
--------
|   |
|   O
|  [|]
|  / 
|________''','''
--------
|   |
|   O
|  [|]
|  / |
|________''','''
--------
|   |
|   O
|  [|]
|  / |
|________''') #8 attempts in total, last one for overflow

while GuessAttempts <= 6:
    if GuessStatus != CorrectAnswer:
        guess = input("Guess a Letter:")
        #$for i in range(0,15):
        for i in range(0,Wordlength):
            if word[i] == guess:
                GuessStatus[i] = word[i]
                RightWrong = 1
        if RightWrong == 1:        
            print("you are correct!")
            print(HangmanPic[GuessAttempts])
        else:
            print("you are wrong!")
            GuessAttempts = GuessAttempts + 1
            print(HangmanPic[GuessAttempts])
        print(GuessStatus)
        RightWrong = 0
    elif GuessStatus == CorrectAnswer:
        print("you win!")
        exit()
        

if GuessAttempts > 6:
    print("you lose, the correct answer is", word) 
#if play == False:
#    print("you used all the attempt, u lose!")
#    print("the correct answer is ", word)
#    TryAgain = input("press 0 to try again, 1 to quit")
#    if TryAgain == "0":
#        play = True
#        gamecore()
#    elif TryAgain == "1":
#        exit()
#    else:
#        print("try a valid answer")    


