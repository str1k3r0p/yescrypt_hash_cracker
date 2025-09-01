#!/usr/bin/env python3
import sys
import crypt

def crack_yescrypt(unshadow_file, wordlist_file):
    # Load credentials from unshadowed file
    users = []
    with open(unshadow_file, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            parts = line.strip().split(":")
            if len(parts) > 1 and parts[1].startswith("$y$"):  # yescrypt marker
                username, hashval = parts[0], parts[1]
                users.append((username, hashval))

    if not users:
        print("[-] No yescrypt hashes found in file.")
        return

    print(f"[+] Loaded {len(users)} yescrypt hash(es)")

    # Load wordlist
    with open(wordlist_file, "r", encoding="utf-8", errors="ignore") as f:
        candidates = [w.strip() for w in f if w.strip()]

    print(f"[+] Loaded {len(candidates)} candidate passwords from wordlist")

    # Try cracking
    for username, target_hash in users:
        print(f"\n[*] Cracking password for user: {username}")
        for password in candidates:
            candidate_hash = crypt.crypt(password, target_hash)
            if candidate_hash == target_hash:
                print(f"[+] Found password for {username}: {password}")
                break
        else:
            print(f"[-] Password for {username} not found in wordlist")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <unshadow_file> <wordlist_file>")
        sys.exit(1)

    unshadow_file = sys.argv[1]
    wordlist_file = sys.argv[2]

    crack_yescrypt(unshadow_file, wordlist_file)
               
