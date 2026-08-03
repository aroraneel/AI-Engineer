import matplotlib.pyplot as plt

study_hours = [1, 2, 2.5, 3, 4, 5, 6, 6.5, 7, 8]
exam_scores = [45, 50, 55, 58, 65, 70, 78, 80, 88, 92]
 
# 3a. Create a scatter plot of exam_scores vs study_hours
plt.scatter(study_hours , exam_scores   )

# 3b. Add a title: "Study Hours vs Exam Scores"
plt.title("Study Hours vs Exam Scores")

# 3c. Add x-axis label "Hours Studied" and y-axis label "Exam Score"
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")

# 3d. Show the plot
plt.show()