def decodeMorse(morse_code):
    MORSE_CODE = {'....': 'H', '.': 'E', '-.--': 'Y', '': ' ', '.---': 'J', '..-': 'U', '-..': 'D'}
    my_string = [i for i in morse_code.split(' ')]
    my_new_string = ''.join([MORSE_CODE.get(i) for i in my_string])
    # # ToDo: Accept dots, dashes and spaces, return human-readable message
    # return morse_code.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')
    return my_new_string.replace('  ', ' ')


a = '.... . -.--   .--- ..- -.. .'
# MORSE_CODE = {'....': 'H', '.': 'E', '-.--': 'Y', ' ': ' ': ' ', '.---': 'J', '..-': 'U', '-..': 'D'}
print(decodeMorse(a))
