helo=["my name is ruchika" , "\nHey world", "\they hey hey"]
file_input=open("file_write_ruch.txt","w")
file_input.writelines(helo)
file_input.close()

"""second method for writing lines:
for line in helo:
  file_input.write(line)
  file_input.write("\n")
file_input.close()
#file_input.write(helo1)
#file_input.close()
"""
