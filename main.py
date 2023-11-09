from collections import deque
labyrinth = ["███████", "█     █", "█   ███", "█ ███ █", "█     █", "███████"]

def print_col_lab (lab: list[str]):
    lab_copy = lab.copy()
    # append ROW indexes
    for i in range (len(lab_copy)):
        lab_copy[i] = list(lab_copy[i])
        lab_copy[i].insert(0, str(i))
        lab_copy[i].append(str(i))
        lab_copy[i] = ''.join(lab_copy[i])
    # append COLUMNS indexes
    column_list = [str(i) for i in range(len(lab_copy[0]) - 2)]
    column_list.append(str(' '))
    column_list.insert(0, str(' '))
    column_list = ''.join(column_list)

    lab_copy.insert(0, column_list)
    lab_copy.append(column_list)

    # printing the labirint
    for element in lab_copy:
        print(element)

#STEP 2

# digit input validation
def prompt_integer():
    while True:
        user_input = input("Enter a digit: ")
        if user_input.isdigit():
            return int(user_input)
        else:
            print("This is not a digit! Please enter a digit.")


def prompt_user_for_location(name: str):
    row = prompt_integer()
    column = prompt_integer()
    name = (row, column)
    return name


#STEP 3

from collections import deque
q = deque()

def bfs(labyrinth, start_location, end_location):
    number_of_rows = len(labyrinth)
    number_of_columns = len(labyrinth[0])
    visited_cells = [[False] * number_of_columns for _ in range(number_of_rows)]
    queue = deque([(start_location, [])])

    while queue:
        (current_row, current_col), path = queue.popleft()

        if (current_row, current_col) == end_location:
            return path + [(current_row, current_col)]

        if (0 <= current_col < number_of_columns and
            0 <= current_row < number_of_rows and not
            visited_cells[current_row][current_col] and labyrinth[current_row][current_col] == ' '):
            visited_cells[current_row][current_col] = True

            # up
            queue.append(((current_row - 1, current_col), path + [(current_row, current_col)]))

            # down
            queue.append(((current_row + 1, current_col), path + [(current_row, current_col)]))

            # left
            queue.append(((current_row, current_col - 1), path + [(current_row, current_col)]))

            # right
            queue.append(((current_row, current_col + 1), path + [(current_row, current_col)]))

    # no path
    return None

# PRINTING THE RESULT

def print_result_labyrinth(lab):
    lab_res = lab.copy()

    for elem in path:
        for item in range(len(lab_res)):
            if item == elem[0]:
                lab_res[item] = list(lab_res[item])
                lab_res[item][elem[1]] = 'X'
                lab_res[item] = ''.join(lab_res[item])

    print_col_lab(lab_res)

# RESULT FUNCTIONS:

print_col_lab(labyrinth)
start_location = prompt_user_for_location("start")
end_location = prompt_user_for_location("end")
path = bfs(labyrinth, start_location, end_location)
if len(path) == 1:
    print('There is no possible path solution')
else:
    print_result_labyrinth(labyrinth)