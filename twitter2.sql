-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 21 Gru 2022, 23:40
-- Wersja serwera: 10.4.27-MariaDB
-- Wersja PHP: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `twitter2`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Zrzut danych tabeli `auth_permission`
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
(25, 'Can add user', 7, 'add_user'),
(26, 'Can change user', 7, 'change_user'),
(27, 'Can delete user', 7, 'delete_user'),
(28, 'Can view user', 7, 'view_user'),
(29, 'Can add post', 8, 'add_post'),
(30, 'Can change post', 8, 'change_post'),
(31, 'Can delete post', 8, 'delete_post'),
(32, 'Can view post', 8, 'view_post'),
(33, 'Can add comment', 9, 'add_comment'),
(34, 'Can change comment', 9, 'change_comment'),
(35, 'Can delete comment', 9, 'delete_comment'),
(36, 'Can view comment', 9, 'view_comment'),
(37, 'Can add like dislike comment', 10, 'add_likedislikecomment'),
(38, 'Can change like dislike comment', 10, 'change_likedislikecomment'),
(39, 'Can delete like dislike comment', 10, 'delete_likedislikecomment'),
(40, 'Can view like dislike comment', 10, 'view_likedislikecomment'),
(41, 'Can add like dislike', 11, 'add_likedislike'),
(42, 'Can change like dislike', 11, 'change_likedislike'),
(43, 'Can delete like dislike', 11, 'delete_likedislike'),
(44, 'Can view like dislike', 11, 'view_likedislike'),
(45, 'Can add following', 12, 'add_following'),
(46, 'Can change following', 12, 'change_following'),
(47, 'Can delete following', 12, 'delete_following'),
(48, 'Can view following', 12, 'view_following');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Zrzut danych tabeli `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(9, 'twitter2', 'comment'),
(12, 'twitter2', 'following'),
(11, 'twitter2', 'likedislike'),
(10, 'twitter2', 'likedislikecomment'),
(8, 'twitter2', 'post'),
(7, 'twitter2', 'user');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Zrzut danych tabeli `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-12-05 10:39:58.752542'),
(2, 'auth', '0001_initial', '2022-12-05 10:39:59.359467'),
(3, 'admin', '0001_initial', '2022-12-05 10:39:59.500554'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-12-05 10:39:59.516173'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-12-05 10:39:59.531789'),
(6, 'contenttypes', '0002_remove_content_type_name', '2022-12-05 10:39:59.625977'),
(7, 'auth', '0002_alter_permission_name_max_length', '2022-12-05 10:39:59.704582'),
(8, 'auth', '0003_alter_user_email_max_length', '2022-12-05 10:39:59.735844'),
(9, 'auth', '0004_alter_user_username_opts', '2022-12-05 10:39:59.751894'),
(10, 'auth', '0005_alter_user_last_login_null', '2022-12-05 10:39:59.798791'),
(11, 'auth', '0006_require_contenttypes_0002', '2022-12-05 10:39:59.814418'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2022-12-05 10:39:59.835793'),
(13, 'auth', '0008_alter_user_username_max_length', '2022-12-05 10:39:59.851339'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2022-12-05 10:39:59.882619'),
(15, 'auth', '0010_alter_group_name_max_length', '2022-12-05 10:39:59.913867'),
(16, 'auth', '0011_update_proxy_permissions', '2022-12-05 10:39:59.929499'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2022-12-05 10:39:59.960682'),
(18, 'sessions', '0001_initial', '2022-12-05 10:39:59.991927'),
(19, 'twitter2', '0001_initial', '2022-12-05 10:40:00.698885'),
(20, 'twitter2', '0002_alter_comment_is_reply_to', '2022-12-05 10:40:01.477900'),
(21, 'twitter2', '0003_alter_comment_is_reply_to', '2022-12-05 10:40:01.744934'),
(22, 'twitter2', '0004_alter_comment_options_alter_likedislike_options_and_more', '2022-12-05 10:40:01.776625'),
(23, 'twitter2', '0005_alter_user_email', '2022-12-19 09:25:38.924260');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `twitter2_comment`
--

CREATE TABLE `twitter2_comment` (
  `id` bigint(20) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `modified_time` datetime(6) NOT NULL,
  `content` varchar(300) NOT NULL,
  `is_reply_to_id` bigint(20) DEFAULT NULL,
  `post_id_id` bigint(20) NOT NULL,
  `user_id_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `twitter2_following`
--

CREATE TABLE `twitter2_following` (
  `id` bigint(20) NOT NULL,
  `time` datetime(6) NOT NULL,
  `user_id_followed_id` bigint(20) NOT NULL,
  `user_id_follower_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `twitter2_likedislike`
--

CREATE TABLE `twitter2_likedislike` (
  `post_id_id` bigint(20) NOT NULL,
  `time` datetime(6) NOT NULL,
  `like_dislike` varchar(1) NOT NULL,
  `user_id_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `twitter2_likedislikecomment`
--

CREATE TABLE `twitter2_likedislikecomment` (
  `post_id_id` bigint(20) NOT NULL,
  `time` datetime(6) NOT NULL,
  `like_dislike` varchar(1) NOT NULL,
  `user_id_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `twitter2_post`
--

CREATE TABLE `twitter2_post` (
  `id` bigint(20) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `modified_time` datetime(6) NOT NULL,
  `title` varchar(80) NOT NULL,
  `content` varchar(500) NOT NULL,
  `visibility` varchar(1) NOT NULL,
  `is_reply_to_id` bigint(20) DEFAULT NULL,
  `user_id_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `twitter2_user`
--

CREATE TABLE `twitter2_user` (
  `id` bigint(20) NOT NULL,
  `email` varchar(254) NOT NULL,
  `username` varchar(40) NOT NULL,
  `password` varchar(60) NOT NULL,
  `created_time` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Zrzut danych tabeli `twitter2_user`
--

INSERT INTO `twitter2_user` (`id`, `email`, `username`, `password`, `created_time`) VALUES
(1, 'twitter2ceo@mail.com', 'twitter2CEO', '1234', '2022-12-19 09:21:07.307409');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indeksy dla tabeli `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indeksy dla tabeli `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indeksy dla tabeli `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indeksy dla tabeli `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indeksy dla tabeli `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indeksy dla tabeli `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indeksy dla tabeli `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indeksy dla tabeli `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indeksy dla tabeli `twitter2_comment`
--
ALTER TABLE `twitter2_comment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `twitter2_comment_post_id_id_7910e03e_fk_twitter2_post_id` (`post_id_id`),
  ADD KEY `twitter2_comment_user_id_id_ea1673fd_fk_twitter2_user_id` (`user_id_id`),
  ADD KEY `twitter2_comment_is_reply_to_id_37b81281_fk_twitter2_comment_id` (`is_reply_to_id`);

--
-- Indeksy dla tabeli `twitter2_following`
--
ALTER TABLE `twitter2_following`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `twitter2_following_user_id_follower_id_user_67eea280_uniq` (`user_id_follower_id`,`user_id_followed_id`),
  ADD KEY `twitter2_following_user_id_followed_id_3d42d4f4_fk_twitter2_` (`user_id_followed_id`);

--
-- Indeksy dla tabeli `twitter2_likedislike`
--
ALTER TABLE `twitter2_likedislike`
  ADD PRIMARY KEY (`post_id_id`),
  ADD KEY `twitter2_likedislike_user_id_id_8877fbf8_fk_twitter2_user_id` (`user_id_id`);

--
-- Indeksy dla tabeli `twitter2_likedislikecomment`
--
ALTER TABLE `twitter2_likedislikecomment`
  ADD PRIMARY KEY (`post_id_id`),
  ADD KEY `twitter2_likedislike_user_id_id_b56b09e0_fk_twitter2_` (`user_id_id`);

--
-- Indeksy dla tabeli `twitter2_post`
--
ALTER TABLE `twitter2_post`
  ADD PRIMARY KEY (`id`),
  ADD KEY `twitter2_post_is_reply_to_id_e3288331_fk_twitter2_post_id` (`is_reply_to_id`),
  ADD KEY `twitter2_post_user_id_id_5395c672_fk_twitter2_user_id` (`user_id_id`);

--
-- Indeksy dla tabeli `twitter2_user`
--
ALTER TABLE `twitter2_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `twitter2_user_email_8bb053df_uniq` (`email`);

--
-- AUTO_INCREMENT dla zrzuconych tabel
--

--
-- AUTO_INCREMENT dla tabeli `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT dla tabeli `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT dla tabeli `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT dla tabeli `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT dla tabeli `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT dla tabeli `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT dla tabeli `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT dla tabeli `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT dla tabeli `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT dla tabeli `twitter2_comment`
--
ALTER TABLE `twitter2_comment`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT dla tabeli `twitter2_following`
--
ALTER TABLE `twitter2_following`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT dla tabeli `twitter2_post`
--
ALTER TABLE `twitter2_post`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT dla tabeli `twitter2_user`
--
ALTER TABLE `twitter2_user`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Ograniczenia dla zrzutów tabel
--

--
-- Ograniczenia dla tabeli `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Ograniczenia dla tabeli `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Ograniczenia dla tabeli `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Ograniczenia dla tabeli `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Ograniczenia dla tabeli `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Ograniczenia dla tabeli `twitter2_comment`
--
ALTER TABLE `twitter2_comment`
  ADD CONSTRAINT `twitter2_comment_is_reply_to_id_37b81281_fk_twitter2_comment_id` FOREIGN KEY (`is_reply_to_id`) REFERENCES `twitter2_comment` (`id`),
  ADD CONSTRAINT `twitter2_comment_post_id_id_7910e03e_fk_twitter2_post_id` FOREIGN KEY (`post_id_id`) REFERENCES `twitter2_post` (`id`),
  ADD CONSTRAINT `twitter2_comment_user_id_id_ea1673fd_fk_twitter2_user_id` FOREIGN KEY (`user_id_id`) REFERENCES `twitter2_user` (`id`);

--
-- Ograniczenia dla tabeli `twitter2_following`
--
ALTER TABLE `twitter2_following`
  ADD CONSTRAINT `twitter2_following_user_id_followed_id_3d42d4f4_fk_twitter2_` FOREIGN KEY (`user_id_followed_id`) REFERENCES `twitter2_user` (`id`),
  ADD CONSTRAINT `twitter2_following_user_id_follower_id_f96ed6f2_fk_twitter2_` FOREIGN KEY (`user_id_follower_id`) REFERENCES `twitter2_user` (`id`);

--
-- Ograniczenia dla tabeli `twitter2_likedislike`
--
ALTER TABLE `twitter2_likedislike`
  ADD CONSTRAINT `twitter2_likedislike_post_id_id_d28462d9_fk_twitter2_post_id` FOREIGN KEY (`post_id_id`) REFERENCES `twitter2_post` (`id`),
  ADD CONSTRAINT `twitter2_likedislike_user_id_id_8877fbf8_fk_twitter2_user_id` FOREIGN KEY (`user_id_id`) REFERENCES `twitter2_user` (`id`);

--
-- Ograniczenia dla tabeli `twitter2_likedislikecomment`
--
ALTER TABLE `twitter2_likedislikecomment`
  ADD CONSTRAINT `twitter2_likedislike_post_id_id_602f1d3f_fk_twitter2_` FOREIGN KEY (`post_id_id`) REFERENCES `twitter2_comment` (`id`),
  ADD CONSTRAINT `twitter2_likedislike_user_id_id_b56b09e0_fk_twitter2_` FOREIGN KEY (`user_id_id`) REFERENCES `twitter2_user` (`id`);

--
-- Ograniczenia dla tabeli `twitter2_post`
--
ALTER TABLE `twitter2_post`
  ADD CONSTRAINT `twitter2_post_is_reply_to_id_e3288331_fk_twitter2_post_id` FOREIGN KEY (`is_reply_to_id`) REFERENCES `twitter2_post` (`id`),
  ADD CONSTRAINT `twitter2_post_user_id_id_5395c672_fk_twitter2_user_id` FOREIGN KEY (`user_id_id`) REFERENCES `twitter2_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
