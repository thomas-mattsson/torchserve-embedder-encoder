from sentence_transformers import SentenceTransformer, CrossEncoder

# Sentences we want sentence embeddings for
sentences = ['This is an example sentence', 'Each sentence is converted']

model = SentenceTransformer('intfloat/multilingual-e5-small')
query_instruction = "Represent the query for retrieval: "

text_embeddings = model.encode(sentences=sentences, normalize_embeddings=True, convert_to_tensor=True)
if len(text_embeddings) > 0:
    print("Sentence embeddings has been computed successfully, the model is working!")
else:
    raise Exception("No embeddings returned") 

# We can now dump the model on disk
model.save("./embedder_model_files")

question = "how are you doing?"
model = CrossEncoder("jeffwan/mmarco-mMiniLMv2-L12-H384-v1")
inputs = [[question, sentence] for sentence in sentences]
out = model.predict(inputs)
print("Cross encoder is working!")

model.save("./cross_encoder_model_files")