import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch API URL and API Key from environment variables
api_url = os.getenv("GROQ_API_URL")  # Correct API URL is now being used
api_key = os.getenv("GROQ_API_KEY")

# Set up headers for the API request, including authentication
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Function to query the LLAMA 3.2 model via the Groq API
def query_elon(prompt, context=""):

    # Construct the payload for the API request
    data = {
        "model": "llama-3.2-3b-preview",  # Using LLAMA 3.2 model
        "messages": [
            {"role": "system", "content": "You are Elon Musk, a tech entrepreneur and innovator."},  # Sets AI persona
            {"role": "user", "content": f"{context}\n{prompt}"}  # User's query with optional context
        ],
        "max_tokens": 200,  # Limits the response length
        "temperature": 0.7  # Controls randomness in responses
    }

    try:
        # Send a POST request to the API with headers and data
        response = requests.post(api_url, headers=headers, json=data)
        response.raise_for_status()  # Raises an exception for HTTP errors

        # Extract and return the AI-generated response
        return response.json().get("choices", [{}])[0].get("message", {}).get("content", "Error: No response")

    except requests.exceptions.RequestException as e:
        # Return the error message if an API request fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    response = query_elon("Tell me about SpaceX.")
    print("\nElon Musk (LLAMA 3.2 via Groq):", response)
