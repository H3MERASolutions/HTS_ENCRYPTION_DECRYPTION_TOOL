HTS Level 06 Encryption/Decryption Tool
A lightweight, interactive Python utility designed to solve the Hack This Site (Level 06) challenge. This tool automates the process of shifting ASCII values based on character position to encrypt or decrypt strings instantly.

🚀 Features
Interactive CLI Menu: Navigate through options using your arrow keys.

Cross-Platform Support: Works on Windows, Linux, and macOS.

Real-time Logic: Uses the specific HTS Level 06 algorithm (incremental ASCII shifting).

Colorized Output: Clean, easy-to-read terminal interface with ANSI colors.

🧠 The Logic
The cipher works by shifting each character's ASCII value by its index in the string:

Encryption: Encrypted_Char = Original_Char + Index

Decryption: Original_Char = Encrypted_Char - Index

🛠️ Installation & Usage
Clone the repository:

Bash
git clone https://github.com/your-username/HTS_ENCRYPTION_DECRYPTION_TOOL.git
cd HTS_ENCRYPTION_DECRYPTION_TOOL
Run the tool:
Make sure you have Python 3 installed.

Bash
python HTSDecryptor.py
📂 Project Structure
HTSDecryptor.py: The main entry point of the application.

components.py: Contains the core encryption/decryption logic, UI components, and cross-platform input handling.

👤 Author
H3MERA

LinkedIn: Sadaham Abhisheka
