subjects=int(input("Enter Numbr of Subjects:"))
total=0

for i in range(subjects):
    marks=float(input(f"Enter marks for subject {i+1}:"))
    total+=marks

average=total/subjects

if average>=90:
    grade='A+'
elif average>=80:
    grade='A' 
elif average>=70:
    grade='B' 
elif average>=60:
    grade='C' 
elif average>=50:
    grade='D' 
else:
    grade='F'

print("Average Marks =",average)
print("Grade =",grade)            