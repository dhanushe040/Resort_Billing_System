# Resort_Billing_System

🏨 Dhanush Resort – Python Billing System
A simple command-line billing system for a resort, built using Python and object-oriented programming. This project calculates total charges based on room rates and duration of stay, with a small surcharge for high-value bookings.

Features
  🔷 🛏️ Create a new booking with room number, customer name, charges, and days

  🔷 📋 Display customer and booking details

  🔷 💵 Compute total charges with conditional surcharge

  🔷 🧾 Generate a formatted bill with all details

  🔷 🧭 Menu-driven interface with input validation

Class Structure
python
class resort:
    def __init__(rno, name, charges, days)   # Initialize booking details
    def compute()                            # Calculate total amount with surcharge if applicable
    def getinfo()                            # Display basic booking info
    def dipinfo()                            # Display full bill with computed amount
Menu Options
1. Read → Enter booking details

2. Display → Show customer info

3. Total → Compute total charges

4. Bill → Display full bill

5. Exit → Close the program

Surcharge Logic
If total charges exceed ₹11,000, a 2% surcharge is added automatically.

How to Run
Run the script in any Python environment. Follow the prompts to manage resort bookings and generate bills.
