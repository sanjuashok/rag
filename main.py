import constants
import openai
import numpy as np
import pandas as pd

from sklearn.metrics import DistanceMetric
print(DistanceMetric.__doc__)

openai.api_key = constants.OPENAI_API_KEY

# Read the file.
file_path = "data/tinystories-sample.txt"
with open(file_path, 'r') as file:
    lines_list = file.readlines()


# ye olde story holder
stories = []

token = ""
for line in lines_list:
    if line.strip() != '<|endoftext|>':
        token += line
    else:
        # add token to an array
        stories.append(token)
        # reset token
        token = ""


#  now we store the embeddings with a link to the story. 
np_embs = []

# below is the code to serialize the embeddings from openai. the list of embeddings is saved in np_embs.nyc. 
'''
for idx, story in enumerate(stories):
    # get the embedding for the story
    print(idx)
    response = openai.Embedding.create(
        input= story,
        model="text-embedding-ada-002"
    )
    embeddings = response['data'][0]['embedding']

    np_embs.append(np.array(embeddings))

embedding_data = {
    "stories" : stories,
    "embedding":  np_embs
}

np.save('np_embs.npy', np_embs)
'''

# load the embeddings from the serialized format
np_embs = np.load('np_embs.npy', allow_pickle=True)

# Since the loaded_array_list may contain Python objects, it is necessary to convert it to a regular Python list
#np_embs = np_embs.tolist()

# now we have a list of embeddings from the indexed data. Now let's do a quick test 
print("at sample query")
sample_query = "who was at the big lake?"
response = openai.Embedding.create(
        input= sample_query,
        model="text-embedding-ada-002"
    )

query_embedding = response['data'][0]['embedding']


distance_metric = 'euclidean'
dist = DistanceMetric.get_metric(distance_metric)
distances = dist.pairwise(np.vstack([query_embedding, np_embs]))[0, 1:]

k = 3  # The number of nearest neighbors you want to find

# Indices of the k-nearest neighbors (sorted by distance)
nearest_indices = np.argsort(distances)[:k]


for i in nearest_indices:
    print(stories[i] + '\n')


