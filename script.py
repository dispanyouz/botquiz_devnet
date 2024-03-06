### First command, get the time and day
@client.on(events.NewMessage(pattern='(?i)/time'))
async def time(event):
    # Get the sender of the message
    sender = await event.get_sender()
    SENDER = sender.id
    # Define the text and send the message
    text = "Received! Day and time: " + str(datetime.datetime.now())
    await client.send_message(SENDER, text, parse_mode="HTML")
