import memory_profiler as mem_profile
import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

Before=str(mem_profile.memory_usage())

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(0,num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person

# t1 = time.clock()
# people = people_list(10000) uncomment this and comment line 35 to see the result by print the same data using lists
# t2 = time.clock()

# t1 = time.clock()
people = people_generator(1000000)
# t2 = time.clock()

for i in people:
    print(i)

print('Memory (Before) : ' + Before + 'MB')
print('Memory (After) : ' + str(mem_profile.memory_usage()) + 'MB')
# print ('Took ' + str(t2-t1) + ' Seconds')
