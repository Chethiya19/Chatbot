from transformers import pipeline

# Load small GPT-2 model for speed
chatbot_pipeline = pipeline("text-generation", model="gpt2")

def get_chatbot_response(user_input):
    # Generate text
    result = chatbot_pipeline(user_input, max_length=50, num_return_sequences=1)
    return result[0]['generated_text']
