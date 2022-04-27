
class RoulettePlayer:
    def __init__(self):
        self.pot = 0
        self.bet = 0
        self.in_game = True
        self.has_drink = False
        self.game_duration = 0

    def update_bet(self):
        bet_amount = input('How much money would you like to bet? (2-500)')
        try:
            if int(bet_amount) >= 2 and int(bet_amount) <= 500:
                if int(bet_amount) > self.pot:
                    print('Please Enter a bet less than your pot')
                    return False
                else:
                    self.bet =int(bet_amount)
                    return True
            else:
                print('Please enter a bet between 2 and 500 dollars')
                return False
        except Exception as e :
            print(e)
            print('Please Try Again and only enter integers')
            return False
        return True                 
            
    def get_pot(self):
        return self.pot
    
    def update_pot(self, amount):
        self.pot += int(amount)
        self.game_duration += 1
        if self.pot <= 0:
            self.in_game = False
            print('Thanks for playing, you have lost all your money, please deposit more.')
            
    def give_tip(self, tip_amount):
        if self.pot < tip_amount:
            print("Sorry I am broke")
            return False
        else:
            print("Waiteress tipped successfully")
            self.pot -= tip_amount
        return True

    def get_game_duration(self):
        return self.game_duration

    def leave_table(self):
        #indicate winnings and such
        self.in_game = False
        return self.in_game
    