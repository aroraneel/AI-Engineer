import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
website_visitors = [1200, 1500, 1400, 1800, 2100, 1900]
 
# 1a. Create a line plot of website_visitors over months
plt.plot(months, website_visitors)

# 1b. Add a title: "Website Visitors Over 6 Months"
plt.title("Website Visitors Over 6 Months")

# 1c. Add x-axis label "Month" and y-axis label "Visitors"
plt.xlabel("Months")
plt.ylabel("Visitors")

# 1d. Show the plot
plt.show()