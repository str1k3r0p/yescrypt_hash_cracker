# 🔑 Yescrypt Password Hash Cracker

This repository provides **two tools** (Python and Bash) for cracking **yescrypt password hashes** from Linux systems.  
Yescrypt is the default hashing algorithm in modern Linux distributions (e.g., Ubuntu, Debian).  

Both scripts require an **unshadowed file** (merged `/etc/passwd` + `/etc/shadow`) and a **wordlist** of candidate passwords.  

## 📂 Repository Contents

- **`yescrypt_cracker.py`** → Python-based yescrypt cracker using the built-in `crypt` library.  
- **`decrypt.sh`** → Bash-based yescrypt cracker using `mkpasswd` (from the `whois` package).  

## ⚡ Prerequisites

### For Python script:
- Python 3 installed on your system.

### For Bash script:
- Install `mkpasswd`:
  ```bash
  sudo apt update && sudo apt install whois -y

## 🛠️ How to Use

### 1. Generate an unshadow file

```bash
unshadow /etc/passwd /etc/shadow > unshadowed.txt
```
### 2. Run the Python script

```bash
python3 yescrypt_cracker.py unshadowed.txt wordlist.txt
```

**Sample output:**

[+] Loaded 2 yescrypt hash(es)
[+] Loaded 10 candidate passwords from wordlist

[*] Cracking password for user: root
[+] Found password for root: toor


### 3. Run the Bash script

```bash
chmod +x decrypt.sh
./decrypt.sh unshadowed.txt wordlist.txt

## Sample output:**

[*] Cracking password for user: kali
[+] Found password for kali: 1234

