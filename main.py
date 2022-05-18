#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

model = './Input/Letters/starting_letter.txt'
path = './Output/ReadyToSend/'

def write_birthday_invite(name, model, path):
    """
    Takes a name and replaces in all '[name]' occurences in a model
    The model argument need to be the Absolute or Relative path to the file in txt.
    And the path to the folder where it will write the new file.
    The path can be absolute or relative, as default it is relative, so if you want to
    change it, just set the relative argument to False
    """
    with open(model) as starting_letter:
        content = starting_letter.read()
        new_content = content.replace('[name]', f'{name}')
        with open(f'{path}{name}.txt', mode='w') as new_file:
            new_file.write(new_content)

def get_names_from_list(a_list):
    
    with open('./Input/Names/invited_names.txt') as invites:
        all_invites = invites.readlines()
        names = []
        for guest in all_invites:
            print(guest)
            guest_name = guest.strip('\n')
            print(guest_name)
            names.append(guest_name)

