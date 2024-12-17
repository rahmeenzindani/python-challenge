import csv

# Define file path
file_path = 'Resources/budget_data.csv'

# Initialize variables
total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
monthly_changes = []
dates = []
greatest_increase = {'date': '', 'amount': 0}
greatest_decrease = {'date': '', 'amount': 0}

# Read the CSV file
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip header row
    
    for row in reader:
        date = row[0]
        profit_loss = int(row[1])
        
        total_months += 1
        total_profit_loss += profit_loss
        
        # Calculate monthly change
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            monthly_changes.append(change)
            if change > greatest_increase['amount']:
                greatest_increase = {'date': date, 'amount': change}
            if change < greatest_decrease['amount']:
                greatest_decrease = {'date': date, 'amount': change}
        
        previous_profit_loss = profit_loss
        dates.append(date)

# Calculate average change
average_change = sum(monthly_changes) / len(monthly_changes)

# Prepare analysis output
analysis = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit_loss}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n"
)

# Print results to terminal
print(analysis)

# Export results to a text file
with open('analysis/financial_analysis.txt', 'w') as output_file:
    output_file.write(analysis)
