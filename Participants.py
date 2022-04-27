
class CockTailWaitress:
    def __init__(self):
        self.name = ''
        self.total_tip = 0
                
    def check_drink_eligibility(self, player_duration, player_pot):
        if player_duration > 4 or player_pot > 200:
            print("Hey would you like you a drink")
            return True
        else:
            print("Hey if you play little more you'll get free drinks!!")
            return False

    def add_tip(self, tip_amount):
        self.total_tip += tip_amount
        return self.total_tip

    def get_total_tips(self):
        return self.total_tip