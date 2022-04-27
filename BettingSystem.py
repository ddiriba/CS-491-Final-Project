
class RouletteBetting:
    def __init__(self):
        self.bet_type = '' #Odd/Even = 1 , Color = 2, Numerical =3
        self.valid_bet = False
        self.bet_chosen = ''
        self.win_multiplier = 0


    def choose_bet_type(self):
        print('1. Odd or Even')
        print('2. Red or Black')
        print('3. Numbers (0-36)')

        while not self.valid_bet:
            self.bet_type = input('What type of bet would you like? (choose 1,2 or 3)')
            try:
                if int(self.bet_type) < 1 and int(self.bet_type) > 3:
                    print('Please enter a valid choice (choose 1,2 or 3) ')
                else:
                    self.valid_bet = True
            except:
                print('Please enter a valid choice (choose 1,2 or 3) ')
                pass

        self.valid_bet = False
        while not self.valid_bet:
            if self.bet_type == '1':
                self.bet_chosen = input('(1) Odd or (2) Even')
                try:
                    if int(self.bet_type) < 1 and int(self.bet_type) > 2:
                        print('Please enter a valid choice (choose 1 or 2) ')
                    else:
                        self.valid_bet = True
                        if int(self.bet_type) == 1:
                            self.bet_chosen = 'Odd'
                        else:
                            self.bet_chosen = 'Even'
                        return self.bet_chosen
                except:
                    print('Please enter a valid choice (choose 1 or 2)')
                
            elif self.bet_type == '2':
                self.bet_chosen = input('(1) Red or (2) Black')
                try:
                    if int(self.bet_type) < 1 and int(self.bet_type) > 2:
                        print('Please enter a valid choice (choose 1 or 2) ')
                    else:
                        self.valid_bet = True
                        if int(self.bet_type) == 1:
                            self.bet_chosen = 'Red'
                        else:
                            self.bet_chosen = 'Black'
                        return self.bet_chosen
                except:
                    print('Please enter a valid choice (choose 1 or 2)')

            elif self.bet_type == '3':
                self.bet_chosen = input('Choose a number between 0 and 36')
                try:
                    if int(self.bet_type) < 0 and int(self.bet_type) > 36:
                        print('Please enter a valid integer between 0 and 36 ')
                    else:
                        self.valid_bet = True
                        return self.bet_chosen
                except:
                    print('Please enter a valid integer between 0 and 36 ')
            return self.bet_type

    def get_bet_type(self):
        return self.bet_chosen

    def check_results_bet(self, result_color, result_odev, result_num):
        if self.bet_chosen == 'Red' or self.bet_chosen == 'Black':
            if self.bet_chosen == str(result_color):
                self.win_multiplier = 1
                print('You win with a multiplier of 1 to 1')
                return self.win_multiplier
            else:
                self.win_multiplier = -1
                print('You lose')
                return self.win_multiplier
        elif self.bet_chosen == 'Odd' or self.bet_chosen == 'Even':
            if self.bet_chosen == str(result_odev):
                self.win_multiplier = 1
                print('You win with a multiplier of 1 to 1')
                return self.win_multiplier
            else:
                self.win_multiplier = -1
                print('You lose')
                return self.win_multiplier
        else:
            if self.bet_chosen == str(result_num):
                self.win_multiplier = 36
                print('You win with a multiplier of 1 to 36')
                return self.win_multiplier
            else:
                self.win_multiplier = -1
                print('You lose')
                return self.win_multiplier

