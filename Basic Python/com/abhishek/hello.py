import numpy as np
import re
values = [1.2, 1.3]
print(values)
#[1.2, 1.3]

arr1 = np.array([1.2,1.3,1.4])
print(arr1)
## [1.2 1.3 1.4]

list = ['uabc','bdcd','eg']
list1=sorted(list)
print(list1)
#['bdcd', 'eg', 'uabc']

# tuple example : u can not manipulate the value
tuple=(1,2,3)
print (tuple)
#(1, 2, 3)

#dict example
hashmap={1:'abc',2:'cde',3:'dec'}
print(hashmap)
#{1: 'abc', 2: 'cde', 3: 'dec'}

#will return as its not present
print(hashmap.get(5))
#None

f = open("test1.txt",'a+')
# does not take parenthesis for if and for loop
for x in range(10):
    f.write("Hi This is my first file to create and a file in python %d" %x )
f.close()


def main():
    print("this is main function testing")

if __name__ == '__main__':
    main()


# this will parse text
text = "Popularity in 1990"
year_match = re.search(r'Popularity(\sin\s)(\d\d\d\d)', text)
print(year_match)
print(year_match.group(2))

#read content from file and inster in hashmap and print in alphabatic
hashtable = {}
file = open("test1.txt",'rU')
text = file.read()
tuples= re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',text)
for rank_tuple in tuples:
    print(rank_tuple)
    (rank,male,girl) = rank_tuple
    if male not in hashtable:
        hashtable[male]=rank
        hashtable[girl] = rank
print(hashtable)

#after sorting
sortedNames = sorted(hashtable.keys())
print("printing after sorting " )
for entry in sortedNames:
    print(entry + ' ' + hashtable[entry])
file.close()