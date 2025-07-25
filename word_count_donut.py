import csv
import matplotlib.pyplot as plt

def main():
    # Input word from user (case-sensitive, as in the file)
    target_word = input("Enter the Greek word to count: ").strip()
    filename = '01-matthew.csv'
    
    total_words = 0
    target_count = 0

    # Read and process the CSV file
    with open(filename, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            word = row['word']
            total_words += 1
            if word == target_word:
                target_count += 1

    # Check for zero occurrences
    if total_words == 0:
        print("No words found in the file.")
        return

    # Prepare data for donut chart
    other_count = total_words - target_count
    data = [target_count, other_count]
    labels = [f"{target_word} ({target_count})", f"Other Words ({other_count})"]
    colors = ['#ff9999','#66b3ff']

    # Donut chart
    fig, ax = plt.subplots()
    wedges, texts, autotexts = ax.pie(
        data, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, pctdistance=0.85
    )

    # Draw center circle for donut shape
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig.gca().add_artist(centre_circle)

    plt.title(f"Proportion of '{target_word}' in {filename}\nTotal words: {total_words}")
    plt.tight_layout()
    plt.show()

    print(f"\n'{target_word}' occurs {target_count} times out of {total_words} words.")

if __name__ == "__main__":
    main()