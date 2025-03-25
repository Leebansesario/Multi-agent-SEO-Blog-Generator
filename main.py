from agents.research_agent import fetch_trending_topics
from agents.planning_agent import create_outline
from agents.content_agent import generate_content
from agents.seo_agent import optimize_content
from agents.review_agent import proofread

def generate_blog():
    topic = fetch_trending_topics()[0]
    outline = create_outline(topic)

    blog_content = f"# {outline['title']}\n\n{outline['introduction']}\n\n"
    for section in outline['sections']:
        blog_content += f"## {section['heading']}\n\n{generate_content(section)}\n\n"

    blog_content += f"### Conclusion\n\n{outline['conclusion']}"
    blog_content = optimize_content(blog_content)
    blog_content = proofread(blog_content)

    with open("blog_output.md", "w", encoding="utf-8") as file:
        file.write(blog_content)

    print("Blog generated successfully!")

if _name_ == "_main_":
    generate_blog()
