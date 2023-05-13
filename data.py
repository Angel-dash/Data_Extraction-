# Import pandas library
import pandas as pd

# Define a function to extract information from a text file


def extract_info(file):
    # Create an empty dictionary to store the information
    info = {}
    # Open the file and read the lines
    with open(file, "r") as f:
        lines = f.readlines()
    # Loop through the lines and look for keywords
    for line in lines:
        # Split the line by spaces
        words = line.split()
        # Look for the name
        if words[0].isalpha() and words[1].isalpha():
            info["Name"] = words[0] + " " + words[1]
        # Look for the age
        if words[0].isdigit() and words[1] == "years":
            info["Age"] = words[0]
        # Look for the gender
        if words[0] == "Male" or words[0] == "Female":
            info["Gender"] = words[0]
        # Look for the insulin
        if words[0] == "Insulin":
            info["Insulin"] = words[2]
        # Look for the A1c result
        if words[0] == "A1c":
            info["A1c"] = words[3]
        # Look for the type of diabetes
        if "Diabetes" in line:
            info["Diabetes"] = line[line.index("Diabetes"):line.index(".")]
        # Look for the medication
        if "Patient is on diabetes meds" in line:
            info["Medication"] = "Yes"
        else:
            info["Medication"] = "No"
        # Look for the readmission time
        if "<30 days" in line:
            info["Readmission"] = "<30 days"
        elif ">30 days" in line:
            info["Readmission"] = ">30 days"
        else:
            info["Readmission"] = "Unknown"
    # Return the dictionary
    return info


# Create an empty list to store the information from multiple records in the file
data = []
# Open the file and read the lines
with open("new_data.txt", "r") as f:
    lines = f.readlines()
# Split the lines by empty lines to separate each record
records = "".join(lines).split("\n\n")
# Loop through the records and call the extract_info function on each record
for record in records:
    # Save the record as a temporary file
    with open("temp2.txt", "w") as f:
        f.write(record)
    # Append the information from the temporary file to the data list
    data.append(extract_info("temp2.txt"))
# Convert the list of dictionaries to a pandas dataframe
df = pd.DataFrame(data)
# Save the dataframe as a csv file
df.to_csv("output.3csv", index=False)
