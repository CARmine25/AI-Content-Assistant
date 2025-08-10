from utils.io_handler import get_user_input, display_output
from utils.logger import log_interaction

if __name__ == "__main__":
    user_input = get_user_input()
    response = f"Echo: {user_input}"
    display_output(response)
    log_interaction(user_input, response)
