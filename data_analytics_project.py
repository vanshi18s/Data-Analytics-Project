import pandas as pd
import matplotlib.pyplot as plt


# Load the dataset
df = pd.read_csv('online_course_engagement_data.csv')

# Explore the dataset
print(df)
print(df.info())
print(df.describe())

# A histogram of time spent

plt.hist(df['TimeSpentOnCourse'], bins=50)
plt.xlabel('Time Spent (minutes)')
plt.ylabel('Frequency')
plt.title('Time Spent Distribution')
plt.show()

df = pd.read_csv('online_course_engagement_data.csv')

#The course completion rate for each course category

completion_rates = df.groupby('CourseCategory')['CourseCompletion'].mean()
print(completion_rates)

# A bar chart for the completion rates

plt.bar(completion_rates.index, completion_rates.values)
plt.xlabel('Course Category')
plt.ylabel('Course Completion Rate')
plt.title('Course Completion Rate by Course Category')
plt.show()