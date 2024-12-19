class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)
        print(f"{self.name} enrolled in {course.title}.")

class Course:
    def __init__(self, title, description, instructor):
        self.title = title
        self.description = description
        self.instructor = instructor
        self.materials = []
        self.assignments = []

    def add_material(self, material):
        self.materials.append(material)

    def add_assignment(self, assignment):
        self.assignments.append(assignment)

class Assignment:
    def __init__(self, title):
        self.title = title
        self.submissions = {}

    def submit(self, student, answer):
        self.submissions[student.name] = answer
        print(f"{student.name} submitted assignment {self.title}.")

    def grade(self, student, feedback):
        if student.name in self.submissions:
            print(f"{student.name} received feedback: {feedback}")
        else:
            print(f"No submission found for {student.name}")

# Example usage
student1 = User("John Doe", "john@example.com")
course1 = Course("Python Programming", "Learn Python from scratch", "Jane Smith")

course1.add_material("Video Lecture 1: Introduction to Python")
course1.add_material("Quiz 1: Basic Syntax")
assignment1 = Assignment("Assignment 1: Python Basics")
course1.add_assignment(assignment1)

student1.enroll(course1)
assignment1.submit(student1, "My answer to Python basics")
assignment1.grade(student1, "Good job!")
