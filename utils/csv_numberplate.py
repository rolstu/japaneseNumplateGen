import random
import csv

# Full Hiragana + Katakana list
kana_chars = list(
    "あいうえおかきくけこさしすせそたちつてと"
    "なにぬねのはひふへほまみむめもやゆよらりるれろわをん"
    "アイウエオカキクケコサシスセソタチツテト"
    "ナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン"
)

# Expanded Kanji list
kanji_chars = list(
    "日一国会人年大十二本中長出三時行見月分後前生五間上東四今金九入学高小六円子外八"
    "天気話女男車校水火木土曜書山川白黒赤青店社文電語読聞買食飲駅新古友名海空風花森"
    "犬猫鳥魚体心手足顔声星光夜朝昼雨雪春夏秋冬楽歌色家族"
)

# Random generators
def random_kana():
    return random.choice(kana_chars)

def random_kanji_pair():
    return random.choice(kanji_chars) + random.choice(kanji_chars)

def random_two_digit():
    return str(random.randint(10, 99))

def random_three_digit():
    return str(random.randint(100, 999))

# Get user input
try:
    num_rows = int(input("Enter the number of rows to generate: "))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

# Write to CSV
with open("random_data.csv", "w", encoding="utf-8-sig", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["H", "TA", "TB", "TK", "TDD"])

    for _ in range(num_rows):
        row = [
            random_kana(),
            random_two_digit(),
            random_two_digit(),
            random_kanji_pair(),
            random_three_digit()
        ]
        writer.writerow(row)

print(f"File 'random_data.csv' with {num_rows} rows has been generated successfully!")
