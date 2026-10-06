import pandas as pd

# Read the JSON file
df = pd.read_json(r"C:\Users\sohan\Desktop\collage\assiment3-ds\movie_sugestion.json")

print(df)

print("\nMovie with higest rating:")

top_movie = df.loc[df["rating"].idxmax()]

print("Title :", top_movie["title"])
print("Rating:", top_movie["rating"])
print("Price:",top_movie["ticket_price"])