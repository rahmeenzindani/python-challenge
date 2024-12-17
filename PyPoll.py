import csv

# Define file path
file_path = 'Resources/election_data.csv'

# Initialize variables
total_votes = 0
candidates = {}
winner = {'candidate': '', 'votes': 0}

# Read the CSV file
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip header row
    
    for row in reader:
        candidate = row[2]
        total_votes += 1
        if candidate not in candidates:
            candidates[candidate] = 0
        candidates[candidate] += 1

# Calculate results
analysis = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)

# Calculate percentage of votes and find the winner
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    analysis += f"{candidate}: {percentage:.3f}% ({votes})\n"
    if votes > winner['votes']:
        winner = {'candidate': candidate, 'votes': votes}

# Add winner to the analysis
analysis += (
    f"-------------------------\n"
    f"Winner: {winner['candidate']}\n"
    f"-------------------------\n"
)

# Print results to terminal
print(analysis)

# Export results to a text file
with open('analysis/election_results.txt', 'w') as output_file:
    output_file.write(analysis)
