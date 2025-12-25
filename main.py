from utils import print_banner
from password_checker import check_password_strength
from password_generator import generate_password
from breach_checker import check_password_breach

def main():
    print_banner()
    while True:
        print("╔══════════════════════════════════════╗")
        print("║                Menu                  ║")
        print("╠══════════════════════════════════════╣")
        print("║  1. Password Generator               ║")
        print("║  2. Password Checker                 ║")
        print("║  3. Close                            ║")
        print("╚══════════════════════════════════════╝")
        choice = input("Enter your choice (1-3): ").strip()

        if choice == '1':
            try:
                length = int(input("Enter desired password length (minimum 8): "))
            except ValueError:
                length = 12
                print("Invalid input, using default length 12.")
            password = generate_password(length)
            print(f"\nGenerated Password: {password}")
            result = check_password_strength(password)
            print(f"Strength: {result['strength']} (Score: {result['score']}/4)")

        elif choice == '2':
            password = input("Enter a password to check its strength: ")
            result = check_password_strength(password)
            print(f"\nPassword Strength: {result['strength']} (Score: {result['score']}/4)")
            if result['feedback']:
                print("Suggestions to improve:")
                for item in result['feedback']:
                    print(f"- {item}")
            else:
                print("Your password is strong!")
            # Add breach check
            breach_count = check_password_breach(password)
            if breach_count > 0:
                print(f"\033[1;91mThis password has been found in {breach_count} known data breaches!\033[0m")
                print("\033[1;91mRecommendation: Change this password immediately.\033[0m")
            elif breach_count == 0:
                print("This password has not been found in any known data breaches.")
            else:
                print("Unable to check for breaches (no internet or API error).")

        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
