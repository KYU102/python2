x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# # Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print(x)

# # Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
print(students)

# # In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

# # Change the value 20 in z to 30
z[0]['y'] = 30
print(z)



students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    
    for student in students:
        stringList = []
        for t in student.items():
            stringList.append(f"{t[0]} - {t[1]}")

        print(", ".join(stringList))

def iterate(array):
    for x in range(len(array)):
        print('first_name - ' + students[x]['first_name'] + ', ' + 'last_name - ' + students[x]['last_name']) 
        # iterate is the easy way


def iterateDictionary2(key_name,some_list):
    for x in range(len(some_list)):
        print(some_list[x][key_name])

# iterate(students)
iterateDictionary(students)
iterateDictionary2('last_name',students) 



dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(array):
    print(len(array['locations']), 'Locations')
    for x in range(len(array['locations'])):
        print(array['locations'][x])
    
    print(len(array['instructors']), 'Instructors')
    for x in range(len(array['instructors'])):
        print(array['instructors'][x])

printInfo(dojo)
