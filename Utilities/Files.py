fi = r'C:\Users\gnl999935\Documents\SACS\Lift\saclst.lift'
fi1 = r'C:\Users\gnl999935\Documents\SACS'
# with open(fi,'r') as f:
# 	data = f.read()

# # print(data)

# with open(r'C:\Users\gnl999935\Documents\SACS\Lift\saclst1.lift','w') as f:
# 	f.write(data)


from pathlib import Path

# entries = Path(fi1)
# for entry in entries.iterdir():
#     print(entry.name)



# basepath = Path(fi1)
# files_in_basepath = basepath.iterdir()
# for item in files_in_basepath:
#     if item.is_file():
#         print(item.name)



# # List all files in directory using pathlib
# basepath = Path(fi1)
# files_in_basepath = (entry for entry in basepath.iterdir() if entry.is_file())
# for item in files_in_basepath:
#     print(item.name)



# # List all subdirectory using pathlib
# basepath = Path(fi1)
# for entry in basepath.iterdir():
#     if entry.is_dir():
#         print(entry.name)



# from pathlib import Path
# current_dir = Path(fi1)
# for path in current_dir.iterdir():
#     info = path.stat()     
#     print(info.st_mtime)


# from datetime import datetime
# from os import scandir

# def convert_date(timestamp):
#     d = datetime.utcfromtimestamp(timestamp)
#     print('d',d)
#     formated_date = d.strftime('%d %b %Y')
#     return formated_date

# def get_files():
#     dir_entries = scandir(fi1)
#     for entry in dir_entries:
#         if entry.is_file():
#             info = entry.stat()
#             print(f'{entry.name}\t Last Modified: {convert_date(info.st_mtime)}')





# os.mkdir(fi1+'/'+ 'example_directory/')

# from pathlib import Path

# from pathlib import Path

# p = Path(fi1+'/'+ 'example_directory/')
# try:
#     p.mkdir(exist_ok=True)
# except FileExistsError as exc:
#     print(exc)






# p = pathlib.Path(fi1+'/'+'2019/11/05')
# p.mkdir(parents=True)




# os.chdir(fi1)
# # Walking a directory tree and printing the names of the directories and files
# for dirpath, dirnames, files in os.walk('.',topdown=False):
#     print(f'Found directory: {dirpath}')
#     # print('name of directory is ',dirnames)
#     for file_name in files:
#         print(file_name)




# from tempfile import TemporaryFile

# # Create a temporary file and write some data to it
# fp = TemporaryFile('w+t')
# fp.write('Hello universe!')

# # Go back to the beginning and read data from file
# fp.seek(0)
# data = fp.read()

# print('data',data)

# # Close the file, after which it will be removed
# fp.close()




# from pathlib import Path

# data_file = Path('home/data.txt')

# try:
#     data_file.unlink()
# except FileNotFoundError as e:
#     print(f'Error: {data_file} : {e.strerror}')





# trash_dir = Path('my_documents/bad_dir')

# try:
#     trash_dir.rmdir()
# except OSError as e:
#     print(f'Error: {trash_dir} : {e.strerror}')




# import shutil

# trash_dir = 'my_documents/bad_dir'

# try:
#     shutil.rmtree(trash_dir)
# except OSError as e:
#     print(f'Error: {trash_dir} : {e.strerror}')



# import os

# for dirpath, dirnames, files in os.walk('.', topdown=False):
#     try:
#         os.rmdir(dirpath)
#     except OSError as ex:
#         pass




# import shutil

# src = 'path/to/file.txt'
# dst = 'path/to/dest_dir'
# shutil.copy(src, dst)




# import shutil

# src = 'path/to/file.txt'
# dst = 'path/to/dest_dir'
# shutil.copy2(src, dst)





# import shutil
# shutil.copytree('data_1', 'data1_backup')



# import shutil
# shutil.move('dir_1/', 'backup/')


# from pathlib import Path
# data_file = Path('data_01.txt')
# data_file.rename('data.txt')



# import glob
# glob.glob('*.py')



# import glob
# for name in glob.glob('*[0-9]*.txt'):
#     print(name)



# import glob
# for file in glob.iglob('**/*.py', recursive=True):
#     print(file)


# import os
# fi2 = r'C:\Users\gnl999935\Documents'
# os.chdir(fi2)


# import glob
# for file in glob.iglob('**/*.py'):
#     print(file)



# p = Path('.')

# for name in p.glob('*\\*.py'):
#     print(name)



# file = open(r'C:\Users\gnl999935\Documents\text.txt','w')

# file.write('something')
# file.close()



def isPal(x):
    assert type(x) == list
    temp = x
    temp.reverse
    if temp == x:
        return True
    else:
        return False

def silly(n):
    for i in range(n):
        result = []
        elem = input('Enter element: ')
        result.append(elem)
    if isPal(result):
        print('Yes')
    else:
        print('No')


silly(5)


# def isPal(x):
#     assert type(x) == list
#     temp = x
#     print('t',x.reverse())
#     # temp.reverse()
#     # print(temp.reverse())
#     print(x)

#     if temp == x:
#         return True
#     else:
#         return False

# x = ['a','c','g','t']
# w = isPal(x)
# print(w)