class Account:
    def __init__(self, account_id: str, balance: float = 0.0) -> None:
        self.account_id = account_id
        self.balance = float(balance)

    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount
        return self.balance

    def get_balance(self) -> float:
        return self.balance

class Bank:
    def __init__(self, accounts: dict[str, Account] | None = None) -> None:
        self.accounts: dict[str, Account] = accounts or {}

    def create_account(self, account_id: str) -> None:
        if account_id in self.accounts:
            raise KeyError("Account with this ID already exists")
        self.accounts[account_id] = Account(account_id, 0.0)

    def deposit(self, account_id: str, amount: float) -> float:
        if account_id not in self.accounts:
            raise KeyError("Account not found")
        return self.accounts[account_id].deposit(amount)

    def get_balance(self, account_id: str) -> float:
        if account_id not in self.accounts:
            raise KeyError("Account not found")
        return self.accounts[account_id].get_balance()