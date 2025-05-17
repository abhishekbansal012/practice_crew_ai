def reflection_message(recipient, sender):
    return f'''Review the following content:\n\n{recipient.chat_messages_for_summary(sender)[-1]['content']}'''
