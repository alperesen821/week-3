secretNum = 5
attempts = 0
while True:
    guess = int(input("Tahmin: "))
    attempts += 1
    if guess == secretNum:
        print("Tebrikler! Doğru tahmin ettiniz.")
        break
    elif guess < secretNum:
        print("Daha yüksek bir sayı tahmin edin.")
    else:
        print("Daha düşük bir sayı tahmin edin.")
    if attempts >= 5:
        print("Tahmin hakkınız doldu. Doğru sayı:", secretNum)
        break