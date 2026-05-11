#copying data of one file to a new file
with open(r"C:\python\file.txt", "r") as source_file:
    data = source_file.read()
with open(r"C:\python\new_file1.txt", "w") as destination_file:
    destination_file.write(data)

#pickling and unpickling in file handling
import pickle
data = {'name': 'Alice', 'age': 30, 'city': 'New York'}
with open(r"C:\python\data.pkl", "wb") as file:
    pickle.dump(data, file)
with open(r"C:\python\data.pkl", "rb") as file:
    loaded_data = pickle.load(file)
    print(loaded_data)