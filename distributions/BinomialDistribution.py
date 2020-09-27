import math
import matplotlib.pyplot as plt
from .GeneralDistribution import Distribution

class Binomial(Distribution):
    """ Binomial distribution class for calculating and
    visualizing a Binomial distribution.

    Attributes:
        mean (float): representing the mean value of the distribution
        standard_deviation (float): representing the standard deviation of the distribution
        data (list of floats): a list of floats extracted from the data file
        probability (float): representing the probability of an event occurring
        n (int): number of trials
    """


    def __init__(self, probability=.5, size=20):

        self.n = size
        self.probability = probability

        Distribution.__init__(self, self.calculate_mean(), self.calculate_stdev())


    def calculate_mean(self):
        """ Function to calculate the mean from probability and n

        Args:
            None

        Returns:
            float: mean of the data set
        """

        self.mean = self.probability * self.n

        return self.mean


    def calculate_stdev(self):
        """ Function to calculate the standard deviation from probability and n

        Args:
            None

        Returns:
            float: standard deviation of the data set
        """

        self.standard_deviation = math.sqrt(self.n * self.probability * (1 - self.probability))

        return self.probability


    def replace_stats_with_file_data(self):
        """ Function to replace stats data regarding file data

        Args:
            None

        Returns:
            float: the probability value
            float: the n value
        """

        self.n = len(self.data)
        self.probability = sum(self.data) / len(self.data)
        self.mean = self.calculate_mean()
        self.standard_deviation = self.calculate_stdev()


    def plot_bar(self):
        """ Function to output a histogram of the instance
        variable data using matplotlib pyplot library

        Args:
            None
        
        Returns:
            None
        """

        plt.bar(x = ['0', '1'], height = [(1 - self.probability) * self.n, self.probability * self.n])
        plt.title('Bar Chart of Data')
        plt.xlabel('outcome')
        plt.ylabel('count')


    def pdf(self, k):
        """ Probability density function calculator
        for the gaussian distribution.
        
        Args:
            x (float): point for calculating the probability density function
            
        Returns:
            float: probability density function output
        """
        
        a = math.factorial(self.n) / (math.factorial(k) * (math.factorial(self.n - k)))
        b = (self.probability ** k) * (1 - self.probability) ** (self.n - k)
        
        return a * b


    def plot_bar_pdf(self):
        """ Function to plot the pdf of the binomial distribution
        
        Args:
            None
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
        
        x = []
        y = []
        
        # calculate the x values to visualize
        for i in range(self.n + 1):
            x.append(i)
            y.append(self.pdf(i))

        # make the plots
        plt.bar(x, y)
        plt.title('Distribution of Outcomes')
        plt.ylabel('Probability')
        plt.xlabel('Outcome')

        plt.show()


    def calculate_probability_density(self, k):
        """ Function to output a histogram of the instance variable data
        using matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """
                
        plt.bar(
            x = ['0', '1'],
            height = [(1 - self.probability) *self.n, self.probability * self.n]
            )
        plt.title('Bar Chart of Data')
        plt.xlabel('outcome')
        plt.ylabel('count')


    def __add__(self, other):
        """ Function to add together two Binomial distributions with equal
        probability

        Args:
            other (Binomial): Binomial instance

        Returns:
            Binomial: Binomial distribution
        """

        try:
            assert self.probability == other.probability, 'probability values are not equal'
        except AssertionError as error:
            raise

        result = Binomial()
        result.n = self.n + other.n
        result.probability = self.probability
        result.calculate_mean()
        result.calculate_stdev()

        return result
        
    
    def __repr__(self):
        """ Function to output the characteristics of the Binomial instance

        Args:
            None
        
        Returns:
            string: characteristics of the Gaussian data
        """

        return "mean: {}, standard deviation: {}, probability: {}, n: {}".\
            format(self.mean, self.standard_deviation, self.probability, self.n)