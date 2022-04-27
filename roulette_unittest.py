import unittest as u

#classes to be tested
from PythonRoulette import roulette 
from BettingSystem import RouletteBetting
from Player import RoulettePlayer 
from Participants import CockTailWaitress


        
        
class TestRouletteWheel(u.TestCase):
    def test_recordColorHistory_Red(self):
        test_wheel = roulette()
        test_wheel.rollNumber = 7 #should be red
        self.assertEqual(test_wheel.recordColorHistory(), 'Red')
    
    def test_recordColorHistory_Black(self):
        test_wheel = roulette()
        test_wheel.rollNumber = 10 #should be red
        self.assertEqual(test_wheel.recordColorHistory(), 'Black')

    def test_recordColorHistory_Green(self):
        test_wheel = roulette()
        test_wheel.rollNumber = 0 #should be red
        self.assertEqual(test_wheel.recordColorHistory(), 'Green')

    def test_determineIfOddOrEven_odd(self):
        test_wheel = roulette()
        test_wheel.rollNumber = 9
        self.assertEqual(test_wheel.determineIfOddOrEven(), 'Odd')

    def test_determineIfOddOrEven_even(self):
        test_wheel = roulette()
        test_wheel.rollNumber= 16
        self.assertEqual(test_wheel.determineIfOddOrEven(), 'Even')
    
    def test_determineIfOddOrEven_zero(self):
        test_wheel = roulette()
        test_wheel.rollNumber= 0
        self.assertFalse(test_wheel.determineIfOddOrEven())
        
    def test_rollTheRouletteWheel(self):
        test_wheel = roulette()
        self.assertLess(test_wheel.rollTheRouletteWheel(), 37) #it should always generate number lower than 37


class TestWaitress(u.TestCase):
    def test_get_total_tips(self):
        test_waiter = CockTailWaitress()
        test_waiter.total_tip = 60
        self.assertEqual(test_waiter.get_total_tips(), 60)

    def test_add_tip(self):
        test_waiter = CockTailWaitress()
        test_waiter.total_tip = 30
        self.assertEqual(test_waiter.add_tip(40), 70)

    def test_check_drink_duration(self):
        test_waiter = CockTailWaitress()
        self.assertTrue(test_waiter.check_drink_eligibility(6, 0)) # players with more than 4 mins should get drinks
        
    def test_check_drink_high_rollers(self):
        test_waiter = CockTailWaitress()
        self.assertTrue(test_waiter.check_drink_eligibility(0, 500)) # players with lot of money should get drinks

class TestBetting(u.TestCase):
    def test_get_bet_type(self):
        test_bet = RouletteBetting()
        test_bet.bet_chosen = 'Odd'
        self.assertEqual(test_bet.get_bet_type(), 'Odd')

    def test_check_results_bet_color_loss(self):
        test_bet = RouletteBetting()
        test_bet.bet_chosen = 'Red'
        self.assertEqual(test_bet.check_results_bet('Black', 'Even', 31), -1)

    def test_check_results_bet_color_win(self):
        test_bet = RouletteBetting()
        test_bet.bet_chosen = 'Red'
        self.assertEqual(test_bet.check_results_bet('Red', 'Even', 31), 1)

    def test_check_results_bet_odeven_loss(self):
        test_bet = RouletteBetting()
        test_bet.bet_chosen = 'Odd'
        self.assertEqual(test_bet.check_results_bet('Red', 'Even', 31), -1)

    def test_check_results_bet_odeven_win(self):
        test_bet = RouletteBetting()
        test_bet.bet_chosen = 'Even'
        self.assertEqual(test_bet.check_results_bet('Red', 'Even', 31), 1)

    def test_check_results_bet_number_win(self):
        test_bet = RouletteBetting()
        test_bet.bet_chosen = '31'
        self.assertEqual(test_bet.check_results_bet('Red', 'Even', 31), 36)

    def test_check_results_bet_number_loss(self):
        test_bet = RouletteBetting()
        test_bet.bet_chosen = '35'
        self.assertEqual(test_bet.check_results_bet('Red', 'Even', 31), -1)


