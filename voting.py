import random  # For lottery in case of tie

# Voting App for Indian Government Simulation 🇮🇳

# Candidate data
candidates = {
    "Amit Sharma (BJP)": 0,
    "Priya Singh (INC)": 0,
    "Raj Patel (AAP)": 0,
    "Independent": 0
}

# Set to store normalized Voter IDs (no duplicates, fast lookup)
voted_voters = set()

# Function to display candidate list
def display_candidates():
    print("\nCandidates:")
    for i, candidate in enumerate(candidates.keys(), start=1):
        print(f"{i}. {candidate}")

# Function to normalize voter ID (remove spaces, make lowercase)
def normalize_voter_id(voter_id):
    return voter_id.strip().lower()

# Function to cast a vote
def vote():
    name = input("Enter your name: ").strip()
    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("❌ Invalid age input.\n")
        return

    voter_id_raw = input("Enter your Voter ID: ")
    voter_id = normalize_voter_id(voter_id_raw)

    if age < 18:
        print("❌ Sorry, you are not eligible to vote.\n")
        return

    if voter_id in voted_voters:
        print("⚠️ You have already voted. Duplicate voting is not allowed!\n")
        return

    display_candidates()
    try:
        choice = int(input("Enter the number of your selected candidate: "))
        if 1 <= choice <= len(candidates):
            selected_candidate = list(candidates.keys())[choice - 1]
            candidates[selected_candidate] += 1
            voted_voters.add(voter_id)
            print(f"\n✅ Thank you, {name}! Your vote for {selected_candidate} has been recorded.\n")
        else:
            print("❌ Invalid choice. Vote not recorded.\n")
    except ValueError:
        print("❌ Invalid input. Please enter a number.\n")

# Function to show results (Admin only)
def show_results():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    if username == "admin" and password == "1234":
        print("\n📊 ELECTION RESULTS 📊")
        for candidate, votes in candidates.items():
            print(f"{candidate}: {votes} votes")

        max_votes = max(candidates.values())
        winners = [candidate for candidate, votes in candidates.items() if votes == max_votes]

        if len(winners) == 1:
            print(f"\n🏆 Winner: {winners[0]}")
        else:
            print("\n🤝 It's a tie between:")
            for w in winners:
                print(f"🔷 {w}")
            print(f"Each has {max_votes} votes.")

            print("\n🎲 Conducting a random draw (as per Indian election rules)...")
            final_winner = random.choice(winners)
            print(f"🏁 By lottery, the elected winner is: {final_winner}")
    else:
        print("❌ Incorrect admin credentials.\n")

# Main Menu
def main():
    while True:
        print("\n===== DIGITAL VOTING SYSTEM 🇮🇳 =====")
        print("1. Cast Vote")
        print("2. View Results (Admin Only)")
        print("3. Exit")

        option = input("Choose an option (1/2/3): ").strip()

        if option == '1':
            vote()
        elif option == '2':
            show_results()
        elif option == '3':
            print("👋 Thank you for using the voting system. Jai Hind!")
            break
        else:
            print("❌ Invalid choice. Try again.")

# Run the app
main()
