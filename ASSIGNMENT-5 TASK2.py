LIST=[1,2,3,4,5,6,7,8,9,10]
LIST_NEW=[]
for i in range(5):
    LIST_NEW.append(LIST[i])
print("Orginal lisLt:",LIST)
print("Extracted five elements are: ",LIST_NEW)
LIST_NEW.reverse()
print("Reversed extracted elements: ",LIST_NEW)

