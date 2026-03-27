from Components import Colors as Colors
from Components import decrypt_string as decrypt_string
from Components import encrypt_string as encrypt_string
from Components import clear_screen as clear_screen
from Components import interactive_menu as interactive_menu
from Components import get_key as get_key

menu_items = ["Encrypt a string", "Decrypt a string", "Exit"]
choice = interactive_menu(menu_items)

while choice != 2:
    
    if choice == 0:
        clear_screen()
        print(f"{Colors.GREEN}{Colors.BOLD}Encryption Mode{Colors.RESET}")
        user_input = input("\nEnter the string to encrypt: ")
        encrypted_string = encrypt_string(user_input)
        print(f"Encrypted string: {Colors.YELLOW}{encrypted_string}{Colors.RESET}")
        input("\nPress any key to continue...")
    
    elif choice == 1:
        clear_screen()
        print(f"{Colors.GREEN}{Colors.BOLD}Decryption Mode{Colors.RESET}")
        user_input = input("\nEnter the string to decrypt: ")
        decrypted_string = decrypt_string(user_input)
        print(f"Decrypted string: {Colors.YELLOW}{decrypted_string}{Colors.RESET}")
        input("\nPress any key to continue...")
    
    choice = interactive_menu(menu_items)

print(f"{Colors.RED}{Colors.BOLD}Exiting the program. Goodbye!{Colors.RESET}")
