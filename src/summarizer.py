import openai
import os

# Set your OpenAI API key
openai.api_key = 'your-api-key-here'  # Replace with your actual OpenAI API key

def gpt_summarizer(text: str) -> str:
    """
    Summarizes text using OpenAI's GPT model (abstractive summarization).
    """
    try:
        # Request GPT model for a summary
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use a suitable model for summarization
            prompt=f"Summarize the following resume in a concise manner:\n\n{text}",
            max_tokens=150,  # Adjust based on desired summary length
            temperature=0.7  # Controls randomness; lower for more deterministic output
        )

        summary = response.choices[0].text.strip()
        return summary
    except Exception as e:
        return f"An error occurred during summarization: {e}"

# Example usage
if __name__ == "__main__":
    sample_text = """[Insert resume text here for testing]"""
    summarized_text = gpt_summarizer(sample_text)
    print(summarized_text)
