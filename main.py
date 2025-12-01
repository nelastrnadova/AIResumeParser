from openai import OpenAI
client = OpenAI()

#TODO: test if env api key is set

response = client.responses.create(
    model="gpt-5-nano",
    input="Write a one-sentence summary of a random CV."
)

print(response.output_text)