import os

def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f"File Name {filename}: Created Successfully!")
    except FileExistsError:
        print(f"File Name {filename} already exists!")

    except Exception as E:
        print(f"Error creating File: {E}")

def view_all_files():
    files = os.listdir() #list all the file and directory in current directory
    if not files:
        print("No files found")
    else:
        print("Files in directory")
        for file in files:
            print(file)
    
def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been removed succesfully")

    except FileNotFoundError:
        print("ERROR: File not found")
    except Exception as e:
        print(f"An error occured: {e}")

def read_file(filename):
    try:
        with open(filename , "r") as f:
            content = f.read()
            print(f"Content of {filename} : \n{content}")

    except FileNotFoundError:
        print(f"ERROR: The file {filename} Not Found")

    except Exception as e :
        print(f"An error occurred {e}")

def edit_file(filename):
    try:
        with open(filename, "a") as f:
            content = input("What do you want to add: ")
            f.write(content + "\n")
            print("Content added SUCCESS")

    except FileNotFoundError:
        print(f"ERROR: The file {filename} Not Found")

    except Exception as e :
        print(f"An error occurred {e}")






