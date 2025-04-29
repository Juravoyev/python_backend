import random

word_list = [
    "olma", "banan", "nok", "gilos", "behi", "uzum", "anor", "limon", "mango", "tarvuz",
    "qovun", "shaftoli", "o‘rik", "anjir", "avokado", "kivi", "mandarin", "apelsin", "ananas",
    "qulupnay", "malina",

    "it", "mushuk", "quyon", "sigir", "ot", "yo‘lbars", "sher", "maymun", "fil", "tulki",
    "bo‘ri", "quyon", "ayiqlar", "bug‘u", "burgut", "ilon", "toshbaqa", "baliq",

    "non", "guruch", "makaron", "tuxum", "sut", "go‘sht", "baliq", "pishloq", "yogurt",
    "qatiq", "shorva", "lag‘mon", "somsa", "palov", "shashlik", "choy", "qahva", "shirinlik",
    "asal", "murabbo",

    "qizil", "sariq", "yashil", "ko‘k", "havorang", "oq", "qora", "jigarrang", "pushti",
    "to‘q qizil", "to‘q ko‘k", "binafsha",

    "kompyuter", "monitor", "klaviatura", "sichqoncha", "dastur", "kod", "algoritm",
    "Python", "Java", "C++", "Linux", "Windows", "server", "tarmoq", "internet", "mobil",
    "telefon", "robot", "sun’iy intellekt",

    "yomg‘ir", "qor", "quyosh", "shamol", "momaqaldiroq", "muz", "daryo", "dengiz", "ko‘l",
    "tog‘", "o‘rmon", "cho‘l", "yomg‘ir", "suv", "havo"
]
word = random.choice(word_list)
guesses = set()
attempts = 7
while attempts > 0:
    display = "".join(letter if letter in guesses else "_" for letter in word)
    print(display)

    if "_" not in display:
        print("Tabriklaymiz! Siz so‘zni topdingiz. 🎉")
        break

    guess = input("Harfni kiriting: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("❌ Iltimos, faqat bitta harf kiriting!")
        continue

    if guess in guesses:
        print("⚠️ Bu harfni allaqachon kiritgansiz.")
        continue

    guesses.add(guess)

    if guess in word:
        print("✅ To‘g‘ri!")
    else:
        print("❌ Xato!")
        attempts -= 1

    print(f"Qolgan imkoniyatlar: {attempts}")

if attempts == 0:
    print(f"😢 Siz imkoniyatlaringizni tugatdingiz. To‘g‘ri javob: {word}")
