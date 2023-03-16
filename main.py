# in python create code to illustrate the central limit theorem using something similar to a Galton Board simulation
import random
import matplotlib.pyplot as plt
import matplotlib
import tkinter as tk
matplotlib.use('TkAgg')
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Define the number of bins and balls
    plt.interactive(False)

    num_bins = 30
    num_balls = 10000

    # Define the probabilities of the left and right branches
    p_left = 0.5
    p_right = 1 - p_left

    # Simulate the Galton Board
    results = []
    for i in range(num_balls):
        position = 0
        for j in range(num_bins):
            if random.random() < p_left:
                position -= 1
            else:
                position += 1
        results.append(position)

    # Plot the results
    plt.hist(results, bins=num_bins)
    plt.title("Galton Board Simulation")
    plt.xlabel("Bin")
    plt.ylabel("Frequency")
    plt.show()

    # Calculate the mean and standard deviation of the results
    mean = sum(results) / num_balls
    std_dev = (sum((x - mean) ** 2 for x in results) / num_balls) ** 0.5

    # Print the mean and standard deviation
    print("Mean: {}".format(mean))
    print("Standard Deviation: {}".format(std_dev))

# The code simulates a Galton Board with num_bins bins and num_balls balls. The probabilities of the left and right
# branches are p_left and p_right, respectively, and are set to 0.5 and 0.5 by default.
# After simulating the Galton Board, the code plots a histogram of the results using the matplotlib library.
# Finally, the code calculates the mean and standard deviation of the results and prints them to the console.
# The histogram should demonstrate the bell-shaped curve of the normal distribution, which is a manifestation of the
# Central Limit Theorem. The mean and standard deviation should also demonstrate the Central Limit Theorem, as they
# should approach the expected mean and standard deviation of the normal distribution as num_balls increases.