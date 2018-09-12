import sys
from collections import defaultdict

def run_brainfuck(code):
    code = remove_white_space(code)

    cells = defaultdict(int)
    cell_pointer = 0
    instruction_pointer = 0

    while instruction_pointer < len(code):
        command = code[instruction_pointer]

        if command == "+":
            cells[cell_pointer] += 1
        elif command == "-":
            cells[cell_pointer] -= 1
        elif command == ">":
            cell_pointer += 1
        elif command == "<":
            cell_pointer -= 1
        elif command == ".":
            print(chr(cells[cell_pointer]), end = "")
        elif command == ",":
            text = input()
            assert len(text) == 1
            cells[cell_pointer] = ord(text)
        elif command == "[":
            if cells[cell_pointer] == 0:
                depth = 0
                index = instruction_pointer + 1
                while not (code[index] == "]" and depth == 0):
                    if code[index] == "[": depth += 1
                    if code[index] == "]": depth -= 1
                    index += 1
                instruction_pointer = index
        elif command == "]":
            depth = 0
            index = instruction_pointer - 1
            while not (code[index] == "[" and depth == 0):
                if code[index] == "]": depth += 1
                if code[index] == "[": depth -= 1
                index -= 1
            instruction_pointer = index - 1

        instruction_pointer += 1


def remove_white_space(text):
    text = text.replace(" ", "")
    text = text.replace("\n", "")
    text = text.replace("\t", "")
    return text

run_brainfuck(sys.argv[1])
