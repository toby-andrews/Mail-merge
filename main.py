with open("./Input/Names/invited_names.txt") as file:
    names = (file.readlines())

with open("./Input/Letters/starting_letter.txt") as start_letter:
    contents = start_letter.read()

for letter in range(0, len(names)):
    new_invite = contents.replace("[name]", (names[letter].strip()))
    file = open(f"./Output/ReadyToSend/invite_for_{(names[letter])}", mode="w")
    file.write(new_invite)
file.close()
