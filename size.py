import os

def getFileSize(file_path):
    file = open(file_path,'rb')
    all_data = file.read()
    file.close()

    bytes = 0
    for data in all_data:
        bytes = bytes + 1
        #print(data)
    return bytes


if __name__ == '__main__':
    #os.chdir('.\\dist')
    file_path = 'todo1.exe'
    size = os.path.getsize(file_path)
    print(f"Size of {file_path}: {size} bytes")

    file_size = getFileSize(file_path)

    print(f"Size of {file_path}: {file_size} bytes")