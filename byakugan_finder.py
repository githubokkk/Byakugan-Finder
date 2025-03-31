import os
import requests
import concurrent.futures
from colorama import Fore, Style, init
import argparse

# Initialize colorama for colorful terminal output
init(autoreset=True)

# ASCII Art Banner
BANNER = f"""{Fore.BLUE}
 __  __   __  __   __  __   ______   ______    
/\ \_\ \ /\ \_\ \ /\ \/\ \ /\  ___\ /\  __ \   
\ \  __ \\ \____ \\ \ \_\ \\ \ \__ \\ \  __ \  
 \ \_\ \_\\/\_____\\ \_____\\ \_____\\ \_\ \_\ 
  \/_/\/_/ \/_____/ \/_____/ \/_____/ \/_/\/_/ 
                                            
----------------------------------------------------------
       👁️  BYAKUGAN FINDER: Admin Panel Scanner   
       Developer: Krupal Prajapati (https://github.com/Krupal1574)  
----------------------------------------------------------
"""

# Display Banner
os.system("cls" if os.name == "nt" else "clear")
print(Style.BRIGHT + BANNER)

# Argument parser for command-line usage
parser = argparse.ArgumentParser(description="Byakugan Finder: Admin Panel Scanner")
parser.add_argument("-u", "--url", required=True, help="Target base URL (e.g., https://example.com/)")
parser.add_argument("-w", "--wordlist", default="path.txt", help="Wordlist file (default: path.txt)")
parser.add_argument("-o", "--output", default="found_panels.txt", help="Output file to save results (default: found_panels.txt)")
args = parser.parse_args()

# Validate URL format
base_url = args.url.rstrip("/")
wordlist_file = args.wordlist
output_file = args.output

# Load paths from wordlist file
try:
    with open(wordlist_file, "r") as f:
        paths = [line.strip() for line in f.readlines()]
except FileNotFoundError:
    print(Fore.RED + f"\n [!] Wordlist file '{wordlist_file}' not found!")
    exit()

# Open output file once to save found results
found_urls = []

# Function to scan paths
def scan(path):
    try:
        url = f"{base_url}/{path}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        session = requests.Session()
        response = session.get(url, timeout=10, headers=headers)

        if response.status_code < 400:
            result = f"[+] Found: {url} (Status: {response.status_code})"
            print(Fore.GREEN + result)
            found_urls.append(result)
        else:
            print(Fore.RED + f"[-] Not Found: {url} (Status: {response.status_code})")
    except requests.RequestException:
        print(Fore.YELLOW + f"[!] Connection Failed: {url}")

# Run scanning with multithreading
print(Fore.CYAN + f"\n [*] Byakugan Activated... Scanning {len(paths)} paths!\n")

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(scan, paths)

# Save results to file
if found_urls:
    with open(output_file, "w") as f:
        f.write("\n".join(found_urls))
    print(Fore.BLUE + f"\n [+] Scan Complete! Results saved in {output_file}")
else:
    print(Fore.RED + "\n [!] No admin panels found! Try using a better wordlist.")
