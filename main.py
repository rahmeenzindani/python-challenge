import csv

# Function for PyBank Challenge (Financial Analysis)
def pybank_analysis():
    file_path = 'Resources/budget_data.csv'

    # Initialize variables for PyBank
    total_months = 0
    total_profit_loss = 0
    previous_profit_loss = 0
    monthly_changes = []
    dates = []
    greatest_increase = {'date': '', 'amount': 0}
    greatest_decrease = {'date': '', 'amount': 0}

    # Read the CSV file for PyBank
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip header row
        
        for row in reader:
            date = row[0]
            profit_loss = int(row[1])
            
            total_months += 1
            total_profit_loss += profit_loss
            
            # Calculate monthly change (starting from second month)
            if total_months > 1:
                change = profit_loss - previous_profit_loss
                monthly_changes.append(change)
                
                # Update greatest increase and decrease in profits
                if change > greatest_increase['amount']:
                    greatest_increase = {'date': date, 'amount': change}
                if change < greatest_decrease['amount']:
                    greatest_decrease = {'date': date, 'amount': change}
            
            previous_profit_loss = profit_loss
            dates.append(date)

    # Calculate average change
    average_change = sum(monthly_changes) / len(monthly_changes)

    # Prepare analysis output for PyBank
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

    # Export results to a text file for PyBank
    with open('analysis/financial_analysis.txt', 'w') as output_file:
        output_file.write(analysis)


# Function for PyPoll Challenge (Election Analysis)
def pypoll_analysis():
    file_path = 'Resources/election_data.csv'

    # Initialize variables for PyPoll
    total_votes = 0
    candidates = {}
    winner = {'candidate': '', 'votes': 0}

    # Read the CSV file for PyPoll
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip header row
        
        for row in reader:
            candidate = row[2]
            total_votes += 1
            if candidate not in candidates:
                candidates[candidate] = 0
            candidates[candidate] += 1

    # Prepare analysis for PyPoll
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

    # Export results to a text file for PyPoll
    with open('analysis/election_results.txt', 'w') as output_file:
        output_file.write(analysis)


# Main function to run both PyBank and PyPoll analyses
def main():
    print("Running PyBank Analysis...")
    pybank_analysis()  # Call the function for PyBank analysis
    
    print("\nRunning PyPoll Analysis...")
    pypoll_analysis()  # Call the function for PyPoll analysis


if __name__ == "__main__":
    main()  # Run the main function
