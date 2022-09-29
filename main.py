#
#   PROJECT : Random Number Generation with Various Distributions
# 
#   FILENAME : main.py
# 
#   DESCRIPTION :
#       Generating random numbers from different probability distributions and
#       calculating their various statistics (means, variance, and standard deviation).
# 
#   FUNCTIONS :
#       standard_random_number_generation()
#       exponential_random_number_generation()
#       poisson_random_number_generation()
#       histogram()
#       mean()
#       variance()
#       stdev()
#       display_information()
#       main()
# 
#   NOTES :
#       Can't use terminal to display histograms. Need to use a plotting library.
# 
#   AUTHOR(S) : Noah Arcand Da Silva    START DATE : 2022.09.19 (YYYY.MM.DD)
#
#   CHANGES :
#       - Previously tried to implement a histogram through terminal outputs, but quickly ran 
#       into formatting issues.
# 
#   VERSION     DATE        WHO             DETAILS
#   0.0.1a      2022.09.19  Noah            Creation of project.
#   0.0.1b      2022.09.21  Noah            Proper implementation of histograms.
#


from numpy import random as r
import numpy as np
import matplotlib.pyplot as plt


# Setting the number of bins for histrogram.
NBINS = 20

# Setting a seed of 9 to generate random numbers.
# (Random numbers won't be random, because of the static seed).
r.seed(9)


def standard_random_number_generation(size):
    # Generating a list of random numbers.
    # Following the standard uniform distribution.
    return r.uniform(size=size)


def exponential_random_number_generation(size):
    scale = 9
    # Generating a list of random numbers.
    # Following the standard uniform distribution.
    return r.exponential(scale=scale, size=size)


def poisson_random_number_generation(size):
    lam = 9
    # Generating a list of random numbers.
    # Following the standard uniform distribution.
    return r.poisson(lam=lam, size=size)


def histogram(data, data_label, nbins=NBINS):
    # Create a histogram with the data provided.
    plt.clf()
    plt.style.use('ggplot')
    plt.hist(data, nbins, rwidth=0.85, color='cornflowerblue')
    plt.title(data_label)
    plt.xlabel('Generated Random Numbers')
    plt.ylabel('Occurence')
    plt.savefig('histograms/' + data_label + '.svg')


def mean(data):
    # Calculate the mean for the list of numbers.
    return np.mean(data)


def variance(data):
    # Calculate the variance for the list of numbers.
    return np.var(data)


def stdev(data):
    # Calculate the standard deviation for the list of numbers.
    return np.std(data)


def display_information(data, data_label):
    print(data_label + '\n\n')

    print('Histogram (See figure)' + '\n')
    histogram(data, data_label, NBINS)
    
    print('Mean' + '\n------------------')
    print(str(mean(data)) + '\n')

    print('Variance' + '\n' + '------------------')
    print(str(variance(data)) + '\n')

    print('Standard Deviation' + '\n' + '------------------')
    print(str(stdev(data)) + '\n\n')


def main():
    # Standard Uniform Distribution
    size = 10
    distribution_type = 'Standard Uniform'
    while size <=100000:
        data_label = distribution_type + ' Distribution (' + str(size) +' Random Numbers)'
        display_information(standard_random_number_generation(size), data_label)
        size *= 10

    # Exponential Distribution
    size = 10
    distribution_type = 'Exponential'
    while size <= 100000:
        data_label = distribution_type + ' Distribution (' + str(size) +' Random Numbers)'
        display_information(exponential_random_number_generation(size), data_label)
        size *= 10

    # Poisson Distribution
    size = 10
    distribution_type = 'Poisson'
    while size <= 100000:
        data_label = distribution_type + ' Distribution (' + str(size) +' Random Numbers)'
        display_information(poisson_random_number_generation(size), data_label)
        size *= 10


# Running our code.
if __name__ == "__main__":
    main()