import base64
import json
import os

from dotenv import load_dotenv
from perplexity import Perplexity

def main():
    load_dotenv()

    # TODO: error handling
    perplexity_api_key = os.getenv("PERPLEXITY_API_KEY")

    client = Perplexity(api_key=perplexity_api_key)

    # Read and encode file
    with open("CV.pdf", "rb") as file:
        file_data = file.read()
        encoded_file = base64.b64encode(file_data).decode('utf-8')

    completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Get candidate's name and surname and their spoken languages from the attached CV and return a pure JSON object with the keys 'name' (str), 'surname' (str), 'languages' (list)"
                                ". Do not include anything but the JSON object in your response."
                    },
                    {
                        "type": "file_url",
                        "file_url": {
                            "url": encoded_file
                        }
                    }
                ],
            }
        ],
        model="sonar-pro",
    )

    response = completion.choices[0].message.content
    print(response)
    if "```json" in response:
        content_start = response.find("```json")+len("```json")
        content_end = response.find("```", content_start)
        json_response = json.loads(response[content_start:content_end])
    else:
        json_response = json.loads(response)
    print(f"name: {json_response['name']}, surname: {json_response['surname']}, languages: {json_response['languages']}")

if __name__ == "__main__":
    main()
