import os
from PIL import Image, ImageDraw

# Buat folder icons jika belum ada
os.makedirs('static/icons', exist_ok=True)

# Ukuran icon yang dibutuhkan PWA
sizes = [72, 96, 128, 144, 152, 192, 384, 512]

print("Sedang membuat icon...")

for size in sizes:
    # Buat gambar background biru
    img = Image.new('RGB', (size, size), color=(30, 60, 114))
    draw = ImageDraw.Draw(img)
    
    # Gambar lingkaran putih di tengah
    margin = size // 5
    draw.ellipse([margin, margin, size - margin, size - margin], fill=(255, 255, 255))
    
    # Gambar icon "tools" sederhana (seperti obeng atau kunci)
    tool_w = size // 3
    tool_h = size // 4
    tool_x = (size - tool_w) // 2
    tool_y = (size - tool_h) // 2
    
    # Gambar persegi panjang
    draw.rectangle([tool_x, tool_y + tool_h//3, 
                    tool_x + tool_w, tool_y + tool_h], 
                   fill=(30, 60, 114))
    
    # Gambar lingkaran di atas
    circle_size = tool_h // 2
    circle_x = tool_x + tool_w // 2 - circle_size // 2
    circle_y = tool_y
    draw.ellipse([circle_x, circle_y, 
                  circle_x + circle_size, circle_y + circle_size], 
                 fill=(30, 60, 114))
    
    # Simpan file
    img.save(f'static/icons/icon-{size}x{size}.png')
    print(f'✅ Created icon-{size}x{size}.png')

print('\n🎉 Semua icon berhasil dibuat di folder static/icons/')