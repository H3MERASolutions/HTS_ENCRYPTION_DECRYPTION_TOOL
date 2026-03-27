# Importing specific functions and classes from the local Components module
from Components import Colors as Colors
from Components import decrypt_string as decrypt_string
from Components import encrypt_string as encrypt_string
from Components import clear_screen as clear_screen
from Components import interactive_menu as interactive_menu
from Components import get_key as get_key

# Define the menu options for the interactive CLI
menu_items = ["Encrypt a string", "Decrypt a string", "Exit"]

# Initial call to the interactive menu to get the user's first choice
choice = interactive_menu(menu_items)

# Loop continues until the user selects "Exit" (index 2)
while choice != 2:
    
    # --- Choice 0: Encryption Mode ---
    if choice == 0:
        clear_screen()
        print(f"{Colors.GREEN}{Colors.BOLD}Encryption Mode{Colors.RESET}")
        
        user_input = input("\nEnter the string to encrypt: ")
        # Call the encryption logic from Components
        encrypted_string = encrypt_string(user_input)
        
        print(f"Encrypted string: {Colors.YELLOW}{encrypted_string}{Colors.RESET}")
        input("\nPress any key to continue...")
    
    # --- Choice 1: Decryption Mode ---
    elif choice == 1:
        clear_screen()
        print(f"{Colors.GREEN}{Colors.BOLD}Decryption Mode{Colors.RESET}")
        
        user_input = input("\nEnter the string to decrypt: ")
        # Call the decryption logic from Components
        decrypted_string = decrypt_string(user_input)
        
        print(f"Decrypted string: {Colors.YELLOW}{decrypted_string}{Colors.RESET}")
        input("\nPress any key to continue...")
    
    # Re-display the menu after an operation is complete
    choice = interactive_menu(menu_items)

# Final exit message once the loop terminates
print(f"{Colors.RED}{Colors.BOLD}Exiting the program. Goodbye!{Colors.RESET}")
