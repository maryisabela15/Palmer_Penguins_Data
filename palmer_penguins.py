# Load packages
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("penguins_size.csv")

# Viewing the dataset
head_df = df.head() # this line show the firts 5 rows of the dataset
print(head_df)

info_df = df.info() # this line show info about the data and data type

desc_df = df.describe(include="all") # this line show some basic statistics of the dataset
print(desc_df)

shape_df = df.shape # this line show the shape of the dataset
print(shape_df)

# Data analysis and visualization
###################################################################
# 1) We want to know how many penguins are per species and make a plot

count_species = df["species"].value_counts() # this line count the number of pebguin species in the dataset
print(count_species)

sns.set_theme(style="darkgrid")
sns.displot(df, x = "species", binwidth=3)
plt.ylabel("Number of penguins")
plt.xlabel("Species")
plt.title("Palmer Penguins Species")
plt.show()
plt.clf()

# 2) Relationship between the body mass and the flipper length per species
sns.scatterplot(x = df["body_mass_g"], y = df["flipper_length_mm"], hue = df["species"], palette = "mako")
plt.ylabel("Flipper length (mm)")
plt.xlabel("Body mass (g)")
plt.title("Relationship between Body mass and Flipper length per Species")
plt.show()
plt.clf()

# 3) Relationship between the culmen length and the flipper length per island
sns.scatterplot(x = df["culmen_length_mm"], y = df["flipper_length_mm"], hue = df["island"], palette = "rocket")
plt.ylabel("Flipper length (mm)")
plt.xlabel("Body mass (g)")
plt.title("Relationship between Body mass and Flipper length per Islands")
plt.show()
plt.clf()

# 4) Relationship betwwen flipper length and species
sns.violinplot(x = df["species"], y = df["flipper_length_mm"], palette = "Set2")
plt.ylabel("Flipper length (mm)")
plt.xlabel("Species")
plt.title("Flipper length per Species")
plt.show()
plt.clf()

# 5) Relationship between culmen depth and sex/species
sns.boxplot(x = df["species"], y = df["culmen_depth_mm"], width=0.5,fliersize=5, hue = df["sex"])
plt.ylabel("Species")
plt.xlabel("Culmen depth (mm)")
plt.title("Culmen depth per Species/Sex")
plt.show()





