import faiss
import numpy as np

def build_index(embeddings: list[list[float]]):
    array = np.array(embeddings)
    dim = array.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(array)
    return index, array

def searchIndex(index, query_embedding, k=3):
    D, I = index.search(query_embedding, k)
    return I.tolist()[0]
