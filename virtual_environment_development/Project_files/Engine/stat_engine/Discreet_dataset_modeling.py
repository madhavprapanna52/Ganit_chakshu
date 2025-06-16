'''
Discreet dataset modeling unit
Models discreet dataset into probability models - Fitting algorithms used for fitting the functions 

Functions 
    - Fiting and choosing best statisticaal model to fit into the dataset
    - returns modeled function of the dataset 
    - Discreet Generates report through modeling and gives interactives for knowing about datasets
'''
from basic_tool import *

#TODO discreet and continuous both are mapped as random variable based computations thus -- Map those concepts into action

class Discreet_functions_modeling:
    """
    Makes functions based output for the dataset through pluging formulas 
    interactives of the dataset through geting to know about it through functions of discreet modeling
    """
    def __init__(self, data_set):
        self.data_set = data_set  # Only load binary dataset list
        self.cli_mode = True
        self.x = 0
        self.p = 0

    # todo Binomial is made for binary for now - Upgrade expected

    def geometric_distribution(self):
        return (self.p * ((1-self.p)**(self.x - 1)))

    def binomial_distribution(self):
        """
        x ~ total success to compute probability of 
        Dataset is taken into account for computing probability of given success count in given trials
        Analysing the given data - Based thus computations would be based on the given number of trials
        """
        n = 100
        x = self.x
        if self.cli_mode:
            not_got_x = True
            while not_got_x:
                x = int(input('What number of success you want to compute probability :'))
                self.x = x
                if x == '':
                    not_got_x = True
                not_got_x = False

            self.cli_mode = False
            return self.binomial_distribution()

        Binomial_Expression = '(n_x)*(p^x)*(q^(n-x))'
        pa = partition_list(self.data_set)
        self.p = freq_list((pa),success_probability_want=True)[1]
        p = self.p
        q = (1 - p)
        final = (factorial_simplification(f'{n}_{x}')) * (p**x) * (q ** (n - x))
        return final

# testing unit
d = Discreet_functions_modeling(binary_d[0])
print(d.binomial_distribution())
print(d.geometric_distribution())
