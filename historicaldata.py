import pandas as pd
from datetime import datetime, timedelta

# Read input CSV file
input_file = "input.csv"
df = pd.read_csv(input_file)

# Sort data by Employee Code and Date of Joining
df['Date of Joining'] = pd.to_datetime(df['Date of Joining'])
df.sort_values(by=['Employee Code', 'Date of Joining'], inplace=True)

# Function to transform columnar data into row-based format
def transform_data(df):
    transformed_data = []
    effective_dates = {}
    end_dates = {}

    for index, row in df.iterrows():
        employee_code = row['Employee Code']
        manager_code = row['Manager Employee Code']

        if employee_code not in effective_dates:
            effective_dates[employee_code] = []
            end_dates[employee_code] = []

        if not effective_dates[employee_code]:
            effective_dates[employee_code].append(row['Date of Joining'])
            end_dates[employee_code].append(row['Date of Exit'] - timedelta(days=1))
        else:
            effective_dates[employee_code].append(end_dates[employee_code][-1] + timedelta(days=1))
            end_dates[employee_code].append(row['Date of Exit'] - timedelta(days=1))

        # Assign far-future date for the latest record
        if pd.isnull(row['Date of Exit']):
            end_dates[employee_code][-1] = datetime(2100, 1, 1)

        for i in range(len(effective_dates[employee_code])):
            record = {
                'Employee Code': employee_code,
                'Manager Employee Code': manager_code,
                'Effective Date': effective_dates[employee_code][i].strftime('%Y-%m-%d'),
                'End Date': end_dates[employee_code][i].strftime('%Y-%m-%d'),
                'Compensation': row['Compensation'],
                'Compensation 1': row['Compensation 1'],
                'Compensation 2': row['Compensation 2'],
                'Review 1': row['Review 1'],
                'Review 2': row['Review 2'],
                'Engagement 1': row['Engagement 1'],
                'Engagement 2': row['Engagement 2']
            }
            transformed_data.append(record)

    return pd.DataFrame(transformed_data)

# Transform data
transformed_df = transform_data(df)

# Write output to CSV
output_file = "historical_employee_data.csv"
transformed_df.to_csv(output_file, index=False)

print("Transformation complete. Output saved to", output_file)
