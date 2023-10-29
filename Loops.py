# for loop is used for iterating over a sequence (taht is either a list, tupke, dictionary, set or a string)

people= ['ankita', 'john', 'danny', 'ankit']

#simple for loop
for person in people:
    print(f'current person: {person}')

# break
for person in people:
    if(person == 'danny'):
        break
    print(f'current person: {person}')  

# continue
for person in people:
    if(person == 'danny'):
        continue
    print(f'current person: {person}')    


# range
for i in range(len(people)):
    print(people[i])


for i in range(0, 11):
    print(f'Number: {i}')    


# while loop executes a set of statements as long as a condition is true 

count= 0
while count <= 10:
    print(f'Count: {count}')
    count += 1