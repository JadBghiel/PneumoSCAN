##
## EPITECH PROJECT, 2026
## cvrie
## File description:
## clean_student_dataset
##

import pandas as pd

PATH = "rsrc/Student_Dataset.csv"
CLEAN_FILE_PATH = "rsrc/Student_Dataset_Clean.csv"

# cat rsrc/Student_Dataset.csv
# 1,On uneven paths the heel feels wobbly side‑to‑side. Slanted pavements bring a quick aching shift under the ankle when I step.
# 2,0x000000,"The feverish feeling eased, but I’m now breathing faster with a dry, exhausting cough. I get light‑headed after climbing stairs and feel like I can’t fill my lungs completely."
# 3,0x000000,"While working in the garden, I touched a metal grill that had been on the stove. My left forearm has a burning itch and a faint scar."
# 4,A short sprint brought on a twinge in the middle of the back of my thigh. It’s tender along a band and stiffens if I sit too long.
# 5,0x000000,"I accidentally left my hand on a hot mug for a minute. It now feels very tender, and there's a small blister."
# 6,A sudden twist while reaching for a bag made one side of my lower back feel ‘switched off’ and sore. Small stabilizing movements feel shaky.
# 7,0x000000,"During a birthday party, a hot beverage was knocked onto my back. The area is red, tender, and a small blister is visible on my shoulder."

def clean_student_dataset():
    with open(PATH, "r") as file:
        lines = file.readlines()
    cleaned_lines = []
    for line in lines:
        cleaned_line = line.strip().replace("0x000000,", "")
        cleaned_lines.append(cleaned_line)

    with open(CLEAN_FILE_PATH, "w") as file: # ineed to create or truncate the file before writing
        file.write("Id,Description\n") # write the header
        file.write("\n".join(cleaned_lines))

def add_proper_new_column():
    df = pd.read_csv(CLEAN_FILE_PATH)
    #now to append the colum ColourCode with the value 0x000000 for all rows
    df["ColourCode"] = "0x000000" #this works good, it adds the column with the value for all rows
    #now some of the description are closed with quotes and some are not, we need to add them to all descriptions, we can use the apply function to add quotes to all descriptions
    df["Description"] = df["Description"].apply(lambda x: f'"{x}"' if not x.startswith('"') else x) #this will add quotes to all descriptions that do
    df.to_csv(CLEAN_FILE_PATH, index=False)

if __name__ == "__main__":
    clean_student_dataset()
    add_proper_new_column()