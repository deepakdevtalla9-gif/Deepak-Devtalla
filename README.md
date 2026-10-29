# Python OOP Banking System

A beginner-friendly command-line banking project built with Python and Object-Oriented Programming (OOP).

## Features
- Create savings accounts
- Check current balance
- Deposit money
- Withdraw money with insufficient-balance checks
- View transaction history with timestamps
- Validate account names, amounts, and duplicate account numbers
- Demonstrate classes, objects, encapsulation, inheritance, and methods

## Requirements
- Python 3.9 or later
- No third-party packages required

## Run the project
1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

```bash
python banking_system.py
```

On some Windows systems, use `py banking_system.py`.

## How to use
Choose an option from the menu. Create an account first, then use its account number to check balance, deposit, withdraw, or view transaction history.

## OOP concepts used
- **Class and object:** `BankAccount`, `SavingsAccount`, `BankingSystem`, and `Transaction`
- **Encapsulation:** the balance is stored in the private attribute `__balance`
- **Inheritance:** `SavingsAccount` inherits from `BankAccount`
- **Abstraction:** the menu gives users simple actions without requiring them to manage internal transaction records
- **Methods:** `deposit()`, `withdraw()`, `show_transactions()`, and `create_account()`

## Project structure
```text
Python_OOP_Banking_System/
├── banking_system.py
├── README.md
├── class_diagram.mmd
├── docs/
│   └── design.md
└── linkedin_post.txt
```

## Important note
This is an educational demonstration, not real banking software. It does not use a database, authentication, encryption, or real payment services. Account data is lost when the program exits.
