import pprint

import pyperclip
# dic of tic toe board game vale
theBoards = {
    'top-L' : ' ', 'top-M': ' ', 'top-R' : ' ',
    'bot-L' : ' ', 'bot-M': ' ', 'bot-R' : ' ',
    'low-L' : ' ', 'low-M': ' ', 'low-R' : ' ',

}
theBoards['top-L'] = '0'
theBoards['top-M'] = '0'
theBoards['top-R'] = '0'

Mgs = "555"

pyperclip.copy('The text to be copied to the clipboard.')

print(Mgs.isdecimal())
# pprint.pprint(theBoards)

# function which creates tic toe game board
def printBoard(boards):
    print(theBoards['top-L'] + ' | ' + theBoards['top-M'] + ' | ' + theBoards['top-R'])
    print('----------')
    print(theBoards['bot-L'] + ' | ' + theBoards['bot-M'] + ' | ' + theBoards['bot-R'])
    print('----------')
    print(theBoards['low-L'] + ' | ' + theBoards['low-M'] + ' | ' + theBoards['low-R'])

printBoard(theBoards)