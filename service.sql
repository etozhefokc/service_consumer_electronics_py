-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1
-- Время создания: Июн 29 2021 г., 02:13
-- Версия сервера: 10.4.19-MariaDB
-- Версия PHP: 8.0.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `service`
--
CREATE DATABASE IF NOT EXISTS `service` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `service`;

-- --------------------------------------------------------

--
-- Структура таблицы `clients`
--

CREATE TABLE IF NOT EXISTS `clients` (
  `id` int(20) NOT NULL,
  `client` varchar(30) NOT NULL,
  `address` varchar(30) NOT NULL,
  `contact` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `clients`
--

INSERT INTO `clients` (`id`, `client`, `address`, `contact`) VALUES
(1, 'Масаев Т.Р.', 'Советская,34', '+79538619569'),
(2, 'Птушкин А.С.', 'Плашкина,27', '+79898621238');

-- --------------------------------------------------------

--
-- Структура таблицы `performers`
--

CREATE TABLE IF NOT EXISTS `performers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `performer` varchar(30) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `performers`
--

INSERT INTO `performers` (`id`, `performer`, `username`, `password`) VALUES
(1, 'Петров А.В.', 'pav', '123'),
(2, 'Баширов А.В.', 'bav', '123'),
(3, 'Пунин И.В.', 'piv', '123');

-- --------------------------------------------------------

--
-- Структура таблицы `things`
--

CREATE TABLE IF NOT EXISTS `things` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(11) NOT NULL,
  `importance` int(11) NOT NULL,
  `сollect_date` date NOT NULL,
  `realize_date` date NOT NULL,
  `status` int(11) NOT NULL,
  `type` varchar(11) NOT NULL,
  `performer_id` int(11) NOT NULL,
  `client_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `things`
--

INSERT INTO `things` (`id`, `name`, `importance`, `сollect_date`, `realize_date`, `status`, `type`, `performer_id`, `client_id`) VALUES
(1, 'Кофемолка', 1, '2021-06-01', '2021-06-02', 0, '1', 1, 1),
(2, 'Компьютер', 2, '2021-06-29', '2021-06-30', 1, '1', 2, 1);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
