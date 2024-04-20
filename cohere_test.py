import cohere
import json

# Create a new Cohere client
co = cohere.Client("SNUTZQkRHFkybeGNay7bwNftreTkYPjsExGIpRWm")
# Open the JSON file
with open('articles.json', 'r', encoding='utf-8') as articles:
    # Load the JSON data
    data = json.load(articles)

# Initialize an empty dictionary to store the transformed data
transformed_data = {}

# Iterate through each item in the array and assign a unique key to each item
for i, item in enumerate(data):
    transformed_data[f"item_{i}"] = item



response = co.chat(
    documents=[data],
    message="Τι είναι το Data Jump;"
)
print(response)

