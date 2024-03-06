## Function that waits user event [press button]
def press_event(user_id):
    return events.CallbackQuery(func=lambda e: e.sender_id == user_id)


### Quiz command
@client.on(events.NewMessage(pattern='(?i)/quiz'))
async def quiz(event):
    # get the sender
    sender = await event.get_sender()
    SENDER = sender.id

    # Start a conversation
    async with client.conversation(await event.get_chat(), exclusive=True) as conv:
        # get two random numbers between 1 and 10
        rand1 = randint(1, 10)
        rand2 = randint(1, 10)
        # make the sum
        sum = rand1 + rand2
        # make another sum based on two different random numbers. This will be used for the wrong option
        sum_not_true = randint(1, 10) + randint(1, 10)
