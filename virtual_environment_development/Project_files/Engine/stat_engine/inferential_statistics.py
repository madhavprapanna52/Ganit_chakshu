"""
Inferential statistics unit 
    >  Made for making strong observational based and probability 
    modeling based results to inhance data understanding veiw and exposure

Feauring 
    1. Auto model sellection unit  | observation based model sellection for modeling  
    2. Model fiting unit | making model fit evaluations and finalising modeling 
    3. Model_application units 
    4. Probability tools  | prediction tools and formulas based tools 

Procedure 
    - probability kernel - Handeling dataset based senarios and computing probability 
    - simple flaging mechanism - continuous and discreet dataset
"""
from basic_tool import*

data_set = load_csv('synthetic_data.csv')
#data_handle = Data_handle(data_set)

# Probability Handler object 
class Probability_init:
    """
    Making probability kernel thing which initialises the 
    probability instances for the lists and dataset we are presenting 
    
    Initialising probability procedure  
        Data types based computations 
        - Categorical and binomials | Discreet dataset flaged
            } Computing frequency based on data context 
        - Numerical / continuous dataset 
            } bins distribution based on dataset context division
    """

    # Probability data handle object | Flagging system 

    def __init__(self, data_set_list):
        self.data_list = Data_handle(data_set_list)
        #todo Make this adaptable and upgrade interface for good integrations 

    def Discreet_prob_ini(self,which_to_return):
        '''
        Making initialisation of probability infrences for discreet dataset
        data_set - Partitions based frequency computations | total frequency on the dataset based on total experiment 

        Data with instances and total experimental divisions wont need automated division - Simplicity feature

        ~ Label dependent structure 
        output : Frequency list [ [type_1:freq, type_2:freq] ]
        '''
        # Lists of binary data and categorical dataset 
        binary_dataset = self.data_list.row('b') 
        categorical_dataset = self.data_list.row('c')
        
        # All list would have their partitions based frequency 
        binary_data_freq = []
        categorical_freq = []

        # Iterations for frequency counting 
        for binary_elements in binary_dataset:
            partitioned_list  = partition_list(binary_elements)
            freq_dict_list = freq_list(partitioned_list)  # list of dictionaries 
            binary_data_freq.append(freq_dict_list)

        for categorical_unit in categorical_dataset:
            partitioned_cat = partition_list(categorical_unit)
            freq_dict_list = freq_list(partitioned_cat)
            categorical_freq.append(freq_dict_list)

        # Which you want - From dataset 
        if which_to_return == 'c':
            return categorical_freq
        elif which_to_return == 'b':
            return binary_data_freq
        else:
            return [categorical_freq,binary_data_freq] # Probability initialised for discreet dataset
    
    def Continuous_probability_initialisation(self):
        '''
        Theoritical continuous probability modeling 
        partitions based frequency divided by total partitions
         would result in probability of the bin thus 
         modeling continous dataset 
        '''
        continuous_dataset = self.data_list.row('n')  # Numerical dataset 
        cont_probability_model = []
        partition_bin_list = number_partition()
        for cont_elems in continuous_dataset:
            int_l = int_convert(cont_elems) # integers numbers
            # Dictionary list | bins frequency output 
            freq_dict = {}
            for bins in partition_bin_list:
                freq_dict[str(bins)] = bin_frequency(bins, int_l)/10  # probability initialised
            cont_probability_model.append(freq_dict)  # containning the frequencies dict
        return cont_probability_model

#TODO Need probability Modeling engines and fitting algorithm mvp
