import csv
import re
# Define the headers for the CSV file
fields = ['Name', 'Age', 'Gender', 'Type of Diabetes',
          'Insulin', 'A1C Levels', 'On Medication', 'Readmission Time']

# Initialize a list to hold all the extracted data
rows = []

# Open the text file for reading
with open('data.txt', 'r') as file:
    # Regular expression pattern to extract age, insulin level, and type of diabetes
    pattern = r"(\d+) years old.*Insulin is ([A-Za-z]+)\..*has Diabetes with ([a-zA-Z\s]+)- (type I|type II)\."
    diabetes_type = ''
    insulin = ''
    # Iterate over each line in the file and extract the required information
    for line in file:

        # Extract the name from the line
        name = line.split(' ')[0] + ' ' + line.split(' ')[1]

        # Extract the age from the line
        age = int(line.split(' ')[3])

        # Extract the gender from the line
        gender = line.split(' ')[6].rstrip('.')

        # Extract the type of diabetes from the line
        # diabetes_type = line.split(' ')[12].rstrip('.')

        # Extract the insulin status from the line
        # Search for pattern in each line
        match = re.search(pattern, line)
        if match:
            insulin = match.group(2)
            diabetes_type = match.group(3).strip()
        # insulin = line.split(' ')[9]
        # print(insulin)
        # insulin = ''
        # if 'Insulin is ' in line:
        # insulin = line.split(' ')[6]
        # print(insulin)
        # Extract the A1C levels from the line (if present)
        # a1c = ''
        # if 'A1c result is' in line:
        # a1c = line.split(' ')[4]
        # else:
        #    alc = 'NA'
        a1c = 'Yess' if 'A1c result is ' in line else 'No'
        # Determine if the patient is on medication
        on_medication = 'Yes' if 'Patient is on diabetes meds' in line else 'No'

        # Extract the readmission time from the line
        readmission_time = ''
        if 'Pt. got readmitted' in line:
            readmission_time = line.split(
                ' ')[-2] + ' ' + line.split(' ')[-1].rstrip('.\n')

        # Create a dictionary with the extracted information
        row = {'Name': name, 'Age': age, 'Gender': gender, 'Type of Diabetes': diabetes_type,
               'Insulin': insulin, 'A1C Levels': a1c, 'On Medication': on_medication, 'Readmission Time': readmission_time}

        # Append the dictionary to the list of rows
        rows.append(row)

# Write the extracted data to a CSV file
with open('output_from_data.csv', 'w', newline='') as file:
    # Create a CSV writer object
    writer = csv.DictWriter(file, fieldnames=fields)

    # Write the headers to the CSV file
    writer.writeheader()

    # Write each row of data to the CSV file
    for row in rows:
        writer.writerow(row)
