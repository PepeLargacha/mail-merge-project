path = './Output/ReadyToSend/'
a_list = './Input/Names/invited_names.txt'

def write_birthday_invite(name, path):
    """
    Takes a name and replaces in all '[name]' occurences in a model
    The model argument need to be the Absolute or Relative path to the file in txt.
    And the path to the folder where it will write the new file.
    The path can be absolute or relative, as default it is relative, so if you want to
    change it, just set the relative argument to False
    """
    with open('./Input/Letters/starting_letter.txt') as starting_letter:
        content = starting_letter.read()
        new_content = content.replace('[name]', f'{name}')
        with open(f'{path}{name}.txt', mode='w') as new_file:
            new_file.write(new_content)


def get_names_from_list(a_list):
    """Get all names from a txt list with one name per line. and retura a list of names"""
    with open(f'{a_list}') as invites:
        all_invites = invites.readlines()
        names = []
        for guest in all_invites:
            guest_name = guest.strip('\n')
            names.append(guest_name)
    return names


def write_invites(a_list_of_guests, path, write_function):
    for guest in a_list_of_guests:
        write_function(guest, path)

write_invites(get_names_from_list(a_list), path, write_birthday_invite)