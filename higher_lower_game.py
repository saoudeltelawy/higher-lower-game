import random
from game_data import data
import art

# Main Logo
# print(art.main_logo)

# Initial setup
game_over = False
score = 0


def generate_random_account():
    return random.choice(data)


def generate_accounts_details_with_checking(first_account, second_account):
    """Ensure accounts are not the same and return account details."""
    # Check for matching accounts!
    while first_account == second_account:  # Ensure they are not the same
        second_account = generate_random_account()  # i.e. Reassign the second account
    # Then Extracting the details of the accounts
    # First Account Details:
    first_account_name = first_account[
        "name"
    ]  # Access the name key from the random dictionary,..etc.
    first_account_description = first_account["description"]
    first_account_country = first_account["country"]
    first_account_followers = first_account["follower_count"]

    # Second Account Details:
    second_account_name = second_account["name"]
    second_account_description = second_account["description"]
    second_account_country = second_account["country"]
    second_account_followers = second_account["follower_count"]
    return (
        first_account_name,
        first_account_description,
        first_account_country,
        first_account_followers,
        second_account_name,
        second_account_description,
        second_account_country,
        second_account_followers,
    )


def game_logic(
    first_account_name,
    first_account_description,
    first_account_country,
    first_account_followers,
    second_account_name,
    second_account_description,
    second_account_country,
    second_account_followers,
):
    """Core game logic for evaluating the user's choice."""
    global score, game_over

    # Display options
    print(
        f"Compare A: {first_account_name}, {first_account_description}, from {first_account_country}"
    )

    print(art.versus)

    print(
        f"Against B: {second_account_name}, {second_account_description}, from {second_account_country}"
    )

    # Get user input
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Determine correct answer
    correct_answer = "a" if first_account_followers > second_account_followers else "b"

    if user_choice == correct_answer:
        score += 1
        print(f"Correct! Your current score: {score}")
        return True  # User guessed correctly
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True
        return False  # User guessed incorrectly


# Game Start - Game started with two random accounts
first_account = (
    generate_random_account()
)  # Generate the first account randomly from the data [i.e. a dictionary]
second_account = generate_random_account()

while not game_over:
    (
        first_account_name,
        first_account_description,
        first_account_country,
        first_account_followers,
        second_account_name,
        second_account_description,
        second_account_country,
        second_account_followers,
    ) = generate_accounts_details_with_checking(first_account, second_account)

    # Play the game round
    if (
        game_logic(
            first_account_name,
            first_account_description,
            first_account_country,
            first_account_followers,
            second_account_name,
            second_account_description,
            second_account_country,
            second_account_followers,
        )
        is True
    ):
        # Update accounts
        first_account = second_account
        second_account = generate_random_account()
    else:
        game_over = True
