import random
print("🎲 Welcome to guess the number by Mr.Amin)
print("Chose number in  1 and 1000")
secert_number=random.randint(1,1000)
attemps=0
while True:
    guess=int(input(("👉 your number : ")))
    attemps+=1
    if guess<secert_number:
        print("⬆️ number ")
    elif guess>secert_number:
        print("⬇️ number")
    else:
        print(f"✅ مبروك! العدد هو {secret_number}")
        print(f"عدد المحاولات: {attempts}")
