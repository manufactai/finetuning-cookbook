from openai import OpenAI

adapter_name="financial-phrases"
port=9000

client = OpenAI(
    api_key="none",
    base_url=f"http://localhost:{port}/v1",
)

result=client.chat.completions.create(
    model=adapter_name,
    messages=[
        {"role": "user", "content": "Pharmaceuticals group Orion Corp reported a fall in its third-quarter earnings that were hit by larger expenditures on R&D and marketing ."}
    ]
)

print(result.choices[0].message.content)