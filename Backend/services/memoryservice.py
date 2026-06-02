conversation_memory = []


def add_message(role, content):

    conversation_memory.append({
        "role": role,
        "content": content
    })

    # Keep last 10 messages
    if len(conversation_memory) > 10:
        conversation_memory.pop(0)


def get_history():

    history = ""

    for msg in conversation_memory:

        history += (
            f"{msg['role']}: "
            f"{msg['content']}\n"
        )

    return history