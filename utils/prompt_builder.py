def load_prompt_template(filepath="prompts/default_prompt.txt"):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def build_prompt(user_query):
    template = load_prompt_template()
    return template.replace("{{query}}", user_query.strip())
