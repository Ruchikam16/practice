import pickle
name=["ruchika","ankita","renu","anil"]
age=["26","23","50","55"]
pickle_file= open("pickle_file.txt", "wb")
pickle.dump(name,pickle_file)
pickle.dump(age,pickle_file)
pickle_file.close()
