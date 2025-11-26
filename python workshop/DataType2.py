Student_names=["Shruthi","Swathi","Arjun","Anush","Siri"];
print(Student_names[1])

print(Student_names[-1])

Student_names[1]="Sumi"

print(Student_names[1])


Student_names.append("Vaish")
print(f" After modification: {Student_names}")
Student_names.append("Arya")
print(f" After modification: {Student_names}")
Student_names.append("Megha")
print(f" After modification: {Student_names}")
Student_names.append("Bhavya")
print(f" After modification: {Student_names}")


Student_names.remove("Siri")
print(f" After modification: {Student_names}")
Student_names.remove("Anush")
print(f" After modification: {Student_names}")


Student_names.insert(7,"Siri")
print(f" After modification: {Student_names}")
Student_names.insert(6,"Shiv")
print(f" After modification: {Student_names}")
Student_names.insert(8,"Krati")
print(f" After modification: {Student_names}")



Student_names.pop(9)
print(f" After modification: {Student_names}")
Student_names.pop(8)
print(f" After modification: {Student_names}")



print(f" Length of list : {len(Student_names)}")



print(Student_names.reverse())


print(type(Student_names))
