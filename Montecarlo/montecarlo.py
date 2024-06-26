import random
import pandas as pd
import numpy as np

class Die:
    def __init__(self, sides,weights):
        
        sides = np.array(sides)
    #Internally initializes the weights to  1.0 for each face
        self.weights = weights if weights else[1.0]* sides
        
    #Takes a NumPy array of faces as an argument. Throws a TypeError if not a NumPy array
        if not isinstance(sides,np.ndarray):
            TypeError("Not a NumPy array")
            
        if len(sides)!=len(np.unique(sides)):
            ValueError("Array value not distinct")
            
    #Saves both faces and weights in a private data frame with faces in the index
        self.dice_df = pd.DataFrame({'weights':1.0},index=sides)
        
        
    def sides(self):
        return self.dice_df.index.values
    
    def weights(self):
        return self.dice_df['weights'].values
    
    def weights_change(self,side,new_weight):
       
    #Checks to see if the face passed is valid value, i.e. if it is in the die array. If not, raises an IndexError
        if side not in list(self.dice_df['sides']):
            IndexError(f"Side '{side}' is not valid")
        else:
            self.dice_df.loc[self.dice_df['sides']== side,'weights']=new_weight
        
    def roll(self,nrolls=1):
        
        result=[]
     #Takes a parameter of how many times the die is to be rolled; defaults to  1
    
        for I in range(nrolls):
            result=random.choices(self.sides,weights=self.weights)[0]
            result.append(result)
        
    def state(self):
#Returns a copy of the private die data frame
        return self.dice_df.copy()
        
        
  
class Game:
    def __init__(self,die):
        
      self.results = pd.DataFrame()  
      self.die = die 
        
#Takes an integer parameter to specify how many times the dice should be rolled
    def play(self, nrolls):
        
        self.results = pd.DataFrame()
        
        for i in range(len(self.die)):
            result_= pd.DataFrame(self.die[i].roll(nrolls))
            result_.index = [n+1 for n in range(nrolls)]
            result_.index.name = "Roll Data"                
            result_.columns=[i+1]
            result_.columns.name=" Die Number"
            self.results = pd.concat([self.results,result_],axis=1)

    def show_results(self, format='wide'):
        
        if format == 'wide':
            return self.results.copy()
        elif format == 'narrow':
            return self.results.stack().reset_index(level=1, drop=True).rename('Outcome')
        #This method should raise a ValueError if the user passes an invalid option for narrow or wide
        else:
            raise ValueError("Invalid format. Choose 'wide' or 'narrow'.")
        
        
class Analyzer:
    def __init__(self, game):
   #Takes a game object as its input parameter. Throw a ValueError if the passed value is not a Game object   
        if not isinstance(game, Game):
            raise ValueError("Input must be a Game object.")
        
        self.game = game
        self.results = game.show_results()
        
 #Computes how many times the game resulted in a jackpot.
    def jackpot(self):
        n_jackpots = (self.results == self.results.iloc[:, 0]).all(axis=1).sum()
#Returns an integer for the number of jackpots
        return n_jackpots

    def counts_per_roll(self):
  #Computes how many times a given face is rolled in each event      
        side_count = self.results.apply(pd.Series.value_counts)
        return side_count

    def combo_count(self):
    #Computes the distinct combinations of faces rolled, along with their counts    
        combinations = self.results.apply(tuple, axis=1)
        
        counts = pd.Series(combinations).value_counts().reset_index()
        
        counts.columns = ['Combination', 'Count']
        
        return counts

    def permutations(self):
     #Computes the distinct permutations of faces rolled, along with their counts   
        permutations = {}
        
        for I, row in self.results.iterrows():
            perm = tuple(sorted(row))
            if perm in permutations:
                permutations[perm] += 1
            else:
                permutations[perm] = 1
        permutations_counts = pd.DataFrame(permutations.items(), columns=['Permutation', 'Count'])
        
        return permutations_counts
