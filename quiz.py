       # To make the position of the button random, let's define two keyboard that activates with 50% probability
        if (bool(random.getrandbits(1))):
            keyboard = [[Button.inline("{}".format(sum), sum)],
                        [Button.inline("{}".format(sum_not_true), sum_not_true)]]
        else:
            keyboard = [[Button.inline("{}".format(sum_not_true), sum_not_true)],
                        [Button.inline("{}".format(sum), sum)]]

        text = "<b>Quiz time</b> 🤖\n{} + {} = ?\n".format(str(rand1), str(rand2))
        await conv.send_message(text, buttons=keyboard, parse_mode='html')
        press = await conv.wait_event(press_event(SENDER))
        choice = str(press.data.decode("utf-8"))

        if (choice == str(sum)):
            await conv.send_message("Correct Answer!", parse_mode='html')
        else:
            await conv.send_message("Nope, i won!", parse_mode='html')

        await conv.cancel_all()
        return

    ### MAIN

name = '__main__'
if name == '__main__':
    print("bot started")
    client.run_until_disconnected()
