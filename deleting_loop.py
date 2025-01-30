greetings = ['hello', 'hi', 'hey', 'greetings', 'hi', 'hello', 'hi']
newGreetings = []
newGreetings2 = [word for word in greetings if word == 'hi']

for word in greetings:
    if word == 'hi':
        newGreetings.append(word)

greetings = newGreetings
print(greetings)
print("newGreetings2: ", newGreetings2)