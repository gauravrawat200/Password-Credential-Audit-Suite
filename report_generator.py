from datetime import date

report = f"""
Assessment Date: {date.today()}

Total Passwords Tested: 4
Weak Passwords: 1
Medium Passwords: 2
Strong Passwords: 1

Recommendations:
- Use longer passwords
- Include uppercase letters
- Include numbers and symbols
"""

with open("Audit_Report.txt", "w") as f:
    f.write(report)

print("Audit_Report.txt generated successfully.")
