from sentence_transformers import SentenceTransformer, CrossEncoder

# Sentences we want sentence embeddings for
sentences = ['Detta är en exempelmening', 'Det är bra väder idag']

model = SentenceTransformer('intfloat/multilingual-e5-small')
query_instruction = "Represent the query for retrieval: "

text_embeddings = model.encode(sentences=sentences, normalize_embeddings=True, convert_to_tensor=True)
if len(text_embeddings) > 0:
    print("Sentence embeddings has been computed successfully, the model is working!")
else:
    raise Exception("No embeddings returned") 

# We can now dump the model on disk
model.save("./embedder_model_files")

question = "Hur är vädret?"
model = CrossEncoder("intfloat/multilingual-e5-base")
inputs = [[question, sentence] for sentence in sentences]
out = model.predict(inputs)
print("Cross encoder is working!")

model.save("./cross_encoder_model_files")