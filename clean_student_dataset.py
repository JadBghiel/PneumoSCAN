##
## EPITECH PROJECT, 2026
## cvrie
## File description:
## clean_student_dataset
##

PATH = "rsrc/Student_Dataset.csv"


def clean_student_dataset():
    with open(PATH, "r") as file:
        lines = file.readlines()
    cleaned_lines = []
    for line in lines:
        cleaned_line = line.strip().replace("0x000000,", "")
        cleaned_lines.append(cleaned_line)
    clean_file_path = "rsrc/Student_Dataset_Clean.csv"
    with open(clean_file_path, "w") as file: # ineed to create or truncate the file before writing
        file.write("Id,Description\n") # write the header
        file.write("\n".join(cleaned_lines))

if __name__ == "__main__":
    clean_student_dataset()