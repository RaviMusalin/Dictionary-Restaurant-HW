"""Restaurant rating lister."""


# put your code here
new_dict = {}

restaurant_name = input("What is the restaurant name? ")
restaurant_rating = input("What is the restaurants rating? ")
new_dict[restaurant_name.strip()] = restaurant_rating.strip()

def ratings(filename):
    file_ratings = open(filename)
    
    for line in file_ratings:
        name_and_score = line.strip().split(":")
        new_dict[name_and_score[0]] = name_and_score[1] # Dictionary Name[KEY] = VALUE

    for rest, rating in sorted(new_dict.items()):
        print(f'{rest} is rated at {rating}.')


ratings("scores.txt")
