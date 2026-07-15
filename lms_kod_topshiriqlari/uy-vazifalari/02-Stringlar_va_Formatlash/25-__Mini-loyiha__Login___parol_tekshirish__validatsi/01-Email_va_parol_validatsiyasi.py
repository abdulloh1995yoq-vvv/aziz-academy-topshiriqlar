email = input().strip()
print("@" in email and "." in email.split("@")[-1] and email.islower())