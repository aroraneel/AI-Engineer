import matplotlib.pyplot as plt

# Using ALL the data from Tasks 1-3 above, plus one more series:
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
website_visitors = [1200, 1500, 1400, 1800, 2100, 1900]

languages = ["Python", "JavaScript", "Java", "C++", "Go"]
popularity_score = [85, 78, 65, 55, 40]

study_hours = [1, 2, 2.5, 3, 4, 5, 6, 6.5, 7, 8]
exam_scores = [45, 50, 55, 58, 65, 70, 78, 80, 88, 92]

temperature_by_month = [15, 18, 22, 28, 33, 30]   # matches `months` from Task 1
 
# 4a. Create a 2x2 grid of subplots using plt.subplots(2, 2, figsize=(10, 8))
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# 4b. In slot [0,0] (top-left): line plot of website_visitors over months
axes[0,0].plot(months, website_visitors)
axes[0,0].set_title("Website Visitors Over 6 Months")

# 4c. In slot [0,1] (top-right): bar plot of popularity_score by languages
axes[0,1].bar(languages, popularity_score)
axes[0,1].set_title("Programming Language Popularity")

# 4d. In slot [1,0] (bottom-left): scatter plot of exam_scores vs study_hours
axes[1,0].scatter(study_hours, exam_scores)
axes[1,0].set_title("Study Hours vs Exam Scores")

# 4e. In slot [1,1] (bottom-right): line plot of temperature_by_month over months
# 4f. Give EACH subplot its own title using .set_title("...")
axes[1,1].plot(months, temperature_by_month)
axes[1, 1].set_title("Temperature Over 6 Months")

# 4g. Call plt.tight_layout() then plt.show()
plt.tight_layout()
plt.show()