import re
import csv

# Regular expression patterns
age_pattern = r'\b(\d{1,3}) years old\b'
insulin_pattern = r'Insulin is (\w+)'
diabetes_pattern = r'has Diabetes with (\w+)'
a1c_pattern = r'A1c result is >(\d)'

# Input and output file paths
input_file = 'data.txt'
output_file = 'diabetes_data.csv'

# Open the input file and read the content
with open(input_file, 'r') as file:
    data = file.read()

# Find all the matches using regular expressions
age_matches = re.findall(age_pattern, data)
insulin_matches = re.findall(insulin_pattern, data)
diabetes_matches = re.findall(diabetes_pattern, data)
a1c_matches = re.findall(a1c_pattern, data)

# Create a list of dictionaries for each patient
patients = []
for i in range(len(age_matches)):
    patient = {
        'Age': age_matches[i],
        'Insulin': insulin_matches[i],
        'Diabetes Type': diabetes_matches[i],
        'A1c Level': a1c_matches[i]
    }
    patients.append(patient)

# Write the extracted data to a CSV file
with open(output_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=patients[0].keys())
    writer.writeheader()
    writer.writerows(patients)

print('Data extraction and CSV creation completed successfully.')