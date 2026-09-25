import csv

name = input("What's your name? ")
college = input("What's your college? ")


with open("student.csv", mode="a") as file:
  writer = csv.writer(file)
  writer.writerow({"name": name, "college": college})


