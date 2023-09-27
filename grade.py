last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

subjects = ["physics", "calculus", "poetry", "history"]

grades = [98, 97, 85, 88]

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

print(gradebook)

# Add computer science with grade 100 into gradebook using append()
gradebook.append(["computer science"])
gradebook[4].append(100)
print(gradebook)

# Add visual arts into grade book using append([,])
gradebook.append(["visual arts", 93])
print(gradebook)

# Add 5 points to visual arts grade.
gradebook[5][1] += 5
print(gradebook)

# Switch poetry grade from numerical to Pass/Fail
gradebook[2].remove(85)
print(gradebook)

gradebook[2].append("Pass")
print(gradebook)

# Combined last year and this year grade book into full grade book.
full_gradebook = gradebook + last_semester_gradebook
print(full_gradebook)
