-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Aug 17, 2024 at 04:59 AM
-- Server version: 8.0.30
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_shelters`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add Shelter', 7, 'add_shelter'),
(26, 'Can change Shelter', 7, 'change_shelter'),
(27, 'Can delete Shelter', 7, 'delete_shelter'),
(28, 'Can view Shelter', 7, 'view_shelter'),
(29, 'Can add User', 8, 'add_user'),
(30, 'Can change User', 8, 'change_user'),
(31, 'Can delete User', 8, 'delete_user'),
(32, 'Can view User', 8, 'view_user'),
(33, 'Can add Kriteria', 9, 'add_kriteria'),
(34, 'Can change Kriteria', 9, 'change_kriteria'),
(35, 'Can delete Kriteria', 9, 'delete_kriteria'),
(36, 'Can view Kriteria', 9, 'view_kriteria'),
(37, 'Can add Train', 10, 'add_train'),
(38, 'Can change Train', 10, 'change_train'),
(39, 'Can delete Train', 10, 'delete_train'),
(40, 'Can view Train', 10, 'view_train');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL
) ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(9, 'home', 'kriteria'),
(7, 'home', 'shelter'),
(10, 'home', 'train'),
(8, 'home', 'user'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-08-08 12:22:12.057062'),
(2, 'auth', '0001_initial', '2024-08-08 12:22:14.459696'),
(3, 'admin', '0001_initial', '2024-08-08 12:22:14.966336'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-08-08 12:22:15.020322'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-08-08 12:22:15.080117'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-08-08 12:22:15.534997'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-08-08 12:22:15.893519'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-08-08 12:22:16.102786'),
(9, 'auth', '0004_alter_user_username_opts', '2024-08-08 12:22:16.159345'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-08-08 12:22:16.429071'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-08-08 12:22:16.444689'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-08-08 12:22:16.502372'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-08-08 12:22:16.823944'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-08-08 12:22:17.168014'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-08-08 12:22:17.320375'),
(16, 'auth', '0011_update_proxy_permissions', '2024-08-08 12:22:17.382116'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-08-08 12:22:17.762801'),
(18, 'home', '0001_initial', '2024-08-08 12:22:17.981632'),
(19, 'home', '0002_kriteria_shelter_atap_shelter_kolom_bangunan_and_more', '2024-08-08 12:22:18.561963'),
(20, 'home', '0003_remove_kriteria_atap_remove_kriteria_kolom_bangunan_and_more', '2024-08-08 12:22:18.938165'),
(21, 'home', '0004_alter_kriteria_bobot_alter_kriteria_id_and_more', '2024-08-08 12:22:19.608706'),
(22, 'home', '0005_alter_kriteria_bobot_alter_kriteria_id_and_more', '2024-08-08 12:22:20.425152'),
(23, 'home', '0006_shelter_status', '2024-08-08 12:22:20.567200'),
(24, 'home', '0007_train', '2024-08-08 12:22:20.660705'),
(25, 'home', '0008_rename_status_train_decision_alter_train_id', '2024-08-08 12:22:20.875107'),
(26, 'home', '0009_remove_train_id_alter_train_kolom_bangunan', '2024-08-08 12:22:21.124211'),
(27, 'sessions', '0001_initial', '2024-08-08 12:22:21.311082');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('rpa70ta72c7s085f2c12hxv9s61v2yyr', 'eyJ1c2VyIjoxfQ:1seUS1:tF5OoA8FjlBW_w5B0caegqWHB_eXeh2Jm3goU75B9Hk', '2024-08-29 06:59:13.166912'),
('uq4rqzav0t2p2mtio5j8784dqxll0sj4', 'eyJ1c2VyIjoxfQ:1sc2D5:JTD9_F3_29ZN4ANotMSnm9uWXKtqwDHBEuIuB0q9fa0', '2024-08-22 12:25:39.196179');

-- --------------------------------------------------------

--
-- Table structure for table `home_classification`
--

CREATE TABLE `home_classification` (
  `id` int NOT NULL,
  `latitude_longitude` varchar(255) NOT NULL,
  `atap` varchar(50) NOT NULL,
  `rangka_atap` varchar(50) NOT NULL,
  `kolom_bangunan` varchar(50) NOT NULL,
  `decision` varchar(50) NOT NULL,
  `alamat` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `home_classification`
--

INSERT INTO `home_classification` (`id`, `latitude_longitude`, `atap`, `rangka_atap`, `kolom_bangunan`, `decision`, `alamat`) VALUES
(3, '-5.15134, 119.42935', '3.0', '2.0', '2.0', 'Secure', 'Jl.rappocini raya lr.5 no1'),
(4, '-5.151653,119.429614', '4.0', '3.0', '3.0', 'Secure', 'Jl.rappocini raya lr.VG'),
(5, '-5.151736,119.429507', '3.0', '1.0', '2.0', 'Secure', 'Jl.rappocini raya lr.VG'),
(6, '-5.151825,119.429979', '4.0', '2.0', '3.0', 'Secure', 'Jl.rappocini raya lr.VG'),
(7, '-5.151186,119.429632', '2.0', '2.0', '3.0', 'Secure', 'JL.Rappocini Raya LR. III'),
(8, '-5.151174,119.429837', '2.0', '2.0', '3.0', 'Secure', 'Jalan Pelita Raya no.62 kec.Rappocini'),
(9, '-5.151164,119.429862', '4.0', '2.0', '2.0', 'Secure', 'lr 5i 12, Jl. Rappocini Raya'),
(10, '-5.152367,119.430117', '3.0', '2.0', '2.0', 'Secure', 'lr 5 no.1, Jl. Rappocini Raya'),
(11, '-5.152327,119.429847', '4.0', '3.0', '3.0', 'Secure', 'lr 5f no.4, Jl. Rappocini Raya'),
(12, '-5.152611746676702, 119.42906125887924', '3.0', '2.0', '2.0', 'Secure', 'Jl. Rappocini Raya Lorong 5 No.163'),
(13, '-5.152842,119.428344', '4.0', '3.0', '2.0', 'Secure', 'Jl. Rappocini Raya Lr. 3, Rappocini,'),
(14, '-5.149530, 119.426920', '3.0', '2.0', '3.0', 'Secure', 'Jl. Inspeksi Kanal No.3'),
(15, '-5.154150,119.429150', '3.0', '2.0', '3.0', 'Secure', 'Rappocini Raya LR 5B 6 - 2'),
(16, '-5.1479866, 119.4267793', '3.0', '2.0', '3.0', 'Secure', 'Maricaya Baru'),
(17, '-5.1492966, 119.4267843', '1.0', '2.0', '3.0', 'Secure', 'Jl. Monginsidi Baru, Bumi Tirta Nusantara'),
(18, '-5.1519746, 119.4268665', '2.0', '2.0', '2.0', 'Secure', 'Jl. Rappocini Raya, Lr. Kanal'),
(19, '-5.1519349, 119.4262006', '3.0', '3.0', '2.0', 'Secure', 'Jl. Mutiara I'),
(20, '-5.1500305, 119.4280359', '4.0', '1.0', '3.0', 'Secure', 'Jl. Mutiara III'),
(21, '-5.1507000, 119.4277821', '4.0', '2.0', '3.0', 'Secure', 'Jl. Mutiara V'),
(22, '-5.1514103, 119.4276473', '2.0', '2.0', '3.0', 'Secure', 'Jl. Inspeksi Kanal'),
(23, '-5.1521259, 119.4274079', '3.0', '3.0', '3.0', 'Secure', 'Jl. Rappocini Raya, Lorong. Kanal'),
(24, '-5.1495597, 119.4272611', '3.0', '3.0', '3.0', 'Secure', 'Jl. Mutiara Utama'),
(25, '-5.1524404, 119.4273553', '3.0', '1.0', '3.0', 'Secure', 'Jl. Rappocini Raya, Lr, 3'),
(26, '-5.1520464, 119.4284882', '1.0', '2.0', '3.0', 'Secure', 'Jl. Rappocini Raya, Lr. IIIG'),
(27, '-5.1490605, 119.4269174', '3.0', '1.0', '3.0', 'Secure', 'Jl. Monginsidi Baru'),
(28, '-5.1490578, 119.4268604', '4.0', '2.0', '3.0', 'Secure', 'Jl. Monginsidi Baru V'),
(29, '-5.1490491, 119.4267894', '4.0', '1.0', '2.0', 'Secure', 'Jl. Monginsidi Baru'),
(30, '-5.1497981,119.4263411', '2.0', '2.0', '3.0', 'Secure', 'Jl. Monginsidi Baru, Lr. 2'),
(31, '-5.1500910, 119.4262248', '3.0', '2.0', '3.0', 'Secure', 'Jl. Monginsidi Baru, Lr. 2'),
(32, '-5.1509031, 119.4261218', '1.0', '3.0', '3.0', 'Secure', 'Jl. Monginsidi Baru, Lr. 2'),
(33, '-5.1505411, 119.4257973', '3.0', '1.0', '2.0', 'Secure', 'Jl. Monginsidi Baru, Lr. 3'),
(34, '-5.1505271, 119.4257443', '4.0', '2.0', '3.0', 'Secure', 'Jl. Veteran Selatan, Lr. 3'),
(35, '-5.1504850, 119.4256179', '2.0', '2.0', '3.0', 'Secure', 'Jl. Veteran Selatan, Lr. 3'),
(36, '-5.1504302, 119.4254070', '1.0', '2.0', '2.0', 'Secure', 'Jl. Veteran Selatan, Lr. 3'),
(37, '-5.1497831, 119.4269530', '2.0', '2.0', '3.0', 'Secure', 'Jl. Inspeksi Kanal'),
(38, '-5.1501344, 119.4269067', '2.0', '2.0', '3.0', 'Secure', 'Jl. Inspeksi Kanal'),
(39, '-5.1517252, 119.4277697', '2.0', '3.0', '2.0', 'Secure', 'Jl. Rappocini Raya, Lr.3G'),
(40, '-5.1518320, 119.4281673', '2.0', '2.0', '2.0', 'Secure', 'Jl. Rappocini Raya, Lr.1G'),
(41, '-5.1571607, 119.4301998', '3.0', '3.0', '3.0', 'Secure', 'Citra Griyatama Estate'),
(42, '-5.1567383, 119.4301539', '3.0', '1.0', '3.0', 'Secure', 'Citra griyatama estate D16'),
(43, '-5.1569433, 119.4298605', '1.0', '2.0', '3.0', 'Secure', 'Citra griyatama estate D10'),
(44, '-5.1546032, 119.4281466', '4.0', '2.0', '3.0', 'Secure', 'Rappocini Raya No 4'),
(45, '-5.1505561, 119.4259049', '2.0', '1.0', '3.0', 'Secure', 'Jl. Monginsidi Baru, Lr. 2'),
(46, '-5.1546563, 119.4281157', '2.0', '2.0', '3.0', 'Secure', 'Rappocini Raya Lr 1'),
(47, '-5.1563286, 119.4290025', '4.0', '1.0', '3.0', 'Secure', 'Rappocini Raya Lr 5F');

-- --------------------------------------------------------

--
-- Table structure for table `home_kriteria`
--

CREATE TABLE `home_kriteria` (
  `id` int NOT NULL,
  `bobot` int NOT NULL,
  `nama_kriteria` varchar(50) NOT NULL,
  `sub_kriteria` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `home_kriteria`
--

INSERT INTO `home_kriteria` (`id`, `bobot`, `nama_kriteria`, `sub_kriteria`) VALUES
(1, 1, 'ATAP', 'Seng'),
(2, 2, 'ATAP', 'Asbes'),
(3, 3, 'ATAP', 'Genteng'),
(4, 4, 'ATAP', 'Cor'),
(5, 1, 'RANGKA ATAP', 'Kayu'),
(6, 1, 'RANGKA ATAP', 'Baja ringan'),
(7, 2, 'RANGKA ATAP', 'Besi'),
(8, 3, 'RANGKA ATAP', 'Beton'),
(9, 1, 'KOLOM BANGUNAN', 'Kayu'),
(10, 1, 'KOLOM BANGUNAN', 'Baja ringan'),
(11, 2, 'KOLOM BANGUNAN', 'Besi'),
(12, 3, 'KOLOM BANGUNAN', 'Beton berulang');

-- --------------------------------------------------------

--
-- Table structure for table `home_shelter`
--

CREATE TABLE `home_shelter` (
  `id` int NOT NULL,
  `nama_bangunan` varchar(255) NOT NULL,
  `latitude_longitude` varchar(255) NOT NULL,
  `alamat` varchar(255) NOT NULL,
  `atap` varchar(50) NOT NULL,
  `kolom_bangunan` varchar(50) NOT NULL,
  `rangka_atap` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `home_shelter`
--

INSERT INTO `home_shelter` (`id`, `nama_bangunan`, `latitude_longitude`, `alamat`, `atap`, `kolom_bangunan`, `rangka_atap`, `status`) VALUES
(2, 'Masjid', '-5.151653,119.429614', 'Jl.rappocini raya lr.VG', 'Cor', 'Beton berulang', 'Beton', 'Secure'),
(3, 'Rumah', '-5.151736,119.429507', 'Jl.rappocini raya lr.VG', 'Genteng', 'Besi', 'Baja ringan', 'Secure'),
(4, 'Rumah', '-5.151825,119.429979', 'Jl.rappocini raya lr.VG', 'Cor', 'Beton berulang', 'Besi', 'Secure'),
(5, 'Rumah', '-5.151186,119.429632', 'JL.Rappocini Raya LR. III', 'Asbes', 'Beton berulang', 'Besi', 'Secure'),
(6, 'Rumah', '-5.151174,119.429837', 'Jalan Pelita Raya no.62 kec.Rappocini', 'Asbes', 'Beton berulang', 'Besi', 'Secure'),
(7, 'Rumah', '-5.151164,119.429862', 'lr 5i 12, Jl. Rappocini Raya', 'Cor', 'Besi', 'Besi', 'Secure'),
(8, 'Rumah', '-5.151184,119.429904', 'lr 5i 12, Jl. RappociniRaya', 'Genteng', 'Kayu', 'Besi', 'Secure'),
(9, 'Masjid', '-5.152367,119.430117', 'lr 5 no.1, Jl. Rappocini Raya', 'Genteng', 'Besi', 'Besi', 'Secure'),
(10, 'Rumah', '-5.152327,119.429847', 'lr 5f no.4, Jl. Rappocini Raya', 'Cor', 'Beton berulang', 'Beton', 'Secure'),
(11, 'Masjid', '-5.152611746676702, 119.42906125887924', 'Jl. Rappocini Raya Lorong 5 No.163', 'Genteng', 'Besi', 'Besi', 'Secure'),
(12, 'Asrama', '-5.151208026113705, 119.4293336755869', 'Jl.rappocini Raya Lr.5 H No.1, ', 'Seng', 'Baja ringan', 'Baja ringan', 'Secure'),
(13, 'Rumah', '-5.152680, 119.429238', 'Jl. Rappocini Raya Lorong 5 No.335', 'Seng', 'Kayu', 'Kayu', 'Un-Secure'),
(14, 'Rumah', '-5.153010,119.429096', 'Jl. Rappocini Raya Lorong 5D 7-5', 'Seng', 'Kayu', 'Besi', 'Un-Secure'),
(15, 'Rumah', '-5.152700,119.428823', 'Jl. Rappocini Raya Lr. IIIE', 'Asbes', 'Kayu', 'Kayu', 'Un-Secure'),
(16, 'Rumah', '-5.152842,119.428344', 'Jl. Rappocini Raya Lr. 3, Rappocini,', 'Cor', 'Besi', 'Beton', 'Secure'),
(17, 'Rumah', '-5.149530, 119.426920', 'Jl. Inspeksi Kanal No.3', 'Genteng', 'Beton berulang', 'Besi', 'Secure'),
(18, 'Rumah', '-5.153483,119.427963', 'Jl. Rappocini Raya Lrg. 3 No.15d', 'Asbes', 'Kayu', 'Besi', 'Un-Secure'),
(19, 'Rumah', '-5.15354,119.42825', 'Jl. Rappocini Raya Lr III', 'Asbes', 'Kayu', 'Beton', 'Un-Secure'),
(20, 'Rumah', '-5.15356,119.4282', 'Jl. Rappocini Raya Lr IIIB No.1', 'Cor', 'Kayu', 'Kayu', 'Un-Secure'),
(21, 'Rumah', '-5.153816,119.428599', 'Jl. Rappocini Raya Lr IIIB 17', 'Asbes', 'Kayu', 'Kayu', 'Un-Secure'),
(22, 'Rumah', '-5.154150,119.429150', 'Rappocini Raya LR 5B 6 - 2', 'Genteng', 'Beton berulang', 'Besi', 'Secure'),
(23, 'Rumah', '-5.1479866, 119.4267793', 'Maricaya Baru', 'Genteng', 'Beton berulang', 'Besi', 'Secure'),
(24, 'Rumah', '-5.1492966, 119.4267843', 'Jl. Monginsidi Baru, Bumi Tirta Nusantara', 'Seng', 'Beton berulang', 'Besi', 'Secure'),
(25, 'Rumah', '-5.1519746, 119.4268665', 'Jl. Rappocini Raya, Lr. Kanal', 'Asbes', 'Besi', 'Besi', 'Secure'),
(26, 'Rumah', '-5.1519349, 119.4262006', 'Jl. Mutiara I', 'Genteng', 'Besi', 'Beton', 'Secure'),
(27, 'Rumah', '-5.1500305, 119.4280359', 'Jl. Mutiara III', 'Cor', 'Beton berulang', 'Baja ringan', 'Secure'),
(28, 'Rumah', '-5.1507000, 119.4277821', 'Jl. Mutiara V', 'Cor', 'Beton berulang', 'Besi', 'Secure'),
(29, 'Rumah', '-5.1514103, 119.4276473', 'Jl. Inspeksi Kanal', 'Asbes', 'Beton berulang', 'Besi', 'Secure'),
(30, 'Rumah', '-5.1521259, 119.4274079', 'Jl. Rappocini Raya, Lorong. Kanal', 'Genteng', 'Beton berulang', 'Beton', 'Secure'),
(31, 'Ruko', '-5.1495597, 119.4272611', 'Jl. Mutiara Utama', 'Genteng', 'Beton berulang', 'Beton', 'Secure'),
(32, 'Rumah', '-5.1524404, 119.4273553', 'Jl. Rappocini Raya, Lr, 3', 'Genteng', 'Beton berulang', 'Baja ringan', 'Secure'),
(33, 'Rumah', '-5.1520464, 119.4284882', 'Jl. Rappocini Raya, Lr. IIIG', 'Seng', 'Beton berulang', 'Besi', 'Secure'),
(34, 'Rumah', '-5.1490605, 119.4269174', 'Jl. Monginsidi Baru', 'Genteng', 'Beton berulang', 'Kayu', 'Secure'),
(35, 'Rumah', '-5.1490578, 119.4268604', 'Jl. Monginsidi Baru V', 'Cor', 'Beton berulang', 'Besi', 'Secure'),
(36, 'Sekolah', '-5.1490491, 119.4267894', 'Jl. Monginsidi Baru', 'Cor', 'Besi', 'Kayu', 'Secure'),
(37, 'Panti Asuhan', '-5.1497981,119.4263411', 'Jl. Monginsidi Baru, Lr. 2', 'Asbes', 'Beton berulang', 'Besi', 'Secure'),
(38, 'Rumah', '-5.1500910, 119.4262248', 'Jl. Monginsidi Baru, Lr. 2', 'Genteng', 'Beton berulang', 'Besi', 'Secure'),
(39, 'Rumah', '-5.1509031, 119.4261218', 'Jl. Monginsidi Baru, Lr. 2', 'Seng', 'Beton berulang', 'Beton', 'Secure'),
(40, 'Rumah', '-5.1505561, 119.4259049', 'Jl. Monginsidi Baru, Lr. 2', 'Asbes', 'Beton berulang', 'Kayu', 'Secure'),
(41, 'Rumah', '-5.1505411, 119.4257973', 'Jl. Monginsidi Baru, Lr. 3', 'Genteng', 'Besi', 'Baja ringan', 'Secure'),
(42, 'Rumah', '-5.1505271, 119.4257443', 'Jl. Veteran Selatan, Lr. 3', 'Cor', 'Beton berulang', 'Besi', 'Secure'),
(43, 'Rumah', '-5.1504850, 119.4256179', 'Jl. Veteran Selatan, Lr. 3', 'Asbes', 'Beton berulang', 'Besi', 'Secure'),
(44, 'Gudang', '-5.1504302, 119.4254070', 'Jl. Veteran Selatan, Lr. 3', 'Seng', 'Besi', 'Besi', 'Secure'),
(45, 'Rumah', '-5.1497831, 119.4269530', 'Jl. Inspeksi Kanal', 'Asbes', 'Beton berulang', 'Besi', 'Secure'),
(46, 'Toko', '-5.1501344, 119.4269067', 'Jl. Inspeksi Kanal', 'Asbes', 'Beton berulang', 'Besi', 'Secure'),
(47, 'Rumah', '-5.1504850, 119.4268259', 'Jl. Inspeksi Kanal', 'Genteng', 'Kayu', 'Beton', 'Un-Secure'),
(48, 'Rumah', '-5.1511291, 119.4266053', 'Jl. Inspeksi Kanal 1', 'Asbes', 'Besi', 'Kayu', 'Secure'),
(49, 'Rumah', '-5.1517252, 119.4277697', 'Jl. Rappocini Raya, Lr.3G', 'Asbes', 'Besi', 'Beton', 'Secure'),
(50, 'Rumah', '-5.1518320, 119.4281673', 'Jl. Rappocini Raya, Lr.1G', 'Asbes', 'Besi', 'Besi', 'Secure'),
(51, 'Rumah', '-5.1571607, 119.4301998', 'Citra Griyatama Estate', 'Genteng', 'Beton berulang', 'Beton', 'Secure'),
(52, 'Rumah', '-5.1567383, 119.4301539', 'Citra griyatama estate D16', 'Genteng', 'Beton berulang', 'Baja ringan', 'Secure'),
(53, 'Rumah', '-5.1569433, 119.4298605', 'Citra griyatama estate D10', 'Seng', 'Beton berulang', 'Besi', 'Secure'),
(54, 'Rumah', '-5.1546032, 119.4281466', 'Rappocini Raya No 4', 'Cor', 'Beton berulang', 'Besi', 'Secure'),
(55, 'Rumah', '-5.1546563, 119.4281157', 'Rappocini Raya Lr 1', 'Asbes', 'Beton berulang', 'Besi', 'Secure'),
(56, 'Rumah', '-5.1559536, 119.4280527', 'Rappocini Raya Lr 1', 'Seng', 'Baja ringan', 'Kayu', 'Un-Secure'),
(57, 'Rumah', '-5.1560010, 119.4272587', 'Rappocini Raya Lr 1G', 'Asbes', 'Besi', 'Kayu', 'Un-Secure'),
(58, 'Rumah', '-5.1559055, 119.4266794', 'Rappocini Raya Lr 1 G No 4', 'Cor', 'Kayu', 'Kayu', 'Un-Secure'),
(59, 'Ruko', '-5.1564558, 119.4275239', 'Rappocii Raya Lr 2', 'Genteng', 'Kayu', 'Baja ringan', 'Un-Secure'),
(60, 'Rumah', '-5.1577842, 119.4294276', 'Rappocini Raya Lr 2 V', 'Seng', 'Besi', 'Baja ringan', 'Un-Secure'),
(61, 'Rumah', '-5.1555452, 119.4292989', 'Rappocini Raya Lr 5', 'Asbes', 'Kayu', 'Kayu', 'Un-Secure'),
(62, 'Rumah', '-5.1563286, 119.4290025', 'Rappocini Raya Lr 5F', 'Cor', 'Beton berulang', 'Baja ringan', 'Secure'),
(63, 'Rumah', '-5.1560017, 119.4261456', 'Rappocini  Raya  Lr 2', 'Genteng', 'Kayu', 'Kayu', 'Un-Secure'),
(64, 'Rumah', '-5.1540943, 119.4290568', 'Rappocini Raya Lr 11', 'Asbes', 'Besi', 'Baja ringan', 'Un-Secure'),
(65, 'Toko Bangunan', '-5.1543070, 119.4274747', 'Rappocini Raya Lr 2', 'Seng', 'Baja ringan', 'Baja ringan', 'Un-Secure'),
(66, 'Rumah', '-5.1542299, 119.4271753', 'Rappocini Raya Lr 2 A', 'Asbes', 'Kayu', 'Kayu', 'Un-Secure');

-- --------------------------------------------------------

--
-- Table structure for table `home_train`
--

CREATE TABLE `home_train` (
  `atap` varchar(50) NOT NULL,
  `rangka_atap` varchar(50) NOT NULL,
  `kolom_bangunan` varchar(50) NOT NULL,
  `decision` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `home_train`
--

INSERT INTO `home_train` (`atap`, `rangka_atap`, `kolom_bangunan`, `decision`) VALUES
('Seng', 'Kayu', 'Kayu', 'Un-Secure'),
('Asbes', 'Baja ringan', 'Baja ringan', 'Un-Secure'),
('Genteng', 'Besi', 'Besi', 'Secure'),
('Cor', 'Beton', 'Beton berulang', 'Secure'),
('Seng', 'Baja ringan', 'Kayu', 'Un-Secure'),
('Asbes', 'Kayu', 'Baja ringan', 'Un-Secure'),
('Genteng', 'Beton', 'Besi', 'Secure'),
('Cor', 'Besi', 'Beton berulang', 'Secure'),
('Seng', 'Besi', 'Beton berulang', 'Secure'),
('Asbes', 'Kayu', 'Kayu', 'Un-Secure'),
('Asbes', 'Besi', 'Beton berulang', 'Secure'),
('Genteng', 'Kayu', 'Kayu', 'Un-Secure'),
('Cor', 'Besi', 'Besi', 'Secure'),
('Genteng', 'Kayu', 'Beton berulang', 'Secure'),
('Asbes', 'Besi', 'Kayu', 'Un-Secure'),
('Asbes', 'Baja ringan', 'Kayu', 'Un-Secure'),
('Asbes', 'Kayu', 'Besi', 'Un-Secure'),
('Asbes', 'Beton', 'Beton berulang', 'Secure'),
('Seng', 'Beton', 'Beton berulang', 'Secure'),
('Cor', 'Besi', 'Besi', 'Secure'),
('Seng', 'Baja ringan', 'Baja ringan', 'Un-Secure'),
('Seng', 'Kayu', 'Baja ringan', 'Un-Secure'),
('Seng', 'Besi', 'Baja ringan', 'Un-Secure'),
('Genteng', 'Baja ringan', 'Kayu', 'Un-Secure'),
('Genteng', 'Kayu', 'Baja ringan', 'Un-Secure'),
('Cor', 'Kayu', 'Kayu', 'Un-Secure'),
('Cor', 'Kayu', 'Baja ringan', 'Un-Secure'),
('Cor', 'Baja ringan', 'Kayu', 'Un-Secure');

-- --------------------------------------------------------

--
-- Table structure for table `home_user`
--

CREATE TABLE `home_user` (
  `id` int NOT NULL,
  `username` varchar(30) NOT NULL,
  `password` varchar(255) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `level` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `home_user`
--

INSERT INTO `home_user` (`id`, `username`, `password`, `nama`, `level`) VALUES
(1, 'admin', 'admin', 'win', 'admin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `home_classification`
--
ALTER TABLE `home_classification`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `home_kriteria`
--
ALTER TABLE `home_kriteria`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `home_shelter`
--
ALTER TABLE `home_shelter`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `home_user`
--
ALTER TABLE `home_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `home_classification`
--
ALTER TABLE `home_classification`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=48;

--
-- AUTO_INCREMENT for table `home_kriteria`
--
ALTER TABLE `home_kriteria`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `home_shelter`
--
ALTER TABLE `home_shelter`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=67;

--
-- AUTO_INCREMENT for table `home_user`
--
ALTER TABLE `home_user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
