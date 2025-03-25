def create_outline(topic):
    outline = {
        "title": topic,
        "introduction": "Briefly introduce the topic and its relevance.",
        "sections": [
            {"heading": "Current Trends", "content": "Discuss recent changes in HR."},
            {"heading": "Challenges", "content": "List common challenges and solutions."},
            {"heading": "Future Outlook", "content": "What to expect in the coming years."}
        ],
        "conclusion": "Summarize key points and suggest next steps."
    }
    return outline

if _name_ == "_main_":
    topic = "Remote Work and Employee Engagement"
    print(create_outline(topic))
