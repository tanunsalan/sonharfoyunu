word_list = {
    "A": ["Armut", "Altın", "Aslan", "Avize", "Atkı", "Acemi", "Anı", "Ağaç", "Araba", "Arena"],
    "B": ["Balık", "Bilgi", "Baba", "Bayan", "Baykuş", "Bulut", "Buz", "Bağ", "Bahar", "Barut"],
    "C": ["Cevap", "Cemre", "Can", "Ceviz", "Cennet", "Cihan", "Cılız", "Canavar", "Cüzdan", "Cilve"],
    "Ç": ["Çilek", "Çiçek", "Çadır", "Çanak", "Çarşı", "Çekiç", "Çocuk", "Çuval", "Çizgi", "Çanta"],
    "D": ["Deniz", "Dere", "Dut", "Duman", "Diken", "Dağ", "Dans", "Dil", "Deri", "Dünya"],
    "E": ["Elma", "Ekmek", "Erik", "Eşya", "Elektrik", "Eczane", "Etek", "Ev", "Ekim", "Ekşi"],
    "F": ["Fener", "Fare", "Fidan", "Film", "Fırtına", "Fidanlık", "Fenerbahçe", "Fiyat", "Fincan", "Fırın"],
    "G": ["Gemi", "Göz", "Gül", "Gök", "Gece", "Güven", "Gazete", "Gelin", "Gitar", "Güzel"],
    "H": ["Hayal", "Harita", "Horoz", "Hava", "Hayvan", "Halı", "Halat", "Haber", "Hediye", "Hız"],
    "I": ["Islak", "Isırgan", "Isı", "Islık", "Israr", "Ispanak", "Iskart", "Isı ölçer", "Isıl", "Isırık"],
    "İ": ["İnsan", "İnci", "İnternet", "İnşaat", "İnek", "İğne", "İhtiyaç", "İkna", "İman", "İklim"],
    "K": ["Kavun", "Kitap", "Kalem", "Koyun", "Kazan", "Kadın", "Kağıt", "Kekik", "Kanat", "Konak"],
    "L": ["Limon", "Lale", "Leke", "Lamba", "Lira", "Levha", "Leylek", "Lacivert", "Lokum", "Lüfer"],
    "M": ["Muz", "Masa", "Mantar", "Misafir", "Mektup", "Meyve", "Motor", "Mum", "Martı", "Mont"],
    "N": ["Nar", "Nane", "Nehir", "Nakit", "Nisan", "Nota", "Naylon", "Nimet", "Nohut", "Niyaz"],
    "O": ["Orman", "Otobüs", "Okul", "Oyun", "Oyuncak", "Olta", "Onur", "Oda", "Orta", "Organ"],
    "P": ["Palto", "Patlıcan", "Pamuk", "Portakal", "Patates", "Polis", "Priz", "Pilot", "Papatya", "Palamut"],
    "R": ["Renk", "Rehber", "Rüzgar", "Rakı", "Rota", "Resim", "Randevu", "Ray", "Rom", "Ruj"],
    "S": ["Sandal", "Sebze", "Sıcak", "Salon", "Su", "Sarı", "Simit", "Saat", "Sazan", "Şarkı"],
    "Ş": ["Şemsiye", "Şeker", "Şarap", "Şehir", "Şarkıcı", "Şapka", "Şelale", "Şans", "Şişe", "Şemsiye"],
    "T": ["Tavuk", "Taş", "Telefon", "Tarih", "Tatlı", "Tarla", "Tepsi", "Tiyatro", "Tütün", "Tren"],
    "U": ["Uçak", "Uçurum", "Uyku", "Umut", "Usta", "Uzay", "Uygun", "Un", "Umutsuz", "Uğur"],
    "Ü": ["Üzüm", "Üzengi", "Üsküf", "Ücret", "Ünlü", "Üretim", "Ütü", "Ülke", "Üniforma", "Üstün"],
    "V": ["Vazo", "Vadi", "Varil", "Vatan", "Villa", "Vahşi", "Vapur", "Vites", "Volkan", "Vergi"],
    "Y": ["Yelken", "Yumurta", "Yastık", "Yol", "Yengeç", "Yıldız", "Yüzük", "Yemek", "Yayla", "Yorgan"],
    "Z": ["Zeytin", "Zarf", "Zengin", "Zebra", "Zaman", "Zor", "Zincir", "Zar", "Ziyafet", "Zula"],
}
import random
import time

written_words = []  # Tüm yazılan kelimeleri saklar
rounds = 20  # Oyuncu ve yapay zeka için maksimum tur sayısı

def ai_generate_word(last_char):
    """Yapay zeka için kelime üretimi."""
    if last_char.upper() in word_list:
        possible_words = word_list[last_char.upper()]
        possible_words = [word for word in possible_words if word not in written_words]
        return random.choice(possible_words) if possible_words else None
    return None

def player_input(last_char):
    """Oyuncu girişini yönetir."""
    start_time = time.time()
    user_word = input(f"'{last_char}' harfiyle başlayan bir kelime yaz: ").strip().lower()
    if time.time() - start_time > 6:
        print("Çok geç kaldın! 😢")
        return None
    if user_word in written_words:
        print("Bu kelime daha önce söylendi!")
        return None
    if user_word.startswith(last_char):
        return user_word
    else:
        print("Yanlış harfle başladın!")
        return None

print("Son Harf oyununa hoş geldin! 🎮")
first_word = random.choice(word_list["A"])  # İlk kelimeyi başlat
print(f"Yapay zeka başlıyor: {first_word}")
written_words.append(first_word)

for turn in range(1, rounds + 1):
    last_char = written_words[-1][-1]  # Son kelimenin son harfi

    print(f"\n{turn}. TUR - Senin sıran!")
    player_word = player_input(last_char)
    if player_word:
        written_words.append(player_word)
    else:
        print("Maalesef oyunu kaybettin!")
        break

    last_char = written_words[-1][-1]
    ai_word = ai_generate_word(last_char)
    if ai_word:
        print(f"Yapay Zeka: {ai_word}")
        written_words.append(ai_word)
    else:
        print("Yapay zeka cevap veremedi, sen kazandın!")
        break

print("\nOyun bitti! Şimdi sürpriz zamanı! 🎉")
print("Tüm kelimeleri doğru sırayla hatırlayabilir misin?")
time.sleep(2)
print("Hazır mısın? Kelimeleri yazmaya başla!")

score = 0
for i, word in enumerate(written_words):
    user_input = input(f"{i+1}. kelime: ").strip().lower()
    if user_input == word.lower():
        score += 1

print(f"\nTebrikler! {score}/{len(written_words)} kelimeyi doğru hatırladın! 👏")
print
