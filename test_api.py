from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")
result = generator("Hello, how are you?", max_length=30, num_return_sequences=1)
print(result)
