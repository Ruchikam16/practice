import pickle
pickle_read_dict=open("pickle_read_2.txt","wb")
dataset={
    'name':["ruchika","ankita","renu","anil"],
    'fruits':["mango","litchi","banana"]
    }
pickle.dump(dataset,pickle_read_dict)
pickle_read_dict.close()
