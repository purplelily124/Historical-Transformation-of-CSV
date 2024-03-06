# Historical-Transformation-of-CSV

Approach to this task:

Read the Input CSV File: Start by reading the input CSV file containing the employee data into a pandas DataFrame.

Sort Data by Employee and Effective Date: Sort the DataFrame by employee identifiers and effective dates to prepare for the transformation.

Derive Effective and End Dates: Iterate through each employee's records to derive effective and end dates for each historical record based on the provided instructions.

Transform Columnar Data: Transform columnar data related to compensation, engagement, and review into a row-based format, ensuring each row represents a specific period with consistent data.

Handle Missing Data: Implement logic to handle missing data by inheriting values from the most recent past record for the same employee.

Create Output DataFrame: Create a new DataFrame containing the transformed data in the desired format.

Write Output to CSV: Write the output DataFrame to a CSV file formatted for historical data analysis.
