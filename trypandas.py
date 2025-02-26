import pandas as pd
# data = [10, 20, 30, 40]
# series = pd.Series(data)
# print(series)

# df= pd.DataFrame(data)
# print(df)
# Name: ["Alice", "Bob", "Charlie", "David"]
# Age: [25, 30, 35, 40]
# City: ["New York", "Los Angeles", "Chicago", "Houston"]
# data={
#     "Name": ["Alice", "Bob", "Charlie", "David"],
#     "Age": [25, 30, 35, 40],
#     "City": ["New York", "Los Angeles", "Chicago", "Houston"]
# }

# df=pd.DataFrame(data)
# print(df)

# Create a Pandas Series containing the numbers 5, 15, 25, 35, and 45. Print the Series.
numbers=[5, 15, 25, 35, 45]
serires=pd.Series(numbers)
print(numbers)

# Product   Price  Quantity
# Apple     50     10
# Banana    30     20
# Orange    40     15

# data={
#     "product": ["Apple","Banana","Orange"],
# "Price": [50,30,40],
# "Quantity":[10,20,15]
# }

# df=pd.DataFrame(data)
# print(df)


data1 = {
    "Name": ["John", "Emma", "Lucas", "Sophia", "Liam"],
    "Age": [22, 25, 30, 28, 35],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Miami"],
    "Salary": [50000, 60000, 70000, 80000, 90000]
}

df1 = pd.DataFrame(data1)
print(df1)

# # Display the first two rows.
# print(df1.iloc[1:3])

# # Display the last three rows.
# print(df1.iloc[3:5])

# # Show the summary of the DataFrame.
# print(df1.info())

# # Show the statistical summary of numerical columns.
# print(df1.describe())

# # Select the "Name" column and print it.
# df2=(df1["Name"])
# print(df2) 
# # OR
# print(df1["Name"])

# # Select the "Name" and "City" columns.
# print(df1[["Name","City"]])

# # Select the second row using .iloc.
# print(df1.iloc[1])

# # Select the rows where Age is greater than 28.
# print("age greater than 28:", df1[df1["Age"]>28])

# # Select the rows where Salary is greater than 60,000 and Age is less than 30.
# print(df1[(df1["Age"]<30) & (df1["Salary"]>60000)])


# # Add a new column "Experience" with values [2, 5, 7, 3, 10].
# df1["Experience"]=[2, 5, 7, 3, 10]
# print(df1)

# # Increase the "Salary" of all employees by 10%.
# print(df1["Salary"]*1.1)

# # Delete the "City" column.
# print(df1.drop(columns=["City"]))

# # Drop the row where "Name" is "Emma".
# df1 = df1.drop(df1[df1["Name"] == "Emma"].index)
# print(df1) #.............Smjh gya but yaad rakhna difficult hai


# Save the modified DataFrame to a CSV file named "employees.csv".

# df1.to_csv("employees.csv", index=False)  # Write to a CSV file #FOR WRITING INDEX=FALSE SHOULD BE ADD,FOR READING IT DOESN'T NEEDED

# file1=pd.read_csv("employees.csv")v   
# print("file:",file1)
# Save the DataFrame to an Excel file named "employees.xlsx".
df1.to_excel("employees.xlsx", index=False) #FOR WRITING INDEX=FALSE SHOULD BE ADD
print(df1)
excelfile=pd.read_excel("employees.xlsx")
print("EXCEL;",excelfile)