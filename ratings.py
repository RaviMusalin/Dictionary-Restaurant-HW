"""Restaurant rating lister."""


# put your code here
file_ratings = open("scores.txt")

for line in file_ratings:
    # split_line = line.rsplit()
    name_and_score = line.strip().split(":")
    # name_and_score = split_line.split(':')
    print(name_and_score)