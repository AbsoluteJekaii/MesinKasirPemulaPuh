-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 04 Jan 2025 pada 14.29
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kasir_sederhana`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `products`
--

CREATE TABLE `products` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `price` int(11) NOT NULL,
  `stock` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `products`
--

INSERT INTO `products` (`id`, `name`, `price`, `stock`) VALUES
(1, 'Paket Ayam Geprek', 15000, 95),
(2, 'Paket Ayam Bakar', 15000, 94),
(3, 'Paket Chicken Katsu', 18000, 96),
(4, 'Paket Rice Bowl', 13000, 96),
(5, 'Paket Soto Ayam', 15000, 96),
(6, 'Ikan Bakar', 20000, 96),
(7, 'Dimsum', 14000, 97);

-- --------------------------------------------------------

--
-- Struktur dari tabel `transactions`
--

CREATE TABLE `transactions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `total_price` int(11) NOT NULL,
  `transaction_time` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `transactions`
--

INSERT INTO `transactions` (`id`, `user_id`, `product_id`, `quantity`, `total_price`, `transaction_time`) VALUES
(1, 2, 1, 2, 30000, '2024-08-12 15:23:25'),
(2, 2, 2, 2, 30000, '2024-08-12 15:23:33'),
(3, 2, 3, 2, 36000, '2024-08-12 15:23:38'),
(4, 2, 4, 2, 26000, '2024-08-12 15:23:45'),
(5, 2, 5, 2, 30000, '2024-08-12 15:23:49'),
(6, 2, 6, 2, 40000, '2024-08-12 15:42:02'),
(7, 2, 1, 1, 15000, '2024-08-13 14:13:14'),
(8, 2, 2, 1, 15000, '2024-08-13 14:13:14'),
(9, 2, 3, 1, 18000, '2024-08-13 14:13:14'),
(10, 2, 4, 1, 13000, '2024-08-13 14:13:14'),
(11, 2, 5, 1, 15000, '2024-08-13 14:13:14'),
(12, 2, 6, 1, 20000, '2024-08-13 14:13:14'),
(13, 2, 1, 1, 15000, '2024-08-13 15:39:21'),
(14, 2, 7, 3, 42000, '2024-08-14 00:53:25'),
(15, 2, 2, 1, 15000, '2024-08-14 00:54:08'),
(16, 2, 3, 1, 18000, '2024-08-14 00:54:08'),
(17, 2, 4, 1, 13000, '2024-08-14 00:54:08'),
(18, 2, 5, 1, 15000, '2024-08-14 00:54:08'),
(19, 2, 6, 1, 20000, '2024-08-14 00:54:08'),
(20, 2, 1, 1, 15000, '2024-09-05 06:52:49'),
(21, 2, 2, 2, 30000, '2024-09-05 06:52:49');

-- --------------------------------------------------------

--
-- Struktur dari tabel `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  `role` enum('admin','kasir') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `role`) VALUES
(1, 'admin', 'admin123', 'admin'),
(2, 'kasir', 'kasir123', 'kasir');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `transactions`
--
ALTER TABLE `transactions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `product_id` (`product_id`);

--
-- Indeks untuk tabel `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `products`
--
ALTER TABLE `products`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT untuk tabel `transactions`
--
ALTER TABLE `transactions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT untuk tabel `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `transactions`
--
ALTER TABLE `transactions`
  ADD CONSTRAINT `transactions_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `transactions_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
