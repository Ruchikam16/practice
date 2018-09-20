import pickle
open_pickle_file=open("pickle_file.txt","rb")
neww=pickle.load(open_pickle_file)
sec_neww=pickle.load(open_pickle_file)
print( "data read iss :" ,neww,"\n",sec_neww)
