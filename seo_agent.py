import re

def optimize_content(content):
    keywords = ["HR trends", "remote work", "employee engagement"]
    for keyword in keywords:
        content = re.sub(rf"\b{keyword}\b", f"<strong>{keyword}</strong>", content, flags=re.I)
    return content

if _name_ == "_main_":
    sample_content = "HR trends show that remote work improves employee engagement."
    print(optimize_content(sample_content))
