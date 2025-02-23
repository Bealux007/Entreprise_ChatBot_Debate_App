import openai
import os

# Function to generate a response from Steve Jobs' AI persona
def query_steve(user_input, context=""):
    """
    Generates a response from the Steve Jobs AI persona using OpenAI's GPT-4o-mini model.
    
    Parameters:
    - user_input (str): The debate topic or question that Steve Jobs' AI should respond to.
    - context (str, optional): Additional context to help guide the response.

    Returns:
    - str: A generated response from the AI persona of Steve Jobs.
    """

    # Construct the prompt for the AI, simulating Steve Jobs' perspective
    prompt = f"You are Steve Jobs. Answer this debate topic: {user_input}\n\nContext: {context}"
    
    # Call OpenAI's GPT-4o-mini model to generate a response
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are Steve Jobs, a visionary and innovator."},  # Sets AI persona
            {"role": "user", "content": prompt}  # Provides the debate topic/question
        ],
        max_tokens=200  # Limits response length
    )
    
    # Extract and return the AI-generated response
    return response['choices'][0]['message']['content']


# Function to generate a follow-up question from Steve Jobs' perspective
def generate_steve_follow_up(user_input):
    """
    Generates a relevant follow-up question from Steve Jobs' perspective based on user input.

    Parameters:
    - user_input (str): The initial debate topic or question.

    Returns:
    - str: A follow-up question generated from the AI persona of Steve Jobs.
    """

    # Construct the prompt to generate a follow-up question
    follow_up_prompt = f"As Steve Jobs, what relevant follow-up question would you ask based on this input: {user_input}?"

    # Call OpenAI's GPT-4o-mini model to generate the follow-up question
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are Steve Jobs, a visionary and innovator."},  # Sets AI persona
            {"role": "user", "content": follow_up_prompt}  # Provides the topic for generating a follow-up question
        ],
        max_tokens=100  # Limits response length
    )
    
    # Extract and return the AI-generated follow-up question
    return response['choices'][0]['message']['content']
