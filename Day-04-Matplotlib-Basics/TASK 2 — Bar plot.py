import matplotlib.pyplot as plt

languages = ["Python", "JavaScript", "Java", "C++", "Go"]
popularity_score = [85, 78, 65, 55, 40]
 
# 2a. Create a bar plot of popularity_score by languages
plt.bar(languages, popularity_score)

# 2b. Add a title: "Programming Language Popularity"
plt.title("Programming Language Popularity")

# 2c. Add x-axis label "Language" and y-axis label "Popularity Score"
plt.xlabel("Language")
plt.ylabel("Popularity Score")

# 2d. Show the plot
plt.show()