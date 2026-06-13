info = [
    ["Alice", "Math"],
    ["Bob", "Science"],
    ["Alice", "Science"],
    ["Charlie", "Math"],
    ["Bob", "Math"],
    ["Alice", "English"],
    ["Charlie", "English"],
]

# course_set =set()
# for tup in info:
#     course_set.add(tup[1])
#     print(course_set)

for name, subject in info:
    if (subject=="English"):
      print(name)
 
