# Python Pygame GamePack

Kumpulan game sederhana berbasis Python menggunakan library Pygame. Proyek ini dibuat untuk mempelajari konsep Object-Oriented Programming (OOP), pewarisan (inheritance), abstract class, collision detection, dan pengembangan game 2D sederhana.

## 🎮 Daftar Game

### 1. Space Defender

Game shooter sederhana di mana pemain mengendalikan pesawat luar angkasa dan menembak musuh yang datang dari atas.

#### Fitur
- Kontrol pesawat menggunakan keyboard
- Sistem peluru (shooting)
- Musuh muncul secara acak
- Sistem skor
- Sistem nyawa (lives)
- Deteksi tabrakan peluru dan musuh
- Menggunakan gambar sprite pesawat

#### Kontrol
| Tombol | Fungsi |
|---------|---------|
| ← | Bergerak ke kiri |
| → | Bergerak ke kanan |
| Space | Menembak |

---

### 2. Treasure Collector

Game pengumpulan koin dengan rintangan yang terus bertambah seiring kenaikan level.

#### Fitur
- Gerakan 4 arah
- Pengumpulan koin
- Sistem skor
- Sistem level
- Trap/rintangan bergerak
- Tingkat kesulitan meningkat setiap level
- Implementasi Abstract Base Class (ABC)

#### Kontrol
| Tombol | Fungsi |
|---------|---------|
| ↑ | Bergerak ke atas |
| ↓ | Bergerak ke bawah |
| ← | Bergerak ke kiri |
| → | Bergerak ke kanan |

---

## 📂 Struktur Project

```text
project/
│
├── space_defender_232102014.py
├── treasure_collector_232102014.py
│
├── pesawat.png
├── pesawatmusuh1.png
├── pesawatmusuh2.png
│
└── README.md
```

---

## ⚙️ Instalasi

### 1. Clone Repository

```bash
git clone https://github.com/USERNAME/python-pygame-gamepack.git
```

### 2. Masuk ke Folder Project

```bash
cd python-pygame-gamepack
```

### 3. Install Pygame

```bash
pip install pygame
```

### 4. Jalankan Game

#### Space Defender

```bash
python space_defender_232102014.py
```

#### Treasure Collector

```bash
python treasure_collector_232102014.py
```

---

## 🧠 Konsep OOP yang Digunakan

### Space Defender
- Class dan Object
- Inheritance
- Encapsulation
- Collision Detection

### Treasure Collector
- Abstract Class (ABC)
- Inheritance
- Polymorphism
- Encapsulation
- Collision Detection

---

## 🛠️ Teknologi

- Python 3
- Pygame

---

## 👨‍💻 Author

Amar Ma'ruf  
NIM: 232102014

---

## 📜 License

Project ini dibuat untuk keperluan pembelajaran dan pengembangan keterampilan pemrograman Python.
