import re

print("""       
        Welcome
You are in the Madlib Game  
We Hope You'r Ready To play With Us
This game is tack some words from you.
""")

def read_template(path):
    with open(path) as file:
        return file.read().strip()

def parse_template(text):
    regex = re.compile(r"{(.+?)}")

    parts = regex.findall(text)

    stripped_template = regex.sub('{}', text)

    return stripped_template, tuple(parts)


def merge(text,tep):
    return text.format(*tep)

# this write inside my file  that founded madlib_game_file_output.txt
def create_file(result ,file_to_write_on_it):
    with open(file_to_write_on_it, "w") as f:
        f.write(result)

# file to read from and file to write in it
def start_game(file_toRead_game,file_toWrite_game):
    text = read_template(file_toRead_game)
    stripped_text, parts_tuple = parse_template(text)
    user_input = []
    
    for i in range(len(parts_tuple)):
        x = input('enter a {} > '.format(parts_tuple[i]))
        user_input.append(x)
    result = stripped_text.format(*user_input)
    print(f"this is the story you wrote it \n{result}")
    create_file(result,file_toWrite_game)
if __name__=="__main__":
    start_game("assets/madlib_game_read.txt","assets/madlib_game_file_output.txt")
