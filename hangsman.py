## made by yuval_zohar


from string import ascii_lowercase
import random


class hangsman():
    def __init__(self):
        self.wordlist=[]
        
    def words(self):
        self.maxlength=input("please input the max length of the words that you want to guess")
        self.maxlength=int(self.maxlength)
        if type(self.maxlength)==int:
            lines = open('C:\\Users\\yuval\\Desktop\\words.txt').read().splitlines()
            for word in lines :
                word.strip('')
                word.lower()
                if self.maxlength==0:
                    print("impossible word length")
                    break
                elif len(word)<=self.maxlength:
                    self.wordlist.append(word)
                elif len(word)>self.maxlength:
                    continue
        print(self.wordlist)
    

        



    def endofgame(self):
        while True :
            pass
    def guess(self):
        self.numofguess=input("please enter the number of your guess you want to play")
        self.numofguess=int(self.numofguess)
        print(self.wordlist)
        if self.numofguess>0:
                self.curr_word=self.wordlist[random.randrange(1, len(self.wordlist),1)]
                for guess in range(self.numofguess):
                        for i in range(len(self.curr_word)):
                                someguess=input("please enter some char for guess or the whole word !")
                                if someguess==self.curr_word:
                                        print("you win !")
                                        print("the word is:" + self.curr_word)
                                        self.endofgame()
                                if someguess==self.curr_word[i]:
                                        print('the char included in the word ! nice guess')
                                        break
                                if someguess!=self.curr_word[i]:
                                        print('wrong guess.....')
                print('out of guesses, Looser !')
        else: 
                print("wrong number")


def main ():
    playgame=hangsman()
    playgame.words()
    playgame.guess()

main()


