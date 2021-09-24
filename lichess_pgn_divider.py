# write the file name to break here, no .txt please
path = "Garry_Kasparov_-_My_Great_Predecessors_Vol_1"
x = 30  # this is the limit on size of pgn

path1 = path + ".pgn"
f = open(path1,'r')
pgn = f.read() 
# though no need of pgn
# print(pgn)  , this is good 
f.seek(0) 

# number of file for file naming
num_file = 1  # 1 so as to include last one too
variations = 0 # number of variations in the file, or instantly how many are read
for line in f.readlines():
    if (line[0:7] == "[Event "):
        variations = variations + 1 
        if ((variations%x) == 0):
            # print(variations)
            num_file = num_file + 1 
# line[-2:] == "*\n"
# print(variations)
# print(num_file) 

f.seek(0)


# Let's change the names of file and write in it
base_name = path + "_"
list_name = []
for i in range (1,num_file+1):
    dummy = base_name + str(i) + ".pgn"
    list_name.append(dummy)

f2 = open(list_name[0], 'w')
count = 0
i = 0
for line in f.readlines(): 
    if (line[0:7] == "[Event "):
        count = count + 1       
        if (count%x == 0):
            i = i + 1
            f2 = open(list_name[i], 'w') 
    f2.write(line)

f2.close()
f.close()
