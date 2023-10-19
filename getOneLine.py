import openai
import os

# Set up the OpenAI API client
openai.api_key = "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"

# Replace the text below with the content of the article you want to summarize
article_content = """

"""

# Function to generate summary using ChatGPT API
def getOneLine(content):
    prompt = f"""

    Your task is to create a one-line message for the following Twitter user in the format of the following: 
    
    “Hi @_______, I noticed you have an interest in _______, and thought I would reach out”

    Replace the '@______' with the Twitter user's UserName, and replace the second blank space with either the word 'writing', with 25% probability, 'reading' with 25% probability or a personalised word based on their bio/tweets with 50% probability. Do not change the format or append any words to this format. Do not use any hashtags. If the sentence does not make grammatical sense with the personalised word from their bio or tweets, then just use the word 'writing'. Avoid any poitical, religious, non-english or potentially offensive words.

    Here is the context for the Twitter user:
        
    \n\n{content}"""
    
    response = openai.ChatCompletion.create( model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are an assistant crafting short outbound messages to be sent to potential customers."},
                {"role": "user", "content": prompt},
            ],
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.1,

    )
    
    message = response.choices[0].message.content.strip()
    return message

# Generate and print the summary


