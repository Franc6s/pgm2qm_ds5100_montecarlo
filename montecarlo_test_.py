import unittest
import pandas as pd

from Montecarlo.montecarlo import Die
from Montecarlo.montecarlo import Game
from Montecarlo.montecarlo import Analyzer

class MontecarloTestCase(unittest.TestCase):
    
    def weights_change_test(self):
        """
        Tests if the weight change function works correctly
        """
        die = Die([1,2,3,4,5,6])
        die.weights_change(2,3.0)
        expected = 3
        actual = die.state().loc[die.state()['sides']==2,'weights'].values[0]
        self.assertEqual(expected,actual)
    
    def roll_test(self):
        """
        Tests the roll function
        """
        die =Die([1,2,3,4,5,6])
        expected = 5
        actual=len(die.roll(5))
        self.assertIn(expected,actual)
        
    def state_test(self):
        """
        Test the state function to show the die's current state
        """
        die =Die([1,2,3,4,5,6])
        expected_df = pd.DataFrame({'sides':[1,2,3,4,5,6],'weights':[1.0,1.0,1.0,1.0,1.0,1.0]})
        actual_df = die.state()
        pd.testing.assert_frame_equal(expected_df,actual_df)
        
    def play_test(self):
        """
        Test the play function of the Game class
        """
        game_play=Game([Die([1,2,3,4]),Die([1,2,3,4]),Die([1,2,3,4])])
        game_play.play(50)
        expected = 50
        actual = game_play.show_results().shape[0]
        self.assertEqual(expected,actual)
        expected_col = 3
        actual_col = len(game_play.show_results())
        self.assertEqual(expected_col,actual_col)
    
    def show_results_test(self):
        """
        Test the show result function
        """
        game_play=Game([Die([1,2,3,4]),Die([1,2,3,4]),Die([1,2,3,4])])
        game_play.play(50)
        expected = 50
        actual = game_play.show_results(form='wide').shape[0]
        self.assertEqual(expected,actual)
        expected_col = 4
        actual_col = len(game_play.show_results(form='wide'))
        self.assertEqual(expected_col,actual_col)
        
    def jackpot_test(self):
        """
        Test the jackpot function
        """
        game_play=Game([Die([1,2,3,4]),Die([1,2,3,4]),Die([1,2,3,4])])
        game_play.play(50)
        analyzer = Analyzer(game_play)
        jackpot = analyzer.jackpot()
        jackpot_df = analyzer.jackpot_df.shape[0]
        self.assertEqual(jackpot,jackpot_df)
    
    def count_per_roll_test(self):
        """
        Test the count per roll function
        """
        game_play=Game([Die([1,2,3,4]),Die([1,2,3,4]),Die([1,2,3,4])])
        game_play.play(50)
        analyzer = Analyzer(game_play)
        counts_df = analyzer.count_per_roll()
        expected_col = 4
        actual_col = counts_df.shape[1]
        self.assertEqual(expected_col,actual_col)
        expected_rw=50
        actual_rw=counts_df.shape[0]
        self.assertEqual(expected_rw,actual_rw)

    def combo_count_test(self):
        """
        Test the combination count function
        """
        game_play=Game([Die([1,2,3,4]),Die([1,2,3,4]),Die([1,2,3,4])])
        game_play.play(50)
        analyzer = Analyzer(game_play) 
        combo_df=analyzer.combo_count()
        expected_col = 1
        actual_col = combo_df.shape[1]
        self.assertEqual(expected_col,actual_col)
        expected_index = 4
        actual_index = len(combo_df.index.names)
        self.assertEqual(expected_index,actual_index)
        
    def permutations_test(self):
        """
        Test the permutation calculation function
        """ 
        game_play=Game([Die([1,2,3,4]),Die([1,2,3,4]),Die([1,2,3,4])])
        game_play.play(50)
        analyzer = Analyzer(game_play) 
        permutations_df = analyzer.combo_count(permutations=True)
        expected_col = 1
        actual_col = permutations_df.shape[1]
        self.assertEqual(expected_col,actual_col)
        expected_index = 4
        actual_index = len(permutations_df.index.names)
        self.assertEqual(expected_index,actual_index)

if __name__ == '__main__':
    unittest.main(verbosity=3)