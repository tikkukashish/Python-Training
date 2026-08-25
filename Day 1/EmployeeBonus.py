rating=int(input("Enter the rating: "))
experience=int(input("Enter the experience: "))
salary=int(input("Enter the salary: "))
project_status=input("Enter the project status: ")

if rating == 5 and experience>10 and project_status == "on time":
    print(f"bonus: {salary*0.3}")

if rating == 4 and experience>7:
    print(f"bonus: {salary*0.2}")

if rating == 3 and project_status == "delayed":
    print(f"bonus: {salary*0.05}")
