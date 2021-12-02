Dict={'Tim':18,'Charlie':12,'Tiffany':22,'Robert':22}
print("length : %d" % len(Dict))

Dict={'Tim':18,'Charlie':12,'Tiffany':22,'Robert':22}
print("Variable Type : %s" % type(Dict))

Dict={'Tim':18,'Charlie':12,'Tiffany':22,'Robert':22}
print("Printable string:%s" %str(Dict))
#merging dictionary
dict1 = {"username":"XYZ","email":"xyz@gmail.com","Location":"mumbai"}
dict2 = {"first name":"Nick","last Name":"Jonas"}
dict1.update(dict2)
print(dict1)
#dictionary membership test
dict = {"username":"XYZ","email":"xyz@gmail.com","Location":"mumbai"}
print("email" in dict)
print("Location" in dict)
print("test" in dict)
dict = {"username":"XYZ","email":"xyz@gmail.com","Location":"mumbai"}
dict.pop("username")
print(dict)
dict = {"username":"XYZ","email":"xyz@gmail.com","Location":"mumbai"}
dict['Name']='Nick'
print(dict)

dict = {"username":"XYZ","email":"xyz@gmail.com","Location":"mumbai"}
dict['username']='ABC'
print(dict)

dict = {"username":"XYZ","email":"xyz@gmail.com","Location":"mumbai"}
dict2 = {"first name":"Nick","last Name":"Jonas"}
dict["name"]=dict2
print(dict)




