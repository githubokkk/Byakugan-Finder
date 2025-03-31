👁️ Byakugan Finder - Admin Panel Scanner
"The Byakugan sees through all… even hidden admin panels!"


🌀 About
Byakugan Finder is a fast and efficient admin panel scanner that helps penetration testers and ethical hackers discover hidden admin login pages on websites. It uses multithreading to speed up scanning and is inspired by the Byakugan ability from Naruto! 🌪️

⚡ Features
✔️ Multithreading for fast scanning
✔️ Custom wordlists for better accuracy
✔️ Saves results to a file automatically
✔️ User-friendly and beginner-friendly
✔️ Works on Windows, Linux, and macOS

📥 Installation
1️⃣ Clone the Repository

sh
Copy
Edit
git clone https://github.com/Krupal1574/Byakugan-Finder.git
cd Byakugan-Finder
2️⃣ Install Dependencies

sh
Copy
Edit
pip install -r requirements.txt
🚀 Usage
Basic Scan
sh
Copy
Edit
python byakugan_finder.py -u "https://example.com/"
Using a Custom Wordlist
sh
Copy
Edit
python byakugan_finder.py -u "https://example.com/" -w "my_wordlist.txt"
Save Results to a File
sh
Copy
Edit
python byakugan_finder.py -u "https://example.com/" -o "admin_results.txt"
🎯 Example Output
sh
Copy
Edit
[*] Byakugan Activated... Scanning 500 paths!

[+] Found: https://example.com/admin (Status: 200)
[+] Found: https://example.com/wp-admin (Status: 200)
[-] Not Found: https://example.com/administrator (Status: 404)
[-] Not Found: https://example.com/cpanel (Status: 403)

[+] Scan Complete! Results saved in found_panels.txt
🔗 Wordlists for Better Results
If you need stronger wordlists, check these out:

SecLists Admin Panels: 🔗 GitHub Link

FuzzDB Admin Paths: 🔗 GitHub Link

🛡️ Legal Disclaimer
⚠️ Use this tool only for ethical hacking and security testing on websites you have permission to test.
I am not responsible for any misuse or illegal activities using this script.

👤 Developer
👨‍💻 Krupal Prajapati
🔗 GitHub: @Krupal1574

💙 If you found this tool useful, star the repo ⭐ and follow for more cool projects! 🚀

