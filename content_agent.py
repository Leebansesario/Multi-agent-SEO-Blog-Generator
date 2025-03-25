import openai

openai.api_key = "your_openai_api_key"

def generate_content(section):
    prompt = f"Write a detailed paragraph about: {section['heading']}. {section['content']}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

if _name_ == "_main_":
    section = {"heading": "Current Trends", "content": "Discuss recent changes in HR."}
    print(generate_content(section))
