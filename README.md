# Mutual Fund Portfolio Tracker (India)
A Python-based mutual fund portfolio tracker for Indian investors.
Tracks Gold & Silver mutual funds using official AMFI NAV data, supports multiple purchases (SIP / lumpsum), and is designed with clean OOP architecture for easy extension (XIRR, tests, UI).

# Important Links
Important link to get the NAV of each of the mutual fund 
https://portal.amfiindia.com/spages/NAVOpen.txt

# Data Format provided by the above link
119789;INF200K01RN3;INF200K01RO1;SBI Gold Fund - Direct Plan - Income Distribution cum Capital Withdrawal Option (IDCW);48.7711;30-Jan-2026


Mutual Fund : SBI Gold Fund - Direct Plan; Scheme code : 119789

# Mental Model of the app
```text
mf_portfolio_tracker/
│
├── app/
│   ├── __init__.py
│   └── main.py              # Application entry point (CLI)
│
├── core/
│   ├── __init__.py
│   ├── transaction.py       # Transaction entity
│   ├── mutual_fund.py       # MutualFund domain logic
│   └── portfolio.py         # Portfolio aggregation (future use)
│
├── services/
│   ├── __init__.py
│   ├── nav_fetcher.py       # AMFI NAV service
│   └── xirr.py              # XIRR calculation (placeholder)
│
├── storage/
│   ├── __init__.py
│   ├── repository.py        # JSON persistence layer
│   └── portfolio.json       # Stored investment data
│
├── tests/
│   ├── __init__.py
│   ├── test_transaction.py
│   ├── test_mutual_fund.py
│   └── test_xirr.py
│
├── requirements.txt
└── README.md
```

# New Features to be added 
1) Record multiple transactions at a time for any one mutual fund
2) Search mechanism for finding the mutual funds and then recording the transactions
3) Display the list of mutual funds invested and the total return
4) Create a HTML file to show all the transaction results
