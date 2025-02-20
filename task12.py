import os

def check_file_permissions(file_path):
    permissions = {
        "exists": os.path.exists(file_path),
        "readable": os.access(file_path, os.R_OK),
        "writable": os.access(file_path, os.W_OK),
        "executable": os.access(file_path, os.X_OK)
    }
    return permissions

file_path = input("Enter the file path: ")
permissions = check_file_permissions(file_path)

print(f"File exists: {permissions['exists']}")
print(f"File is readable: {permissions['readable']}")
print(f"File is writable: {permissions['writable']}")
print(f"File is executable: {permissions['executable']}")
