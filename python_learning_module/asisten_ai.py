import google.generativeai as genai
import os

# --- Konfigurasi Penting ---
# Cara paling aman adalah menyimpan API Key di environment variable.
# Di terminal, SEBELUM menjalankan file ini, ketik perintah:
#
# Untuk Windows (Command Prompt):
# set GOOGLE_API_KEY="KUNCI_API_ANDA_DISINI"
#
# Untuk macOS/Linux (Terminal):
# export GOOGLE_API_KEY="KUNCI_API_ANDA_DISINI"
#
# Ganti KUNCI_API_ANDA_DISINI dengan API Key yang kamu dapat dari Google AI Studio.

try:
    # Mengambil API key dari environment variable
    api_key = os.environ.get("GOOGLE_API_KEY")
    genai.configure(api_key=api_key)
except TypeError:
    print("\nERROR: API Key belum diatur!")
    print("Pastikan Anda sudah mengatur GOOGLE_API_KEY di terminal sebelum menjalankan program.")
    exit() # Keluar dari program jika key tidak ditemukan

# --- Pilih Model ---
# Kita akan pakai model Gemini 1.5 Flash yang terkenal cepat dan pintar
model = genai.GenerativeModel('gemini-1.5-flash')

# --- Program Utama Asisten Tanya Jawab ---
def jalankan_asisten():
    print("="*50)
    print("🤖 Halo! Saya Asisten Python dari Gemini 1.5 Flash.")
    print("   Ajukan pertanyaan apa saja tentang coding Python.")
    print("   Ketik 'keluar' untuk berhenti.")
    print("="*50)

    # Loop agar kita bisa terus bertanya tanpa henti
    while True:
        # Minta input dari pengguna
        pertanyaan = input("Pertanyaan Anda > ")

        # Cek jika pengguna ingin keluar
        if pertanyaan.lower() == 'keluar':
            print("\n🤖 Sampai jumpa lagi! Teruslah semangat belajar coding!")
            break

        # Kita berikan konteks tambahan agar jawaban Gemini lebih relevan
        prompt_lengkap = f"""
        Anda adalah seorang mentor pemrograman Python yang sangat ahli dan ramah.
        Jelaskan jawaban dengan cara yang mudah dimengerti untuk seorang siswa SMP.
        Jawab pertanyaan berikut: {pertanyaan}
        """

        try:
            print("\n🤖 Gemini sedang berpikir...")
            # Kirim pertanyaan (prompt) ke model Gemini
            response = model.generate_content(prompt_lengkap)

            # Cetak jawaban dari Gemini dengan rapi
            print("\nJawaban Gemini 🤖:")
            print("-" * 20)
            print(response.text)
            print("-" * 20, "\n")

        except Exception as e:
            # Penanganan jika terjadi error (misal: koneksi internet putus)
            print(f"\nOops, terjadi kesalahan: {e}")
            print("Silakan coba lagi.\n")

# --- Jalankan Program Asisten ---
if __name__ == "__main__":
    jalankan_asisten()
