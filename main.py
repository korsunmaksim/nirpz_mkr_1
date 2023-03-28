def get_data(file_path):
    info = []
    file=open(file_path,'r')
    for str in file:
        info.append(str)
    file.close()
    return info


    