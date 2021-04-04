import datetime
import os
from constants import USERNAME, EXTENSION, CATEGORIES


def get_filename_title(title):
    title = title.replace(" ", "_")
    title = title.replace(".", "_")
    title = title.replace("__", "_")
    return title


def insert_new_problem(existing_problems, new_problem):
    data = []
    for problem in existing_problems:
        problem = problem[1:-1].strip()
        fields = [field.strip() for field in problem.split("|")]
        data.append(fields)
    data.append(new_problem)
    # Sort by category and then problem number ascending
    data = sorted(data, key=lambda x: (x[1], int(x[0].split("/")[-1][:-1])))
    return data


def get_sorted_problem_list(problems, problem_information, category,
                            solution_information):
    new_problem = [problem_information, category, solution_information]
    sorted_problems = insert_new_problem(problems, new_problem)
    lines = []
    for problem in sorted_problems:
        line = "| {} | {} | {} |".format(problem[0], problem[1], problem[2])
        lines.append(line)
    return lines


def update_readme(title, filename_title, url, category):
    separator = '| --- | --- | --- |'
    problem_information = "[{}]({})".format(title, url)
    solution_information = "[Solution](solutions/{})".format(filename_title)
    with open("../README.md", "r+") as readme:
        lines = [line.strip() for line in readme.readlines()]
        separator_index = lines.index(separator) + 1
        header = lines[:separator_index]
        problems = lines[separator_index:]
        problems = [line.strip() for line in problems if line.strip() != '']
        sorted_problems = get_sorted_problem_list(problems,
                                                  problem_information,
                                                  category,
                                                  solution_information)
        # clear the file contents
        readme.seek(0)
        readme.truncate()
        for line in header:
            readme.write(line + "\n")
        for line in sorted_problems:
            readme.write(line + "\n")


def make_problem_directory(repo_path, filename_title):
    directory = os.path.join(repo_path, "solutions", filename_title)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return str(directory)


def make_solution_file(title, category, url, username, directory_path,
                       extension='.py'):
    filename = "solution_" + username + extension
    file_path = os.path.join(directory_path, filename)
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.writelines(
                write_file_header(title, category, url, username, extension))
    return file_path


def write_file_header(title, category, url, username, extension=".py"):
    created_date = datetime.datetime.today().strftime("%d %B %Y")
    multiline_comment_start = '"""\n'
    multiline_comment_end = '"""\n'
    if extension != ".py":
        multiline_comment_start = '/*\n'
        multiline_comment_end = '*/\n'
    header_str = multiline_comment_start
    header_str += 'Title     : ' + title + '\n'
    header_str += 'Category  : ' + category + '\n'
    header_str += 'URL       : ' + url + '\n'
    header_str += 'Author    : ' + username + '\n'
    header_str += 'Created   : ' + created_date + '\n'
    header_str += multiline_comment_end
    return header_str


def get_mandatory_field(user_message, options=None):
    if options:
        options_length = len(options)
        print("\n".join(
            [str(i + 1) + ". " + val for i, val in enumerate(options)]))
        print()
        while True:
            user_input = input(
                user_message + " from 1-{}: ".format(options_length)).strip()
            try:
                user_input = int(user_input)
                if 1 <= user_input and user_input <= options_length:
                    return options[user_input - 1]
                else:
                    raise Exception
            except Exception:
                print("Invalid input. Enter an option from 1-{}: ".format(
                    len(options)))
    else:
        while True:
            if options == None:
                user_input = input(user_message).strip()
                if not user_input:
                    print("Invalid input. Please try again.")
                else:
                    return user_input


def get_user_inputs():
    title = get_mandatory_field("Add new problem title: ")
    filename_title = get_filename_title(title)
    url = get_mandatory_field("Add new problem url: ").rstrip("/")
    category = get_mandatory_field("Select Problem Type ", CATEGORIES)
    username = input("Username (keep blank for " + USERNAME + "): ").strip()
    extension = input("Extension (keep blank for " + EXTENSION + "): ").strip()
    if username == '':
        username = USERNAME
    if extension == '':
        extension = EXTENSION
    return title, filename_title, url, category, username, extension


if __name__ == '__main__':
    title, filename_title, url, category, username, extension = get_user_inputs()
    current_path = os.path.dirname(os.path.realpath(__file__))
    repo_path = os.path.abspath(os.path.join(current_path, os.pardir))
    update_readme(title, filename_title, url, category)
    directory = make_problem_directory(repo_path, filename_title)
    filepath = make_solution_file(title, category, url, username, directory,
                                  extension)
    print("Done. Open {}".format(filepath))
