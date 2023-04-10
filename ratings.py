"""Restaurant rating lister."""


# put your code here
def ratings(filename):
    file_ratings = open(filename)
    new_dict = {}
    for line in file_ratings:
        name_and_score = line.strip().split(":")
        new_dict[name_and_score[0]] = name_and_score[1] # Dictionary Name[KEY] = VALUE

    for rest, rating in sorted(new_dict.items()):
        print(f'{rest} is rated at {rating}.')

ratings("scores.txt")