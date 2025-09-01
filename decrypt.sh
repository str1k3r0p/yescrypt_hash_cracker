!/bin/bash
# Usage: ./decrypt.sh <unshadow_file> <wordlist_file>
 
if [ $# -ne 2 ]; then
    echo "Usage: $0 <unshadow_file> <wordlist_file>"
    exit 1
fi
 
UNSHADOW=$1
WORDLIST=$2
 
if ! command -v mkpasswd &> /dev/null; then
    echo "[-] mkpasswd not found! Install with: apt install whois -y"
    exit 1
fi
 
# Read yescrypt hashes from unshadow file
while IFS=: read -r USER HASH REST; do
    if [[ $HASH == \$y\$* ]]; then
        echo "[*] Cracking password for user: $USER"
 
        while IFS= read -r PASS; do
            # Generate hash with same salt from mkpasswd
            GEN=$(mkpasswd -m yescrypt "$PASS" "$HASH" 2>/dev/null)
 
            if [[ "$GEN" == "$HASH" ]]; then
                echo "[+] Found password for $USER: $PASS"
                break
            fi
        done < "$WORDLIST"
 
    fi
done < "$UNSHADOW"
