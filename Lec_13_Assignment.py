import pandas as pd

import matplotlib.pyplot as plt


dataframe = pd.read_csv("IMDB-Movie-Data.csv")


""""" (Q1)  makes a dataframe from the imported IMDB csv file

Args:

        dataframe = dataframe from the imported IMDB csv file"""



print(len(dataframe))

""""" Q(2)  prints the number of rows in the imported IMDB csv file

Args:

        dataframe: dataframe from imported IMDB csv file"""




print(dataframe)
""""" Q(3)  prints out the dataframe columns

Args:
        dataframe: dataframe from imported IMBD csv file"""




dataframe_sort = dataframe.sort_values(["Revenue (Millions)"], ascending=False)
print(dataframe_sort.iloc[0]["Title"])

""""" Q(4)  makes a dataframe sorted by revenue grossed in descending order and prints the name of the highest grossing movie

Args:

        dataframe_sort: dataframe sorted for by revenue grossed in descending order
        Revenue (Millions): revenue of each movie in miilions of dollars"""




plt.scatter(dataframe.Metascore, dataframe["Revenue (Millions)"])
plt.savefig('scatter_assignment_Lec_13.png')

""""" Q(5)  makes a scatter plot of movies according to Metascore rating vs. revenue grossed

Args:

        Revenue (Millions): revenue of each movie in miilions of dollars
        Metascore: Metascore rating of each movie"""




dataframe_sort_Metascore = dataframe.sort_values(["Metascore"])
plt.bar(dataframe_sort_Metascore['Title'].head(20), dataframe_sort_Metascore['Revenue (Millions)'].head(20))
plt.xlabel('Movie Title')
plt.xticks(rotation='45')
print(dataframe_sort_Metascore)
plt.savefig('bar_graph_assignment_Lec_13.png')

""""" Q(6)  makes a dataframe composed of top 20 rated movies by Metascore and makes a bar plot with each movie with its associated revenue

Args:

        dataframe_sort_Metascore: dataframe sorted for top 20 movies according to Metascore rating
        Title: tile of the movie
        Revenue (Millions): revenue of each movie in miilions of dollars
        Metascore: Metascore rating of each movie"""




dataframe_sub_Ridley_Scott = dataframe[dataframe.Director == "Ridley Scott"]
print(len(dataframe_sub_Ridley_Scott))
print(dataframe_sub_Ridley_Scott[["Metascore"]].mean(axis=1))

""""" Q(7)  makes a dataframe of movies directed by Ridley Scott

Args:

        dataframe_sub_Ridley_Scott: dataframe sorted for movies directed by Ridley Scott
        Metascore: Metascore rating of each movie"""




dataframe_high_rev_high_score = dataframe[(dataframe["Revenue (Millions)"] > 500) & (dataframe["Metascore"] > 90)]
print(dataframe_high_rev_high_score)
dataframe_high_rev_high_score.to_csv("top_movies.csv", index=False)

""""" Q(8)  makes a dataframe composed of movies grossing in excess of 500 million$ that also have a Metascore rating greater than 90

Args:

        dataframe_high_rev_high_score: dataframe sorted for movies with revenue > 500 million$
        Revenue (Millions): revenue of each movie in miilions of dollars
        Metascore: Metascore rating of each movie"""