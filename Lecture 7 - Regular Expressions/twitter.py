import re

url = input("URL: ").strip()

# Matches the domain and captures everything after the trailing slash
matches = re.search(r"^https?://(?:www\.)?twitter\.com/([a-zA-Z0-9_]+)", url, re.IGNORECASE)

if matches:
    print(f"Username: {matches.group(1)}")
else:
    print("Invalid Twitter URL")
