# Import pandas package
import pandas as pd

def main():
    ## Data exploration in python

    # Assign data
    data = {
        'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj', 'Ravi', 'Natasha', 'Riya'],
        'Age': [17, 17, 18, 17, 18, 17, 17],
        'Gender': ['M', 'F', 'M', 'M', 'M', 'F', 'F'],
        'Marks': [90, 76, 'NaN', 74, 65, 'NaN', 71]
    }

    # Convert into DataFrame
    df = pd.DataFrame(data)

    # Display data
    print(df)

    ## Dealing with missing values in Python

    # Compute average
    c = avg = 0
    for ele in df['Marks']:
        if str(ele).isnumeric():
            c += 1
            avg += ele
    avg /= c

    # Replace missing values
    #df = df.replace(to_replace="NaN", value=avg)
    # Convert 'Marks' to numeric, forcing errors to NaN
    df['Marks'] = pd.to_numeric(df['Marks'], errors='coerce')
    # Replace NaN with the average
    df['Marks'] = df['Marks'].fillna(avg)

    # Display data
    print(df)

    ## Data Replacing in Data Wrangling
    # in the GENDER column, we can replace the Gender column data by categorizing them into different numbers.

    # Categorize gender
    df['Gender'] = df['Gender'].map({'M': 0, 'F': 1}).astype(float)

    # Display data
    print(df)

    ## Filtering data in Data Wrangling
    # suppose there is a requirement for the details regarding name, gender, and marks of the top-scoring students.
    # Here we need to remove some using the pandas slicing method in data wrangling from unwanted data.

    # Filter top scoring students
    df = df[df['Marks'] >= 75].copy()

    # Remove age column from filtered DataFrame
    df.drop('Age', axis=1, inplace=True)

    # Display data
    print(df)

    ## Data Wrangling Using Merge Operation:

    # Creating Dataframe
    details = pd.DataFrame({
        'ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
        'NAME': ['Jagroop', 'Praveen', 'Harjot', 'Pooja', 'Rahul', 'Nikita',
                 'Saurabh', 'Ayush', 'Dolly', "Mohit"],
        'BRANCH': ['CSE', 'CSE', 'CSE', 'CSE', 'CSE', 'CSE', 'CSE', 'CSE', 'CSE', 'CSE']
    })

    # Creating Dataframe
    fees_status = pd.DataFrame({
        'ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
        'PENDING': ['5000', '250', 'NIL', '9000', '15000', 'NIL', '4500', '1800', '250', 'NIL']
    })

    # Merging Dataframe
    print(pd.merge(details, fees_status, on='ID'))

    ## Data Wrangling Using Grouping Method 
    # Use case: cars sold during the year 2010

    # Creating Data
    car_selling_data = {
        'Brand': ['Maruti', 'Maruti', 'Maruti', 'Maruti', 'Hyundai', 'Hyundai',
                  'Toyota', 'Mahindra', 'Mahindra', 'Ford', 'Toyota', 'Ford'],
        'Year': [2010, 2011, 2009, 2013, 2010, 2011, 2011, 2010, 2013, 2010, 2010, 2011],
        'Sold': [6, 7, 9, 8, 3, 5, 2, 8, 7, 2, 4, 2]
    }

    # Creating Dataframe for Provided Data
    df = pd.DataFrame(car_selling_data)

    # Group the data when year = 2010
    grouped = df.groupby('Year')
    print(grouped.get_group(2010))

    #############################
    # Data Wrangling  by Removing Duplication
    # Pandas duplicates() method helps us to remove duplicate values from Large Data.
    # An important part of Data Wrangling is removing Duplicate values from the large data set.

    # initializing Data
    student_data = {
        'Name': ['Amit', 'Praveen', 'Jagroop', 'Rahul', 'Vishal', 'Suraj',
                 'Rishab', 'Satyapal', 'Amit', 'Rahul', 'Praveen', 'Amit'],
        'Roll_no': [23, 54, 29, 36, 59, 38, 12, 45, 34, 36, 54, 23],
        'Email': ['xxxx@gmail.com', 'xxxxxx@gmail.com', 'xxxxxx@gmail.com', 'xx@gmail.com',
                  'xxxx@gmail.com', 'xxxxx@gmail.com', 'xxxxx@gmail.com', 'xxxxx@gmail.com',
                  'xxxxx@gmail.com', 'xxxxxx@gmail.com', 'xxxxxxxxxx@gmail.com', 'xxxxxxxxxx@gmail.com']
    }

    # creating dataframe
    df = pd.DataFrame(student_data)

    # Here df.duplicated() list duplicate  Entries in ROllno.
    # So that ~(NOT) is placed in order to get non duplicate values.
    non_duplicate = df[~df.duplicated('Roll_no')]

    # printing non-duplicate values
    print(non_duplicate)

    ######################
    ## Creating New Datasets Using the Concatenation of Two Datasets
    ##########################

    # Define a dictionary containing employee data 
    data1 = {
        'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age': [27, 24, 22, 32],
        'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
        'Qualification': ['Msc', 'MA', 'MCA', 'Phd'],
        'Mobile No': [97, 91, 58, 76]
    }

    # Define a dictionary containing employee data 
    data2 = {
        'Name': ['Gaurav', 'Anuj', 'Dhiraj', 'Hitesh'],
        'Age': [22, 32, 12, 52],
        'Address': ['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'],
        'Qualification': ['MCA', 'Phd', 'Bcom', 'B.hons'],
        'Salary': [1000, 2000, 3000, 4000]
    }

    # Convert the dictionary into DataFrame  
    df = pd.DataFrame(data1, index=[0, 1, 2, 3])

    # Convert the dictionary into DataFrame  
    df1 = pd.DataFrame(data2, index=[2, 3, 6, 7])

    res = pd.concat([df, df1])
    
    # Display the concatenated DataFrame
    print(res)

if __name__ == "__main__":
    main()