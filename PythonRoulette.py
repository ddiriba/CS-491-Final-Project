#   import libraries
import random
import numpy as np

#   Python Roulette libary      
class roulette:
    

    def __init__(self):
        self.rollNumber = 0
        self.rollHistory = []
        self.colorHistory = []
        #this part was not coded by me (dawit), it is very inefficient
        self.red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        self.black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
        self.odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
        self.even = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
        

    def recordColorHistory(self):
        #   was the roll red?
        if self.rollNumber in self.red:
            self.colorHistory.append('Red')
        #   was the roll black?
        elif self.rollNumber in self.black:
            self.colorHistory.append('Black')
        #   if the roll wasn't black or red, then it was green
        else:
            self.colorHistory.append('Green')
        
        return self.colorHistory[-1]


    #   determine if the roll was odd or even
    def determineIfOddOrEven(self):
        #   was the roll odd?
        if self.rollNumber in self.odd:
            return('Odd')
        #   was the roll even?
        elif self.rollNumber in self.even:
            return('Even')
        #   if the roll wasn't odd or even it landed on 0, or 00
        else:
            return(False)
    
    #   lets roll the roulette wheel
    def rollTheRouletteWheel(self):
        print('--- Spinning the roullete wheel ---')
        self.rollNumber = random.randint(0,36)
       
        self.recordColorHistory()  
        #    add the roll to the history     
        self.rollHistory.append(self.rollNumber)
        print('The ball has landed on '+str(self.rollNumber)+' '+str(self.colorHistory[-1]))
        return(self.rollNumber)
     
    def give_results(self):
        result_odd_even = self.determineIfOddOrEven()
        return self.colorHistory[-1], result_odd_even, self.rollHistory[-1]