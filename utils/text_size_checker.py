kana_chars = list(
    "あいうえおかきくけこさしすせそたちつてと"
    "なにぬねのはひふへほまみむめもやゆよらりるれろわをん"
    "アイウエオカキクケコサシスセソタチツテト"
    "ナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン"
)
kanji_chars = list(
    "日一国会人年大十二本中長出三時行見月分後前生五間上東四今金九入学高小六円子外八"
    "天気話女男車校水火木土曜書山川白黒赤青店社文電語読聞買食飲駅新古友名海空風花森"
    "犬猫鳥魚体心手足顔声星光夜朝昼雨雪春夏秋冬楽歌色家族"
)

# Font setup (replace if needed)
font_path = "/content/NotoSansCJK-Regular.ttc"
font_size = 60

def generate_image_preview(text):
    font = ImageFont.truetype(font_path, font_size)
    dummy_img = Image.new("RGB", (500, 500), "white")
    draw = ImageDraw.Draw(dummy_img)

    # Get actual text size
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Calculate 5% padding on each side
    pad_w = int(text_width * 0.05)
    pad_h = int(text_height * 0.05)

    img_width = text_width + 2 * pad_w
    img_height = text_height + 2 * pad_h

    # New image with just enough padding
    img = Image.new("RGB", (img_width, img_height), "white")
    draw = ImageDraw.Draw(img)

    # Center the text
    x = (img_width - text_width) / 2 - bbox[0]
    y = (img_height - text_height) / 2 - bbox[1]
    draw.text((x, y), text, font=font, fill="black")

    print(f"Text: '{text}'")
    print(f"Text size: {text_width}x{text_height}")
    print(f"Image size: {img_width}x{img_height}")
    display(img)

kanji_sample = random.sample(kanji_chars, 2)
generate_image_preview(kanji_sample[0] + kanji_sample[1])
generate_image_preview(random.choice(kana_chars))
