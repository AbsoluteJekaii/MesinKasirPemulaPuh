# Mesin Kasir Pemula Puh

Proyek ini adalah aplikasi **Mesin Kasir Sederhana** berbasis web yang dibangun menggunakan Flask. Aplikasi ini dirancang untuk membantu mengelola data produk, transaksi, dan pengguna dengan fitur CRUD (Create, Read, Update, Delete).

## Fitur Utama
1. **Manajemen Produk** (Admin)
   - Tambah produk baru.
   - Melihat daftar produk.
   - Mengedit produk.
   - Menghapus produk.
   
2. **Manajemen Transaksi** (Kasir)
   - Melakukan pembayaran dan menambah produk ke keranjang.
   - Melihat riwayat transaksi.
   
3. **Manajemen Pengguna**
   - Sistem login dengan peran **Admin** dan **Kasir**.
   - Logout.

4. **Keranjang Belanja** (Kasir)
   - Menyimpan item yang akan dibeli sebelum pembayaran selesai.

---

## Teknologi yang Digunakan

### Frontend:
- **HTML**
- **CSS**

### Backend:
- **Flask** (Python Web Framework)

### Database:
- **MySQL**

### Server:
- Localhost menggunakan **XAMPP**.

---

## Instalasi dan Persiapan

### Prasyarat
Pastikan perangkat Anda sudah memiliki:
- **Python 3.x**
- **XAMPP** (untuk menjalankan MySQL dan Apache)
- **Git** (opsional, untuk meng-clone repository)

### Langkah-langkah
1. **Clone Repository**
   ```
   git clone https://github.com/AbsoluteJekaii/MesinKasirPemulaPuh.git
   ```

2. **Install Dependencies**
   ```
   cd MesinKasirPemulaPuh
   pip install -r requirements.txt
   ```

3. **Buat Database**
   - Jalankan XAMPP, aktifkan **MySQL**.
   - Buka **phpMyAdmin** di browser Anda (biasanya http://localhost/phpmyadmin).
   - Jalankan query berikut untuk membuat database:
     ```sql
     CREATE DATABASE kasir_sederhana;
     ```
   - Import file `kasir_sederhana.sql` ke dalam database **kasir_sederhana**.

4. **Jalankan Aplikasi**
   ```
   python app.py
   ```
   Aplikasi akan berjalan di **http://127.0.0.1:5000**.

---

## Login Akun
Gunakan kredensial berikut untuk mencoba aplikasi:

- **Admin:**
  - Username: `admin`
  - Password: `admin123`

- **Kasir:**
  - Username: `kasir`
  - Password: `kasir123`

---

## Fitur CRUD
Berikut adalah bagian CRUD dalam aplikasi ini:

### **Create**
- Menambah produk baru di halaman **Add Product** (`/add_product`).
- Menambah transaksi di halaman **Payment** (`/payment`).

### **Read**
- Melihat daftar produk di halaman **Products** (`/products`).
- Melihat riwayat transaksi di halaman **Transaction History** (`/transaction_history`).

### **Update**
- Mengedit produk di halaman **Edit Product** (`/edit_product/<id>`).

### **Delete**
- Menghapus produk di halaman **Products** dengan tombol hapus.
- Menghapus transaksi di halaman **Transaction History** (khusus Admin).

---

## Catatan Tambahan
1. Pastikan Anda telah mengaktifkan MySQL di XAMPP sebelum menjalankan aplikasi.
2. Pastikan semua dependensi telah diinstal menggunakan `pip install -r requirements.txt`.
3. Jangan lupa untuk mengimport file `kasir_sederhana.sql` ke dalam database.
4. Anda dapat mengubah koneksi database di file `app.py` jika diperlukan:
   ```python
   connection = pymysql.connect(
       host='localhost',
       user='root',
       password='',  # Ubah password jika diperlukan
       db='kasir_sederhana',
       cursorclass=pymysql.cursors.DictCursor
   )
