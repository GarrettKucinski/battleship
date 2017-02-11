
# value = "Hi my name is Garrett! I don't like to fish, I like crafting. I do like eating fish though. Crafting is fun."
value = "Treehouse Rocks. rocks are cool. I like using Treehouse! What do you use?"

# def word_count(value):
    # word_count = {}
    # sentence = ""
    # punctuation = ",.'!?"
    #
    # for letter in value:
    #     if letter not in punctuation:
    #         sentence += letter.lower()
    #
    # for word in sentence.split(' '):
    #     if word not in word_count.keys():
    #         word_count[word] = 1
    #     else:
    #         word_count[word] += 1
    #
    # return word_count

def word_count(words):
    words = words.lower().split()
    word_count = dict()
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    return word_count

def combo(one, two):
    pairs = []
    for index, item in enumerate(one):
        pairs.append((one[index], two[index]))

    print(pairs)

# combo('hel', [2, 3, 5,])

COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

def covers(topics):
    for course, covers in COURSES.items():
        if covers & topics:
            print(course)

def covers_all(topics):
    matched_courses = []
    for course, covers in COURSES.items():
        if topics == topics & covers:
            matched_courses.append(course)
    print(matched_courses)

# covers_all({"input", "strings"})

TILES = ('-', ' ', '-', ' ', '-', '||',
         '_', '|', '_', '|', '_', '|', '||',
         '&', ' ', '_', ' ', '||',
         ' ', ' ', ' ', '^', ' ', '||'
)

# for tile in TILES:
#     if tile == '||':
#         print('\n')
#     else:
#         print(tile, end='')


BOARD_SIZE = 10
BOARD_HEADING = [chr(letter) for letter in range(ord('A'), ord('A') + BOARD_SIZE)]

def create_board():
    board = [['0' for space in range(BOARD_SIZE)] for row in range(BOARD_SIZE)]
    return board

def place_ship(location, length, orientation, board, ship):
    alpha = ''.join([chr(letter) for letter in range(65,75)]).lower()
    column, row = location

    row = row - 1
    column = alpha.index(column)

    if orientation.lower() == 'h':
        if '-' not in board[row][column:(column + length)] and '|' not in board[row][column:(column + length)]:
            board[row][column:(column + length)] = ['-' for num in range(length)]
        else:
            print('Sorry, {} cannot be placed, you already have a ship there, please replace your ship'.format(ship))

    if orientation.lower() == 'v':
        v_pos = list()

        for board_row in range(row, (row + length)):
            v_pos.append(board[board_row][column])

        if '-' not in v_pos and '|' not in v_pos:
            for board_row in range(row,(row + length)):
                board[board_row][column] = '|'
        else:
            print('Sorry, {} cannot be placed, you already have a ship there, please replace your ship'.format(ship))

    return board

def print_board(board):
    '''first print three spaces

    c will take on the value of each number
    specified in range(ord('A'), ord('A') + BOARD_SIZE).
    passing each number to chr(c) generates
    the letter equivalent of that number

    In this case with board_SIZE == 10
    and range(ord('A'), ord('A') + board_SIZE) == range(66, 76)

    This loop will iterate though the numbers 66-76
    By passing each number to chr() via the iterator variable c
    it will print out the letters A-J
    '''

    print("   " + " ".join(BOARD_HEADING))

    row_num = 1
    for row in board:
        print(str(row_num).rjust(2) + " " + (" ".join(row)))
        row_num += 1

game_board = create_board()

# should place ship
new_game_board = place_ship(('b',3), 5, 'h', game_board, 'Air Carrier')

SHIP_INFO = [
    ("Aircraft Carrier", 5),
    ("Battleship", 4),
    ("Submarine", 3),
    ("Cruiser", 3),
    ("Patrol Boat", 2)
]

board_heading_str = ', '.join(str(alpha).lower() for alpha in BOARD_HEADING)
for ship_name, ship_length in SHIP_INFO:
    while True:

        # 11. Prompt player for guess.
        position = input("Player One, Enter a location for {}: ".format(ship_name))

        if position[0] not in board_heading_str:
            print("Your column must be a letter.")
            continue

        orientation = input('Player One, Enter an orientation for {}'.format(ship_name))

        if orientation not in 'hv':
            print('You must pick either "h" or "v"')
            continue

        # If we get here, the entry was vaild, so beak out
        break
