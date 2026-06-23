filename=input("Enter the  filename:")

try:
    with open(filename,"r") as file:
        text=file.read()

    lines=text.split("\n")
    linecount=len(lines) 

    words=text.split()
    wordcount=len(words)

    char_count=len(text)   

    print("Number of Lines      :", linecount)
    print("Number of Words      :", wordcount)
    print("Number of Characters :", char_count)

except FileNotFoundError:
    print("Error:File not found")


