import random

def generate_otp():
    otp = ""
    for _ in range(6):
        otp += str(random.randint(0, 9))
    return otp

# Example usage
print("Your OTP is:", generate_otp())
