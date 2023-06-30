
# Update with the exercise you are trying to test
from src import solutions
from word_counter import WordCounter
#from tax_man import TaxMan


def main():


    people_list = [
    {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
    {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
]   
    people_list2 = [
        {'id': 2, 'name': 'bob',     'weight_kg': 90, 'height_meters': 1.7},
        {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
    ]

    sentence = "This is a test of the emergency broadcast system"

    items = [
        {"id": 1, "desc": "clock", "price": 1.00},
        {"id": 2, "desc": "socks", "price": 2.00},
        {"id": 3, "desc": "razor", "price": 3.00},
    ]

    # solutions.sort_people()
    
    
    solutions.sort_people(people_list, 'name', 'desc')
    print(people_list)
    

    new_list = solutions.filter_male(people_list)
    print(new_list)
    

    new_people_list = solutions.calc_bmi(people_list2) 
    print(new_people_list)

    print(solutions.get_people(people_list))

    word_counter = WordCounter(sentence)

    print(word_counter.get_word_count())    # Returns the number of all the words.

    print(word_counter.get_shortest_word()) # Returns the length of the shortest word.
    print(word_counter.get_longest_word())  # Returns the length of the longest word.

    

















if __name__ == '__main__':
    main()
