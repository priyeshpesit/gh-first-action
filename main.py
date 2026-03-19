from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-4.1",
    input=open("tef_prompt.txt").read(),
)

print(response.output[0].content[0].text)