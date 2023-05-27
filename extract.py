import pandas as pd

# Initialize empty lists to store patient information
names = []
ages = []
genders = []
diabetes_types = []
insulin_status = []
readmission_statuses = []
medications = []

# Read data from file
with open('data.txt', 'r') as file:
    lines = file.readlines()

# Process each patient record
for line in lines:
    line = line.strip()
    if line:
        parts = line.split('. ')
        patient_info = parts[0].split(' is ')
        name = patient_info[0]
        age_gender = patient_info[1].split(' years old ')
        age = int(age_gender[0])
        gender = age_gender[1]
        other_info = parts[1:]

        insulin = 'Unknown'
        medication = 'Not on diabetes meds'
        diabetes_type = 'Unknown'
        readmission_status = 'Unknown'

        for info in other_info:
            if info.startswith('Insulin'):
                insulin = info.split(' is ')[1]
            elif info.startswith('Patient is on diabetes meds'):
                medication = 'Diabetes meds'
            elif 'type 1' in info:
                diabetes_type = 'Type I'
            elif 'type II' in info:
                diabetes_type = 'Type II'
            elif info.startswith('Pt. got readmitted'):
                readmission_status = info.split(' in ')[1]

        names.append(name)
        ages.append(age)
        genders.append(gender)
        diabetes_types.append(diabetes_type)
        insulin_status.append(insulin)
        readmission_statuses.append(readmission_status)
        medications.append(medication)

# Create a DataFrame from the collected data
data = {
    'Patient Name': names,
    'Age': ages,
    'Gender': genders,
    'Diabetes Type': diabetes_types,
    'Insulin Status': insulin_status,
    'Readmitted Status': readmission_statuses,
    'Medications': medications
}
df = pd.DataFrame(data)

# Save DataFrame to CSV file
df.to_csv('DataOutput2.csv', index=False)