class TestPlayer(u.TestCase):
    def test_player_pot(self):
        test_player = RoulettePlayer()
        test_player.pot = 560
        self.assertEqual(test_player.get_pot(), 560)
    
    def test_updating_pot_wins(self):
        test_player = RoulettePlayer()
        test_player.pot = 560
        test_player.update_pot(500)
        self.assertEqual(test_player.pot, 1060) #proper adding
        
    def test_updating_pot_losses(self):
        test_player = RoulettePlayer()
        test_player.pot = 560
        test_player.update_pot(-500)
        self.assertEqual(test_player.pot, 60) #proper adding negatives
        
    def test_give_tip(self):
        test_player = RoulettePlayer()
        test_player.pot = 560
        self.assertTrue(test_player.give_tip(50))

    def test_give_tip_insufficient_funds(self):
        test_player = RoulettePlayer()
        test_player.pot = 560
        self.assertFalse(test_player.give_tip(5000))

    def test_get_game_duration(self):
        test_player = RoulettePlayer()
        test_player.game_duration = 16
        self.assertEqual(test_player.get_game_duration(), 16)

    def test_leave_table(self):
        test_player = RoulettePlayer()
        self.assertFalse(test_player.leave_table())


#integration testing
#player vs waiter
class TestPlayerWaiter(u.TestCase):
    def test_check_drinks(self):
        test_player = RoulettePlayer()
        test_player.pot = 5000
        test_player.game_duration = 3
        test_waiter = CockTailWaitress()
        self.assertTrue(test_waiter.check_drink_eligibility(test_player.get_game_duration(), test_player.get_pot()))

    def test_player_tipping(self):
        test_player = RoulettePlayer()
        test_player.pot = 5000
        test_waiter = CockTailWaitress()
        test_tip = 100
        self.assertTrue(test_player.give_tip(100))
        test_waiter.add_tip(100)
        self.assertEqual(test_waiter.get_total_tips(), 100)

#betting vs roulette wheel
class TestBettingRouletteResults(u.TestCase):
    def test_roulete_player_win(self):
        test_wheel = roulette()
        test_wheel.rollNumber = 29
        test_wheel.rollHistory = [29]
        test_wheel.colorHistory = ['Black']
        test_bet = RouletteBetting()
        test_bet.bet_chosen = 'Odd'
        color_result, odev_result, num_result = test_wheel.give_results()
        self.assertEqual(test_bet.check_results_bet(color_result, odev_result, num_result), 1) #winning multiplier

    def test_roulete_player_loss(self):
        test_wheel = roulette()
        test_wheel.rollNumber = 29
        test_wheel.rollHistory = [29]
        test_wheel.colorHistory = ['Black']
        test_bet = RouletteBetting()
        test_bet.bet_chosen = 'Even'
        color_result, odev_result, num_result = test_wheel.give_results()
        self.assertEqual(test_bet.check_results_bet(color_result, odev_result, num_result), -1) #losing multiplier

#player vs betting
class TestPlayerBetting(u.TestCase):
    def test_bet_player_updating_win(self):
        test_player = RoulettePlayer()
        test_player.bet = 100
        test_player.pot = 5000
        test_bet = RouletteBetting()
        test_bet.bet_chosen = 'Even'
        test_player.update_pot(test_bet.check_results_bet('Red', 'Even', 31) * test_player.bet)
        self.assertEqual(test_player.get_pot(), 5100)

    def test_bet_player_updating_loss(self):
        test_player = RoulettePlayer()
        test_player.bet = 100
        test_player.pot = 5000
        test_bet = RouletteBetting()
        test_bet.bet_chosen = 'Odd'
        test_player.update_pot(test_bet.check_results_bet('Red', 'Even', 31) * test_player.bet)
        self.assertEqual(test_player.get_pot(), 4900)


if __name__ == '__main__':
    u.main()    








#integration testing






