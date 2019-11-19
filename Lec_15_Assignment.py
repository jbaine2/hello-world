import numpy as np

import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt



mpg = sns.load_dataset("mpg")



# problem 1


sns.distplot(mpg["mpg"])
plt.savefig("01.png")

"""makes a distribution chart of the dataset mpg
Args:

        mpg: mpg dataset
"""

# problem 2

sns.catplot(x="model_year", y="mpg", kind="box", data=mpg)
plt.savefig("02.png")

""" makes a categorical box plot comparing the model year and the mpg from the dataset mpg
Args:

        mpg: mpg dataset
        model_year: model year of corresponding car
        "mpg": fuel efficiency of corresponding car in miles per gallon 
        
        """

# problem 3


sns.relplot(x="horsepower", y="weight", hue="cylinders", col="model_year", col_wrap=6, data=mpg)
plt.savefig("03.png")

""" makes relational plots comparing horsepower, weight, and the number of cylinders according to each year
Args:

        mpg: mpg dataset
        horsepower: horsepower of corresponding car
        weight: weight corresponding car in miles per gallon 
        cylinders: number of cylinders in car engine for corresponding car
        model_year: model year for corresponding car

        """

# problem 4

# generate a pair plot with a hue of car origin only use columns mpg, cylinders and weight
sns.pairplot(mpg, hue="origin", vars=["mpg", "cylinders", "weight"])
plt.savefig("04.png")

""" makes a pair plot comparing car origin, mpg, number of cylinders, and weight
Args:

        mpg: mpg dataset
        origin: country that produced the car
        "mpg": fuel efficiency of corresponding car in miles per gallon
        cylinders: number of cylinders in car engine for corresonding car
        weight: weight of the corresponding car 

        """




# problem 5


sns.catplot(x="cylinders", y="mpg", hue="origin", kind="violin", data=mpg)
plt.savefig("05.png")






# problem 6

sns.relplot(x="horsepower", y="mpg", hue="origin", size="weight", sizes=(40, 400), data=mpg)
plt.savefig("06.png")



# problem 6 (7)


df_US_cars = mpg[mpg.origin == "usa"]
sns.catplot(x="model_year", y="horsepower", hue="cylinders", kind="swarm", data=df_US_cars)
plt.savefig("07.png")