import random
import string

# Tampilkan ASCII cowsay
print(r"""
  ____________________
( hmm... let me think )
  --------------------
         o   ^__^
          o  (oo)\_______
             (__)\       )\/\
                 ||----w |
                 ||     ||
""")

# Nama file output
outfile = "cow.txt"

# Tanya input dari user
name = input("What name do you want to fill in the wordlist?: ").strip()
birth = input("Enter birthdate (example: 01012000): ").strip()
symbols = input("Enter symbol(s) you want to add (example: !@#): ").strip()
social = input("Favorite social media: ").strip()
game = input("Favorite game: ").strip()
artist = input("Favorite artist / idol: ").strip()
food = input("Favorite food: ").strip()
hobby = input("Hobby: ").strip()
color = input("Favorite color: ").strip()
pet = input("Pet name: ").strip()
birthplace = input("Birthplace / Hometown: ").strip()
movie = input("Favorite movie / series: ").strip()
fav_number = input("Favorite number: ").strip()

print("\nMembuat wordlist kecil... harap tunggu\n")

# Set untuk menghindari duplikat
wordlist = set()

# Fungsi variasi sederhana
def simple_variations(word):
    if not word:
        return set()
    return {
        word.lower(),
        word.upper(),
        word.capitalize()
    }

# Kumpulkan semua input
groups = {
    "name": simple_variations(name),
    "social": simple_variations(social),
    "game": simple_variations(game),
    "artist": simple_variations(artist),
    "food": simple_variations(food),
    "hobby": simple_variations(hobby),
    "color": simple_variations(color),
    "pet": simple_variations(pet),
    "birthplace": simple_variations(birthplace),
    "movie": simple_variations(movie),
    "fav_number": simple_variations(fav_number),
}

common_numbers = ["123", "99", "2024"]
common_symbols = symbols if symbols else "!@#"

# Masukkan dasar
for group in groups.values():
    wordlist.update(group)
if birth:
    wordlist.add(birth)

# Kombinasi sederhana
for group in groups.values():
    for w in group:
        if birth:
            wordlist.add(w + birth)
            wordlist.add(birth + w)
        for n in common_numbers:
            wordlist.add(w + n)
        for s in common_symbols:
            wordlist.add(w + s)

# Tambah sedikit random
chars = string.ascii_letters + string.digits + common_symbols
for _ in range(20):  # kecilin jumlah random
    choice = random.choice(
        [name, birth, social, game, artist, food, hobby, color, pet, birthplace, movie, fav_number, ""]
    )
    random_word = "".join(random.choice(chars) for _ in range(random.randint(6, 12)))
    if choice:
        pos = random.randint(0, len(random_word))
        random_word = random_word[:pos] + choice + random_word[pos:]
    wordlist.add(random_word)

# Simpan
with open(outfile, "w", encoding="utf-8") as f:
    for word in sorted(wordlist):
        f.write(word + "\n")

print(f"Wordlist kecil berhasil dibuat: {outfile}")
