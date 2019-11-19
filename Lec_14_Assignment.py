
import pandas as pd

import matplotlib.pyplot as plt



df_imdb = pd.read_csv("IMDB-Movie-Data.csv")


# problem 1

df_director = df_imdb.groupby(["Director"], as_index=False).count()

# create new dataframe "df_director" that is a grouping of "Director" from df_imdb with calling

# count see example from class where I used mean instead





#problem 2

df_director_min = df_director[["Director", "Title"]]


# take df_director and create a new data frame df_director_min that contains only the "Director"

# and "Title" columns, in this case "Title" is actually the number of titles the director

# has made based on how we did the grouping earlier





#problem 3

df_director_min = df_director_min.sort_values(["Title"], ascending=False)
print(df_director_min)
# take df_director_min and sort by "Title" with the highest number first, save it back

# into df_director_min





#problem 4
df_director_min_first_30 = df_director_min[0:30]
plt.bar(df_director_min_first_30["Director"], df_director_min_first_30["Title"])
plt.xticks(rotation='45')
plt.savefig("directors_with_most_movies.png")
# take df_director_min and slice the first 30 rows and make a bar plot

# rotate the x-axis 45 degrees plt.xticks(rotation='45')

# save plot to "directors_with_most_movies.png"





# problem 5
df = pd.read_csv("animals.csv")
df_location = pd.read_csv("animals_location.csv")
df_sex = pd.read_csv("animals_sex.csv")
df_merge = df.merge(df_location)
df_animals_info = df_merge.merge(df_sex)
df_animals_info.to_csv("nanimals_info.csv", index=False)

# create a dataframe df, df_location, df_sex from csv files: "animals.csv",

# "animal_location.csv", "animal_sex.csv" respectively.

# merge df with df_location and include rows that are shared, i.e. no rows with NaN

# save as df_merge

# merge df_merge with df_sex keep rows regardless of if there is missing data

# save final df into csv file "animals_info.csv"





# problem 6
df_Q6 = pd.DataFrame(columns="col1,col2,col3".split(","))
df_Q6.loc[0] = ["A", 0, 1]
df_Q6.loc[1] = ["B", 1, 2]
df_Q6.loc[2] = ["C", 2, 3]
df_Q6.to_csv("Q6.csv")
# create a dataframe in the format of below

# col1 col2 col3

# A    0    1

# B    1    2

# C    2    3

# save it to a csv file