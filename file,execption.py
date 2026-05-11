# Open a file and print it's content
with open("file.txt", "r") as file:
    content = file.read()
    print(content)

#create a file and write 5 line of content to it
with open("file.txt", "w") as file:
    for i in range(5):
        file.write(f"Line {i+1}\n")

# add new conteent to the file
with open("file.txt", "a") as file:
    file.write("This is an additional line.\n")

