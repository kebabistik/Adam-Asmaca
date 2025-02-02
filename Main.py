import random

def get_random_word():
    words = ["python", "bilgisayar", "programlama", "kodlama", "yazılım"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def hangman():
    while True:
        word = get_random_word()
        guessed_letters = set()
        attempts = 6
        
        print("Adam Asmaca Oyununa Hoş Geldiniz!")
        
        while attempts > 0:
            print("\nKelime:", display_word(word, guessed_letters))
            guess = input("Bir harf tahmin edin: ").lower()
            
            if len(guess) != 1 or not guess.isalpha():
                print("Lütfen sadece bir harf girin.")
                continue
            
            if guess in guessed_letters:
                print("Bu harfi zaten tahmin ettiniz.")
                continue
            
            guessed_letters.add(guess)
            
            if guess not in word:
                attempts -= 1
                print(f"Yanlış tahmin! Kalan hak: {attempts}")
            
            if all(letter in guessed_letters for letter in word):
                print("Tebrikler! Kelimeyi doğru tahmin ettiniz:", word)
                break
        else:
            print("Maalesef kaybettiniz! Kelime:", word)
        
        again = input("Başka bir oyun oynamak ister misiniz? (evet/hayır): ").lower()
        if again != "evet":
            print("Oyun sonlandırıldı. Görüşmek üzere!")
            break

if __name__ == "__main__":
    hangman()
