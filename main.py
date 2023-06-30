
# Update with the exercise you are trying to test
from src import solutions
from word_counter import WordCounter
from tax_man import TaxMan
from Calculator import Calculator


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

    

    # solutions.sort_people()
    """
    
    solutions.sort_people(people_list, 'name', 'desc')
    print(people_list)
    

    new_list = solutions.filter_male(people_list)
    print(new_list)
    """

    #new_people_list = solutions.calc_bmi(people_list2) 
    #print(new_people_list)

    # print(solutions.get_people(people_list))
"""
    word_counter = WordCounter(sentence)

    print(word_counter.get_word_count())    # Returns the number of all the words.
    print(word_counter.get_shortest_word()) # Returns the length of the shortest word.
    print(word_counter.get_longest_word())  # Returns the length of the longest word.
"""

"""
items = [
        {"id": 1, "desc": "clock", "price": 1.00},
        {"id": 2, "desc": "socks", "price": 2.00},
        {"id": 3, "desc": "razor", "price": 3.00},
    ]
tm = TaxMan(items, "10%")
tm.calc_total()
print(tm.get_total())
"""

calculator1 = Calculator(4, 3)
calculator1.add(4, 3)
print(calculator1.get_result())


calculator2 = Calculator(4, 3)
calculator2.sub(4, 3)
print(calculator2.get_result())

calculator3 = Calculator(2, 3)
calculator3.mul(2, 3)
print(calculator3.get_result())

calculator4 = Calculator(8, 2)
calculator4.div(8, 2)
print(calculator4.get_result())
















if __name__ == '__main__':
    main()
