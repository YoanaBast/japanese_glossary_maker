from text_transformer import TextTransformer

transform = TextTransformer()


def multiline_input(prompt="Paste your text (type END on a new line to finish):", end_command="END"):
    print(prompt)
    lines = []
    while True:
        line = input()
        if line.strip() == end_command:
            break
        lines.append(line.strip())
    return " ".join(lines)  # Join lines with spaces instead of newlines


def add_words_to_db(inst):
    transform.take_unique_words_from_str(multiline_input('Please dump your text here: (type END when done)'))
    transform.add_words_to_db()
    transform.refresh_text_file()

def add_words_to_common_for_exclusion(inst):
    transform.add_to_common_for_exclusion(*multiline_input("Add words (separate by a comma): (type END when done)").split(', '))

def user_check():
    print('Choose an option:\nAdd words to the glossary (1)\nAdd words for exclusion (2)\nExit (3)')
    return int(input('Your answer (type 1, 2, or 3): '))

while True:
    answer = user_check()
    if answer == 1:
        add_words_to_db(transform)
    elif answer == 2:
        add_words_to_common_for_exclusion(transform)
    elif answer ==3:
        print('Cya')
        break
    else:
        print('Please choose a valid answer!')
