import pinecone
from colour_data import colour_data
from colour import Colour, plot_colours

# Replace this with your Pinecone API key
API_KEY = "<YOUR_PINECONE_API_KEY>"

new_index_name = "colour-index"

print("initialising Pinecone connection...")
pinecone.init(api_key=API_KEY, environment="us-west1-gcp-free")
print("Pinecone initialised")

print(f"Creating 3-dimensional index called '{new_index_name}'...")
pinecone.create_index(new_index_name, dimension=3)
print("Success")

print("Checking Pinecone for active indexes...")
active_indexes = pinecone.list_indexes()
print("Active indexes:")
print(active_indexes)

print(f"Getting description for '{new_index_name}'...")
index_description = pinecone.describe_index(new_index_name)
print("Description:")
print(index_description)

print(f"Getting '{new_index_name}' as object...")
pinecone_index = pinecone.Index(new_index_name)
print("Success")

print("Upserting vectors...")
upsert_response = pinecone_index.upsert(
    vectors=colour_data,
    namespace="colour-namespace"
)
print("Success")

# Function to search for similar colours
def find_similar_colours(query_colour, top_k=5):
    print(f"searching for similar colours to {query_colour.name} ({query_colour.as_hex()})")
    print(f"Vector to search: {query_colour.vector}")
    query = pinecone_index.query(
        queries=[
            query_colour.vector
            ],
        top_k=top_k,
        namespace='colour-namespace',
        include_values=True
        )
    
    return query.results[0].matches

# Use the search function
colours_to_test = [
    Colour('Light Coral', [240, 128, 128]),
    Colour(
        'Bisque',
        [
            1.0,
            0.8941176470588236,
            0.7686274509803922
        ],
        format = "normalised"
        ),
    Colour(
        'My new hex colour',
        "ae237f",
        format="hex"
        )
]

for colour_to_test in colours_to_test:
    similar_colours = find_similar_colours(colour_to_test)
    plot_colours(colour_to_test, similar_colours)
