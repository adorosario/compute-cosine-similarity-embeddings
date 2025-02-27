import numpy as np
from openai import OpenAI

def get_embedding(text, model="text-embedding-3-small"):  # Using text-embedding-3-small by default
    """Get the embedding vector for a text string."""
    client = OpenAI()
    response = client.embeddings.create(
        input=text,
        model=model
    )
    return response.data[0].embedding

def cosine_similarity(v1, v2):
    """Compute the cosine similarity between two vectors."""
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    return dot_product / (norm_v1 * norm_v2)

def text_similarity(text1, text2, model="text-embedding-3-small"):  # Using text-embedding-3-small by default
    """Compute the cosine similarity between two text strings based on their embeddings."""
    embedding1 = get_embedding(text1, model)
    embedding2 = get_embedding(text2, model)
    return cosine_similarity(embedding1, embedding2)

# Command line usage
if __name__ == "__main__":
    import argparse
    
    # Set up command line argument parser
    parser = argparse.ArgumentParser(description='Compute cosine similarity between two text strings')
    parser.add_argument('string_a', type=str, help='First text string')
    parser.add_argument('string_b', type=str, help='Second text string')
    # Model is hardcoded to text-embedding-3-small as requested
    parser.add_argument('--model', type=str, default='text-embedding-3-small',
                        help='OpenAI embedding model to use (fixed to text-embedding-3-small)')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Calculate similarity using text-embedding-3-small model
    similarity = text_similarity(args.string_a, args.string_b, model="text-embedding-3-small")
    
    # Print result
    print(f"String A: \"{args.string_a}\"")
    print(f"String B: \"{args.string_b}\"")
    print(f"Similarity: {similarity:.4f}")
