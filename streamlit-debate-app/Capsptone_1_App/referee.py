# load the necessary modules 
import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Ensure correct API URL format
api_url = os.getenv("GROQ_API_URL")  # Should be "https://api.groq.com/openai/v1/chat/completions"
api_key = os.getenv("GROQ_API_KEY")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

def summarize_and_judge(chat_history):
    """Summarizes the debate and ensures ONE clear winner (Steve or Elon)."""
    
    # Convert chat history into a readable debate format
    debate_text = "\n".join([f"{speaker}: {response}" for speaker, response in chat_history])

    summary_prompt = [
        {"role": "system", "content": "You are a debate summarizer."},
        {"role": "user", "content": f"Summarize this debate in 3-5 sentences:\n\n{debate_text}\n\nKeep it neutral and concise."}
    ]

    judge_prompt = [
        {"role": "system", "content": "You are a strict debate referee."},
        {"role": "user", "content": f"""
        Based on the debate below, pick ONE winner.
        
        **Rules:**
        - Pick ONLY ONE winner.
        - Your response MUST be in this format:
          - 'Winner: Steve Jobs' OR  
          - 'Winner: Elon Musk'  
        - DO NOT return a tie.
        - DO NOT provide any extra text.
        
        Debate:
        {debate_text}
        
        Now, decide the winner strictly in the required format.
        """}
    ]

    try:
        # Request Debate Summary
        summary_data = {
            "model": "gpt-4o-mini",
            "messages": summary_prompt,  #  Using "messages" instead of "prompt"
            "temperature": 0.7,
            "max_tokens": 250
        }

        summary_response = requests.post(api_url, json=summary_data, headers=headers)
        summary_response.raise_for_status()
        summary = summary_response.json().get("choices", [{}])[0].get("message", {}).get("content", "").strip()

        #  Request Winner Decision (Ensuring valid format)
        attempts = 3  # Allow retries in case the format is incorrect
        winner = ""

        while attempts > 0:
            judge_data = {
                "model": "gpt-4o-mini",
                "messages": judge_prompt,  #  Using "messages" instead of "prompt"
                "temperature": 0.7,
                "max_tokens": 50
            }

            judge_response = requests.post(api_url, json=judge_data, headers=headers)
            judge_response.raise_for_status()
            winner = judge_response.json().get("choices", [{}])[0].get("message", {}).get("content", "").strip()

            if winner.startswith("Winner: Steve Jobs") or winner.startswith("Winner: Elon Musk"):
                break  #  Valid winner format detected

            attempts -= 1  # Retry if incorrect format

        #  Final validation (Ensure proper formatting)
        if "Steve Jobs" in winner:
            winner = "Winner: Steve Jobs"
        elif "Elon Musk" in winner:
            winner = "Winner: Elon Musk"
        else:
            winner = "Error: Referee failed to select a winner."

        return summary, winner

    except requests.exceptions.RequestException as e:
        return f"Error fetching summary: {str(e)}", "Error fetching winner."
