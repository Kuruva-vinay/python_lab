import csv

def create_csv_file(filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['empno', 'name', 'salary'])
        while True:
            empno = input("Enter employee number (or 'done' to finish): ")
            if empno.lower() == 'done':
                break
            name = input("Enter employee name: ")
            salary = input("Enter employee salary: ")
            writer.writerow([empno, name, salary])

def search_employee(filename, empno):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == empno:
                return row[1], row[2]
    return None

def main():
    filename = 'employee_details.csv'
    create_csv_file(filename)
    empno = input("Enter employee number to search: ")
    result = search_employee(filename, empno)
    if result:
        print(f"Employee Name: {result[0]}, Salary: {result[1]}")
    else:
        print("Employee not found.")

if __name__ == "__main__":
    main()
