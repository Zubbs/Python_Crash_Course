import json

def input_favourite_number():
    fav_number_file = 'fav_number.json'
    try:
        with open(fav_number_file) as file_object:
            number = json.load(file_object)
    
    except FileNotFoundError:
        number = input('what is your favourite number: ')
        fav_number_file = 'fav_number.json'
        with open(fav_number_file, 'w') as file_object:
            json.dump(number,file_object)

    else:

        print(f'I know your favourite number, its {number}')




input_favourite_number()
print_favourite_number()