class User:
    def __init__ (self, first, last, email, password, login_attempts = 0):
        self.first = first
        self.last = last
        self.email = email
        self.password = password
        self.attempts = login_attempts

        self.fullName = first+" "+last

    def describe_user (self):
        print(f"Your user info: {self.first},{self.last},{self.email},{self.password}")

    def greet_user (self):
        print(f"Welcome! {self.fullName}")

    def increment_login_attemps(self):
        self.attempts += 1
    
    def reset_login_attemps(self):
        self.attempts = 0


alice = User("Alice","Perego","aliceperego@icloud.com","12345678")

alice.describe_user()
alice.greet_user()

for i in range(1, 5):
    alice.increment_login_attemps()

print(alice.attempts)

alice.reset_login_attemps()

print(alice.attempts)