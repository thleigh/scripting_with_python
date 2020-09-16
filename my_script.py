#open a file
tanner_file = open('tanner.txt', 'a')

numbers = [1, 2, 3]
for i in range(len(numbers)):
    num = numbers[i]
    tanner_file.write("{}\n".format(num))

#write to the file
# tanner_file.write('Student at General Assembly')

#add \n to add to the next line
# tanner_file.write('\nHello Tanner')

#read a file
# print(tanner_file.read())

#close a file
tanner_file.close()

adam_file = open('adam.txt', 'w')
adam_file.write('Adam')
adam_file.close()

#Look up how to read lines from a file in python
new_file = open('new_file.txt')
file_items = new_file.readlines()\

for i in range(len(file_items)):
    each_item = file_items[i]
    print('Before: {}'.format(each_item))
    print(each_item[0:-1])
    file_items[i] = each_item[0:-1]
    print(file_items)

print(file_items)

new_file.close()

