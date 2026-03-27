import os
import platform
import subprocess
import sys

# ANSI color codes
class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BLACK = "\033[90m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
        
# Encryption Logic
def encrypt_string(plain_string):
    characters = list(plain_string)
    encrypted_characters = []
    
    for i in range(len(characters)):
        ascii_value = ord(characters[i])
        encrypted_ASCII = ascii_value + i
        encrypted_character = chr(encrypted_ASCII)
        encrypted_characters.append(encrypted_character)
        
    encrypted_string = "".join(encrypted_characters)
    return encrypted_string

# Decryption Logic
def decrypt_string(encrypted_string):
    characters = list(encrypted_string)
    decrypted_characters = []
    
    for i in range(len(characters)):
        ascii_value = ord(characters[i])
        decrypted_ASCII = ascii_value - i
        decrypted_character = chr(decrypted_ASCII)
        decrypted_characters.append(decrypted_character)
        
    decrypted_string = "".join(decrypted_characters)
    return decrypted_string

# region Banner
def print_banner():

    print(f"""
        ===========================================================================================================
        || {Colors.GREEN}{Colors.BOLD}[HACK THIS SITE] LEVEL 06 ENCRYPTION DECRYPTION TOOL{Colors.RESET}                                                  ||
        || {Colors.YELLOW}{Colors.DIM}Author: H3MERA{Colors.RESET}                                                                                        ||
        || {Colors.CYAN}{Colors.ITALIC}GitHub: www.linkedin.com/in/sadaham-abhisheka-4008963b5{Colors.RESET}                                               ||
        ||                                                                                                       ||
        || {Colors.MAGENTA}Description: A simple tool to decrypt and encrypt the string from Hack This Site Level 06.{Colors.RESET}            ||
        || {Colors.RED}Usage: Run the script and enter the encrypted string when prompted.{Colors.RESET}                                   ||
        ===========================================================================================================
      
        """)
# endregion

def clear_screen():
    command = 'cls' if os.name == 'nt' else 'clear'
    subprocess.run(command, shell=True)
    
def get_key():
    """Detects keypresses across different Operating Systems."""
    if os.name == 'nt':  # Windows
        import msvcrt
        key = msvcrt.getch()
        if key == b'\xe0':  # Prefix for arrow keys
            return msvcrt.getch()
        return key
    else:  # Linux / Mac
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
            # Linux arrow keys are 3-byte sequences: \x1b, [, and A/B/C/D
            if ch == '\x1b':
                ch = sys.stdin.read(2)
                return ch # Returns '[A' for up, '[B' for down
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    
def interactive_menu(options):
    selected = 0
    while True:
        clear_screen()
        print_banner()
        
        for i, option in enumerate(options):
            if i == selected:
                print(f"{Colors.GREEN}> {option}{Colors.RESET}")
            else:
                print(f"  {option}")
        
        key = get_key()

        # Handle Windows Keys
        if key == b'H' or key == '[A': # Up
            selected = (selected - 1) % len(options)
        elif key == b'P' or key == '[B': # Down
            selected = (selected + 1) % len(options)
        elif key == b'\r' or key == '\r' or key == '\n': # Enter
            return selected