alphabet = "abcdefghijklmnopqrstuvwxyz"


def chart_generator():
    # Generates a list of lists representing the virgenére chart, with the key letter in the left-hand
    # side, and the message letter on the top row.
    alpha_list = []
    virgenere_grid = []

    for i in alphabet:
        # Transforms alphabet string into a chart containing each character as a string item.
        alpha_list.append(i)

    def offset(list_to_offset, offset_value):
        # Generates offset values of the alphabet, moving the first letter to the end every time it runs.
        offset_alphabet_list = list_to_offset[offset_value:] + list_to_offset[:offset_value]
        return offset_alphabet_list

    chart_counter = 1
    # Counter makes sure the index of the alpha_list won't extrapolate.
    while len(virgenere_grid) < 26:
        if len(virgenere_grid) == 0:
            virgenere_grid.append(alpha_list)
        else:
            virgenere_grid.append(offset(alpha_list, chart_counter))
            chart_counter += 1
        # While loop adds original alpha_list and subsequent offset lists to a variable called virgenere_grid.

    return virgenere_grid


def cypher_extender(key, message):
    # Makes the keyword the same length as the input message, allowing for the use of the virgenere_grid.
    extended_cypher = []
    extend_counter = 0
    while len(extended_cypher) < len(message):
        extended_cypher.append(key[extend_counter])
        extend_counter += 1
        if extend_counter == len(key):
            extend_counter = 0

    # while loop repeats the characters in the key in order until it is as long as the input message.
    return extended_cypher


def encode():
    # Prompts user for the keyword to use in encoding and what the message to encode is.
    cypher = str(input('What will be the code word?')).lower()

    def input_key_handler(key=str):
        if key.isalpha():
            handled_key = key
            return handled_key
        else:
            corrected_key_input = input('Your key must contain only letters. Please input again.')
            return input_key_handler(corrected_key_input)

    cypher = input_key_handler(cypher)

    input_message = str(input('What is the message?')).lower()

    def input_message_handler(string=str):
        if not string.isalpha():
            corrected_message_input = input('Your message must contain only letters. Please input again.')
            return input_message_handler(corrected_message_input)
        else:
            return string

    message = input_message_handler(input_message)
    coded_message = ''
    virgenere_grid = chart_generator()
    # I don't really know how to use a variable returned from other functions, so I assigned it to a new variable
    # with the same name, which seemed to work. I must look up if there is a way to do that better.
    extended_cypher = cypher_extender(cypher, message)
    coding_counter = 0
    # Counter synchronizes the indexes of the characters in the extended key and the input message.
    while coding_counter < len(message):
        coded_message += virgenere_grid[alphabet.index(extended_cypher[coding_counter])][alphabet.index(message[coding_counter])]
        coding_counter += 1

    print(coded_message)
    exiting = input('Press enter to exit')
    # Prevents the console from quitting straight after the encoding.


def decode():
    decoded_message = ''
    decoding_key = str(input('What was is the key to decode?')).lower()

    def input_key_handler(key=str):
        # Makes sure that the cypher key is alpha.
        if key.isalpha():
            handled_key = key
            return handled_key
        else:
            corrected_key_input = input('Your key must contain only letters. Please input again.')
            return input_key_handler(corrected_key_input)

    decoding_key = input_key_handler(decoding_key)

    message_to_decode = str(input('What is the message to be decoded?'))

    def input_message_handler(string=str):
        # Makes sure the message to be decoded is alpha.
        if not string.isalpha():
            corrected_message_input = input('Your message must contain only letters. Please input again.')
            return input_message_handler(corrected_message_input)
        else:
            return string

    message_to_decode = input_message_handler(message_to_decode)

    extended_decoding_key = cypher_extender(decoding_key, message_to_decode)

    virgenere_grid = chart_generator()

    # Generates grid of offset alphabet sets.

    extended_cypher = cypher_extender(decoding_key, message_to_decode)
    # Extends cypher to the same length of the message to decode by making it into a list.

    decoding_counter = 0
    # Counter synchronizes the indexes of the characters in the extended key and the input message.
    while decoding_counter < len(message_to_decode):
        line = alphabet.index(extended_decoding_key[decoding_counter])
        letter_position = virgenere_grid[line].index(message_to_decode[decoding_counter])

        decoded_message += virgenere_grid[0][letter_position]

        decoding_counter += 1

    print(decoded_message)
    input('Press enter to exit')
    # Allows time to look at the decoded message before console closes.


def welcome():
    print('Welcome to the Virgenere_cypher encoder / decoder. \n What would you like to do today?')
    options = input('1. Encode \n'
                    '2. Decode \n'
                    '3. Exit \n')

    if options in '1.' or options.lower() in 'encode':
        encode()
    elif options in '2.' or options.lower() in 'decode':
        decode()
    elif options in '3.' or options.lower() in 'exit':
        print('Thank you for considering this software. I hope to see you next time! \n'
              'Press enter to exit.')
        input()
        quit()
    else:
        print('Input not recognized. Please try again. \n')
        welcome()


welcome()
