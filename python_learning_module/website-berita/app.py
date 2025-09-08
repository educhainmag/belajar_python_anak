from flask import Flask, render_template

app = Flask(__name__)

# Anggap ini database berita kita (pakai List & Dictionary)
semua_berita = [
    {
        "id": 1,
        "judul": "Timnas Indonesia Menang di Laga Terakhir!",
        "penulis": "Jules Sport",
        "konten": "Timnas Indonesia berhasil memenangkan pertandingan terakhirnya dengan skor 2-0. Gol dicetak oleh striker andalan di babak kedua..."
    },
    {
        "id": 2,
        "judul": "Ditemukan Spesies Ikan Baru di Laut Dalam",
        "penulis": "Jules Sains",
        "konten": "Para peneliti mengumumkan penemuan spesies ikan baru yang dapat hidup di kedalaman lebih dari 8000 meter. Ikan ini memiliki kemampuan unik..."
    },
    {
        "id": 3,
        "judul": "Festival Kuliner Nusantara Kembali Digelar",
        "penulis": "Jules Food",
        "konten": "Setelah dua tahun vakum, Festival Kuliner Nusantara kembali digelar di ibu kota. Acara ini menampilkan lebih dari 100 jenis makanan khas dari seluruh Indonesia."
    }
]

# Halaman utama yang menampilkan semua judul berita
@app.route('/')
def halaman_utama():
    return render_template('index.html', berita_list=semua_berita)

# Halaman untuk membaca satu berita lengkap
@app.route('/berita/<int:id_berita>')
def detail_berita(id_berita):
    berita_ditemukan = None
    for berita in semua_berita:
        if berita['id'] == id_berita:
            berita_ditemukan = berita
            break
    return render_template('detail.html', berita=berita_ditemukan)

if __name__ == '__main__':
    app.run(debug=True)
