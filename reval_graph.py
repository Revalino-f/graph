import os
from datetime import datetime, timedelta

# Huruf-huruf untuk tulisan "REVAL"
letters = {
    "R": [
        "11110",
        "10001",
        "10001",
        "11110",
        "10100",
        "10010",
        "10001"
    ],
    "E": [
        "11111",
        "10000",
        "10000",
        "11110",
        "10000",
        "10000",
        "11111"
    ],
    "V": [
        "10001",
        "10001",
        "10001",
        "10001",
        "10001",
        "01010",
        "00100"
    ],
    "A": [
        "01110",
        "10001",
        "10001",
        "11111",
        "10001",
        "10001",
        "10001"
    ],
    "L": [
        "10000",
        "10000",
        "10000",
        "10000",
        "10000",
        "10000",
        "11111"
    ]
}

# Susun huruf "REVAL" jadi satu grid horizontal
def build_message_grid(message):
    grid = []
    for row in range(7):
        line = ''
        for char in message.upper():
            if char in letters:
                line += letters[char][row] + '0'
        grid.append(line)
    return grid

# Buat grid tulisan
message = "REVAL"
msg_grid = build_message_grid(message)

# Tentukan posisi awal tulisan (di tengah)
total_weeks = 52
start_col = (total_weeks - len(msg_grid[0])) // 2  # agar tulisan di tengah

# Grid utama 7x52 (graph GitHub)
grid = [[1 for _ in range(52)] for _ in range(7)]  # isi semua dengan 1 (untuk full commit)

# Tempelkan tulisan "REVAL" ke tengah grid dengan angka 10 (biar lebih gelap)
for y in range(7):
    for x in range(len(msg_grid[0])):
        if msg_grid[y][x] == '1':
            grid[y][x + start_col] = 10

# Tanggal mulai: Minggu pertama di tahun ini
start_date = datetime(datetime.now().year, 1, 1)
while start_date.weekday() != 6:  # cari hari Minggu
    start_date -= timedelta(days=1)

# Commit sesuai grid
for x in range(52):  # minggu
    for y in range(7):  # hari
        commit_date = start_date + timedelta(weeks=x, days=y)
        for _ in range(grid[y][x]):
            with open('file.txt', 'a') as file:
                file.write(f"Commit on {commit_date}\n")
            os.system('git add .')
            os.system(f'git commit --date="{commit_date.isoformat()}" -m "Commit on {commit_date}"')

# Push ke GitHub
os.system('git push -u origin main')
