def summarize_text(prompt):
    return "[Summary]: " + prompt[:50] + "..."

def correct_grammar(prompt):
    return "[Corrected Grammar]: " + prompt.capitalize().rstrip('.') + "."

def rewrite_tone(prompt, tone):
    return f"[Rewritten in {tone} tone]: {prompt}"

def translate_text(prompt, lang):
    return f"[Translated to {lang}]: {prompt}"

def generate_headline(prompt):
    return "[Headline]: " + prompt[:8].capitalize() + "..."

def extract_keywords(prompt):
    return "[Keywords]: " + ", ".join(prompt.split()[:5])
