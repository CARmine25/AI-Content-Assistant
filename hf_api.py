def get_dummy_response(prompt: str) -> str:
    if "capital of india" in prompt.lower():
        return "The capital of India is New Delhi."
    elif "translate" in prompt.lower():
        return "यह एक डमी अनुवाद है।"
    return "This is a dummy response. [No real AI output yet]"
