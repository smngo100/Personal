# 8-9. Messages
def show_messages(short_messages):
    for short_message in short_messages:
        print(short_message)

short_msgs = ['hello', 'wyd', 'hru', 'idk']
show_messages(short_msgs)
print()


# 8-10. Sending Messages
def send_messages(short_messages, sent_messages):
    while short_messages:
        sending_messages = short_messages.pop()
        print(f"Sending messages: {sending_messages}")
        sent_messages.append(sending_messages)

def show_sent_messages(sent_messages):
    for sent_message in sent_messages:
        print(f"Messages sent: {sent_message}")

# OR
"""
def show_sent_messages(sent_messages):
    print("Messages sent: ")
    for sent_message in sent_messages:
        print(f"{sent_message}")
"""

short_messages = ['hello', 'wyd', 'hru', 'idk']
sent_messages = []

send_messages(short_messages, sent_messages)
show_sent_messages(sent_messages)
print()


# 8-11. Archived Messages
def send_messages(short_messages, sent_messages):
    while short_messages:
        sending_messages = short_messages.pop()
        print(f"Sending messages: {sending_messages}")
        sent_messages.append(sending_messages)

def show_sent_messages(sent_messages):
    for sent_message in sent_messages:
        print(f"Messages sent: {sent_message}")

short_messages = ['hello', 'wyd', 'hru', 'idk']
sent_messages = []

send_messages(short_messages[:2], sent_messages)
show_sent_messages(sent_messages)
