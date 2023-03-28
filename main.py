#Get info from files
def get_data(file_path):
    info = []
    file=open(file_path,'r')
    for line in file:
        line=line.replace("\n","")
        info.append(line)
    file.close()
    return info

#Write info into file
def write_into_file(file_path:str,info):
    file = open(file_path, "w")
    file.truncate()
    for line in info:
        file.write(line + "\n")
    file.close()

#Check same elements
def check_same_elems(arr_1,arr_2):
    same= []
    for elem in arr_1:
        if elem in arr_2:
            same.append(elem)
    return same


#Check diff elements
def check_diff_elems(arr_1,arr_2):
    diff= []
    for elem in arr_1:
        if elem not in arr_2:
            diff.append(elem)
    return diff


    