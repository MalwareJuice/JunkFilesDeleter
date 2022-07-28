import pathlib
import msvcrt
import time

#get current path
cur_path = pathlib.Path.cwd()

#enumerate all files in the main folder and all subfolders
all_files = [ eachfile for eachfile in cur_path.rglob("*") if eachfile.is_file() ] 

#check if there is no files
if len(all_files) == 1:
	print("No files were found in this directory and all subdirectories\nPress any key to exit...", end='', flush=True)
	if msvcrt.getch():
		exit()

#extract extensions from file names
extensions = []
for eachfile in all_files:
	extensions.append(str(eachfile).split(".")[-1].lower())

extensions = list(set(extensions))

print(f"These are the extensions that were found in this directory and all its subdirectories:\n{extensions}")

#let you choose which files you want to delte based on their extension
while True:
	file_extension = input("Which extension from the above list do you want to delete: ")
	if file_extension.lower() not in extensions:
		print("This extension does not exist in the list!\nPress 'ENTER' to provide another extension or Press any other key to exit...", end='', flush=True)
		if (msvcrt.getch()) != b'\r':
			print("\nExiting...")
			time.sleep(1.5)
			exit()
		else:
			print('')
	else:
		break

#shows you the files that will be deleted
files_to_delete = [ eachfile for eachfile in cur_path.rglob("*."+file_extension) ]

print(f"These are all {file_extension.upper()} files that were found in current directory and its subdirectories:")
counter = 1
for eachfile in files_to_delete:
	print(f" {counter}- {eachfile}")
	counter += 1

#confirm deleteion and exiting
print("Press 'ENTER' to confirm deletion or press any other key to cancel and exit...", end='', flush=True)
if (msvcrt.getch()) == b'\r':
	for eachfile in files_to_delete:
		eachfile.unlink()
	print("\nDone! Press any key to exit")
	if msvcrt.getch():
		exit()
else:
	print("\nCancelled! Exiting...")
	time.sleep(1.5)
	exit()
