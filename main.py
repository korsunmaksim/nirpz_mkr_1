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


def main(input_path_1,input_path_2,same_path,diff_path):
    strs_1=get_data(input_path_1)
    strs_2=get_data(input_path_2)
    same=check_same_elems(strs_1,strs_2)
    diff=check_diff_elems(strs_1,strs_2)
    for elem in check_diff_elems(strs_2, strs_1):
        diff.append(elem)
    write_into_file(same_path,same)
    write_into_file(diff_path,diff)
    print(same,diff)


main("input1.txt","input2.txt","same.txt","diff.txt")