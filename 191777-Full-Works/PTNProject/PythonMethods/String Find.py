



#To find the total occurrence of a substring
my_string = "test string test, test string testing, test string test string"
startIndex = 0
count = 0
for i in range(len(my_string)):
    k = my_string.find('test', startIndex)
    if(k != -1):
        startIndex = k+1
        count += 1
        k = 0
print("The total count of substring test is: ", count )