from models import VideoScript

def get_chatgpt_response(initial_prompt, name, client):
    combined_prompt = f"{initial_prompt}\n\n{name}"
    response = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",  # Ensure this model supports structured outputs
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": combined_prompt}
        ],
        response_format=VideoScript,  # Use the Pydantic model
    )
    structured_response = response.choices[0].message.parsed
    print("Response received.")
    return structured_response