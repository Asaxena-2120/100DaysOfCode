#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

# Read the sample email format, Reading all the lines as a list
with open('./Input/Letters/starting_letter.txt') as file:
    content = file.readlines()

# Get all the names from invited_names.txt
with open('./Input/Names/invited_names.txt') as names_file:
    names = names_file.readlines()
    for name in names:
        # Removing newline from each name
        name_to_input = name.strip("\n")

        # Create a new file to write contents in Output/ReadyToSend folder
        with open(f'./Output/ReadyToSend/letter_to{name_to_input}.txt', mode='w') as name_letter_file:
            pass

        for i in range(len(content)):
            with open(f'./Output/ReadyToSend/letter_to{name_to_input}.txt', mode='a') as name_letter_file:

            # replace only first line contents
                if i == 0:
                    l = content[i].replace((content[i].strip(' Dear,\n')),name_to_input)
                    name_letter_file.write(l)

                else:
                    name_letter_file.write(content[i])







