# Create a Dictionary of Student Marks

dict = {"Alice": 85, "Alex": 90, "Anjali": 95, "Anshu": 100}
user_input = input("Enter the student's name: ")
user_input = user_input.capitalize()
if user_input in dict:
    print(f"{user_input}'s marks: {dict[user_input]}")
else:
    print("Student not found.")

