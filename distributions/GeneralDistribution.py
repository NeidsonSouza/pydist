class Distribution:
    """ Generic distribution class for calculating and visualizing a 
    probability distribution.

    Attributes:
        mean (float): mean value of the distribution
        standard_deviation (float): standard_deviation of the distribution
        data_list (list of floats): a list of floats extracted from the
        data file.
    """


    def __init__(self, mean, standard_deviation):

        self.mean = mean
        self.standard_deviation = standard_deviation
        self.data_list = []
    

    def read_data_file(self, file_name):
        """ Function to read in data from a txt file. The txt file shoud have
        one number (zero or one) per line. The numbers are stored in the
        'data_list' atrribute.

        Args:
            file_name (string): name of a file to read from

        Returns:
            None
        """

        with open(file_name) as file:
            file_data = []
            line = file.readline()

            while line:
                file_data.append(float(line))
                line = file.readline()
            
        file.close()

        if not has_only_zeros_and_ones(file_data):
            raise ValueError('each item in txt file should be zero or one')

        self.data_list = ['%.1f' % item for item in file_data]
    

    @staticmethod
    def has_list_only_zeros_and_ones(any_list):
        """ Function to check if each item of a list is zero or one """

        list_result = [item == 0 or item == 1 for item in any_list]
        return all(list_result)