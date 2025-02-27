import google.generativeai as genai

# Set up API key
genai.configure(api_key="AIzaSyCa58OTZTg7hpSPd1w9Gg3uk5WIzk88ap8")

# Specify a different model
model_name = "gemini-1.5-pro-latest"  # Change this to the desired model

# Load the model
model = genai.GenerativeModel(model_name)

# Generate a response
response = model.generate_content("Explain cloud computing.")

# Print output
print(response.text)
