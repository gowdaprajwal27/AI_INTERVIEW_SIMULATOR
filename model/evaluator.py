from sentence_transformers import SentenceTransformer, util

model = None

def get_model():
    global model
    if model is None:
        model = SentenceTransformer('all-MiniLM-L6-v2')
    return model

def evaluate_answer(user_answer, expected_answer):
    model = get_model()

    # ✅ Create embeddings
    embeddings1 = model.encode(user_answer, convert_to_tensor=True)
    embeddings2 = model.encode(expected_answer, convert_to_tensor=True)

    # ✅ Compute similarity
    similarity = util.pytorch_cos_sim(embeddings1, embeddings2)

    score = float(similarity[0][0]) * 100

    if score > 75:
        feedback = "Excellent answer!"
    elif score > 50:
        feedback = "Good but can be improved."
    else:
        feedback = "Needs improvement."

    return score, feedback