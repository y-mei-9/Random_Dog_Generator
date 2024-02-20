# Yingyi 
# 2/13/2024
# Period 4
# Dog Breeds

# Initialize
import csv
import random
import webbrowser

# File Path
dog_csv_path = "Dogs.csv"  
# Empty Vars for function
index = 0
dog_name = ""
xl_dog_list, large_dog_list, medium_dog_list, small_dog_list = [], [], [], []
# Empty Vars to store data from csv
dog_breeds_list, max_weights_list, dog_images_list, dog_group_list, short_descriptor_list, temperament_list = [], [], [], [], [], []

# Function

# Sorts the dog breeds into size groups
def sort_size():
    for i in range(0, len(max_weights_list)):
        weight = int(max_weights_list[i])
        if weight >= 70:
            xl_dog_list.append(dog_breeds_list[i])
        elif weight >= 60:
            large_dog_list.append(dog_breeds_list[i])
        elif weight >= 20:
            medium_dog_list.append(dog_breeds_list[i])
        else:
            small_dog_list.append(dog_breeds_list[i])

# Generates a short description of the dog
# Parameter (dog_name) is a set
def generate_description(dog_name):
    global index
    index = dog_breeds_list.index(dog_name)
    print(f"\nThe {dog_name} is a {dog_group_list[index].lower()} dog ({short_descriptor_list[index].lower()}). Its typical temperaments are: {temperament_list[index].lower()}.")

# Generates image of the dog
def generate_image():
    webbrowser.open(dog_images_list[index])


# Main

# Retrieve data and put into lists
with open(dog_csv_path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        dog_breeds_list.append(row[1])
        max_weights_list.append(row[9])
        dog_images_list.append(row[11])
        dog_group_list.append(row[2])
        short_descriptor_list.append(row[3])
        temperament_list.append(row[10])


sort_size()

# Generates a random breed with a short description based on user preference
user_preference = input("Welcome to the Pet Shelter.\nWhat size of dog (XL, L, M, S) would you like?: ").upper()
if user_preference == "XL":
    dog_name = random.choice(xl_dog_list)
elif user_preference == "L":
    dog_name = random.choice(large_dog_list)
elif user_preference == "M":
    dog_name = random.choice(medium_dog_list)
elif user_preference == "S":
    dog_name = random.choice(small_dog_list)
else:
    print("Invalid Input")
print(f"\nHere is a {user_preference} dog: {dog_name}")
generate_description(dog_name)

# Opens an image if the user wishes to see the dog
see_image = input("Would you like to see an image (Y or N)?: ").upper()
if see_image == "Y":
    generate_image()
else:
    print("Ok. Goodbye!")
