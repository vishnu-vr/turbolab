import os

def find_duplicates():
	path = "/Users/vishnu/Desktop/turbolabs/data"

	files = os.listdir(path)

	# print(files)

	hash_map = {}

	for filee in files:
		open_file = open(path+'/'+filee,'r')

		file_content = open_file.read().strip()

		file_name = filee.split('.')[0]

		# print(file_name_without_extension)	

		if file_content not in hash_map:
			hash_map[file_content] = []
			hash_map[file_content].append(file_name)
		else:
			hash_map[file_content].append(file_name)

	values = list(hash_map.values())

	return values

if __name__ == '__main__':
    result = find_duplicates()
    for row in result:
        print(" ".join(str(i) for i in row))



