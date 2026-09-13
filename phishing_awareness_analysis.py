# Take message input
message = input("Enter the email or message to analyze: ")

# Convert message to lowercase
text = message.lower()

# Risk score
score = 0

# Store detected red flags
red_flags = []

# Suspicious keywords
suspicious_keywords = [
    "urgent",
    "immediately",
    "verify your account",
    "account locked",
    "password expires",
    "click here",
    "confirm your identity",
    "update billing",
    "wire transfer",
    "confidential",
    "mfa",
    "payment failed",
    "security alert"
]

# Check suspicious keywords
for keyword in suspicious_keywords:
    if keyword in text:
        score = score + 1
        red_flags.append("Suspicious keyword: " + keyword)

# Check for suspicious links
if "http://" in text or "https://" in text or "www." in text:
    score = score + 2
    red_flags.append("Suspicious link found")

# Check for requests for sensitive information
sensitive_words = [
    "password",
    "otp",
    "mfa code",
    "credit card",
    "bank details",
    "payment details"
]

for word in sensitive_words:
    if word in text:
        score = score + 2
        red_flags.append("Request for sensitive information: " + word)

# Check for urgent requests
if "urgent" in text or "immediately" in text:
    score = score + 2
    red_flags.append("Urgent action requested")

# Check for authority-related messages
authority_words = [
    "ceo",
    "manager",
    "director",
    "it support",
    "security team",
    "administrator"
]

for word in authority_words:
    if word in text:
        score = score + 1
        red_flags.append("Possible authority impersonation: " + word)

# Check for dangerous attachments
dangerous_extensions = [
    ".exe",
    ".scr",
    ".js",
    ".iso",
    ".html"
]

for extension in dangerous_extensions:
    if extension in text:
        score = score + 2
        red_flags.append("Potentially dangerous attachment: " + extension)

# Display analysis
print("\n--- Phishing Analysis Report ---")

if score == 0:
    print("Risk Level: Safe")
    print("Action: Close")

elif score <= 4:
    print("Risk Level: Suspicious")
    print("Action: Warn User")

else:
    print("Risk Level: Malicious")
    print("Action: Block & Escalate")

# Display detected red flags
if len(red_flags) > 0:
    print("\nRed Flags Found:")

    for flag in red_flags:
        print("- " + flag)

else:
    print("\nNo obvious red flags detected.")

# Display risk score
print("\nRisk Score:", score)

# Final safety reminder
print("\nRecommendation: Pause -> Verify -> Report")