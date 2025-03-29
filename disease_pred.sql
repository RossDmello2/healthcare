-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 27, 2024 at 09:09 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 7.3.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `disease_pred`
--

-- --------------------------------------------------------

--
-- Table structure for table `add_check`
--

CREATE TABLE `add_check` (
  `add_id` int(10) NOT NULL,
  `ngo_name` text NOT NULL,
  `type_check` varchar(255) NOT NULL,
  `date` date NOT NULL,
  `time` varchar(6) NOT NULL,
  `contact` varchar(333) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `add_check`
--

INSERT INTO `add_check` (`add_id`, `ngo_name`, `type_check`, `date`, `time`, `contact`) VALUES
(1, 'nss', 'eye checkup', '2023-04-09', '01:00', '898989989'),
(2, 'nss', 'teeth checkup', '2023-04-16', '0000-0', '898988989'),
(3, 'tanmann', 'free check-ups', '2023-05-20', '13:00', '898989898'),
(4, 'tanmann', 'eye checkup', '2023-05-20', '23:15', '898989898'),
(5, 'tanmann', 'physical check-up', '2023-05-27', '10:00', '989898989');

-- --------------------------------------------------------

--
-- Table structure for table `b_donation`
--

CREATE TABLE `b_donation` (
  `b_id` int(10) NOT NULL,
  `name` varchar(255) NOT NULL,
  `blood_group` varchar(255) NOT NULL,
  `age` int(200) NOT NULL,
  `mobile` varchar(200) NOT NULL,
  `past_illness` varchar(255) NOT NULL,
  `posted_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `b_donation`
--

INSERT INTO `b_donation` (`b_id`, `name`, `blood_group`, `age`, `mobile`, `past_illness`, `posted_at`) VALUES
(17, 'Asher lopes ', 'AB+', 54, '7676767678', 'nope', '2023-02-07 10:52:11'),
(18, 'dillon', 'A+', 19, '7676767678', 'nope', '2023-04-06 13:04:41'),
(19, 'preeti', 'A+', 20, '98989898', 'nope', '2023-04-06 13:05:06'),
(20, 'rahul ', 'AB+', 20, '98989898', 'nope', '2023-04-23 14:48:46'),
(21, 'rahul ', 'AB+', 20, '909089898', 'nope', '2023-05-01 08:08:06'),
(22, 'raj', 'AB+', 21, '2882828882', 'nope', '2023-05-05 13:43:33');

-- --------------------------------------------------------

--
-- Table structure for table `doc_user`
--

CREATE TABLE `doc_user` (
  `sr_no` int(10) NOT NULL,
  `d_name` varchar(233) NOT NULL,
  `email` varchar(333) NOT NULL,
  `passwrd1` varchar(333) NOT NULL,
  `number` varchar(333) NOT NULL,
  `address` varchar(333) NOT NULL,
  `special` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `doc_user`
--

INSERT INTO `doc_user` (`sr_no`, `d_name`, `email`, `passwrd1`, `number`, `address`, `special`) VALUES
(1, 'shah', 'shah12@gmail.com', '$2b$12$oVTs/Ox.p8nSJ8sdxrlFnu4vbabP3OzSjOvTWMc4KurxlWeZqfgI2', '07378772683', '401 Adarsh,plotNo.44', 'ortho'),
(2, 'patil', 'patil12@gmail.com', '$2b$12$GcakEZbJLWwIVcWj0KIkDehs2coivoaSrt2BiLMjzUbqBEIp55ZFq', '07378772683', '401 Adarsh,plotNo.44', 'ortho'),
(3, 'redkar', 'redkr12@gmail.com', '$2b$12$uxvYIbeMX24Cv5zo50wV8u6oZ9ccV.2UobP/0EKOJsyn2QGBgDYYK', '07378772683', '401 Adarsh,plotNo.44', 'skin'),
(4, 'usdfuiw', 'sddfa@gmail.com', '$2b$12$24MWL/fKJlLOB0tdqqhlaua0WrMELquAhgdtVnlRRWpdVD1q78el2', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `doc_users`
--
-- Error reading structure for table disease_pred.doc_users: #1932 - Table 'disease_pred.doc_users' doesn't exist in engine
-- Error reading data for table disease_pred.doc_users: #1064 - You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'FROM `disease_pred`.`doc_users`' at line 1

-- --------------------------------------------------------

--
-- Table structure for table `ngo_users`
--

CREATE TABLE `ngo_users` (
  `ngo_name` varchar(255) NOT NULL,
  `pass1` varchar(255) NOT NULL,
  `type1` varchar(255) NOT NULL,
  `number` varchar(244) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `sr_no` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ngo_users`
--

INSERT INTO `ngo_users` (`ngo_name`, `pass1`, `type1`, `number`, `created_at`, `sr_no`) VALUES
('wie', '$2b$12$0QElBBARmfdAuiVBCUtIzO9sLf5AOyr2oSLpHU6mNNQ09U3lWbpDm', 'blood camps', '6768787878', '2023-01-16 16:47:12', 4),
('adani', '$2b$12$/5rG60XacEiQqGnVVo2SZuTdVRLYZVEjXdc3zLurlnq8Lcjd1oS.G', 'social work', '898989898', '2023-02-02 18:55:10', 5),
('sav', '$2b$12$MZ5Zl3QtKDIYX3LtJFjy5OU8oV8Cn52oUzd.bWiVCZGPKJ9kHVbPm', 'check-ups', '8989989889', '2023-02-09 08:15:22', 6),
('nss12', '$2b$12$W8XAWuXLqBKAUhL/B4tBuuaA3BVQhZ0W7oN340LsBYYgOTE1V1Ftu', 'free medications', '8080909090', '2023-03-15 17:04:19', 7),
('nss34', '$2b$12$433CuJOP/uHnu6fW4CpKgeCa9TUwA1QeHSbIhSlyvu3XY3p0lV0nm', 'check-ups', '809090909', '2023-03-15 17:05:41', 8),
('key', '$2b$12$sOv22YeVIi6NQAlSBFoe..UIyBxR9yj5/p75tOL69MEU7f141qKs2', 'blood camps', '8989898898', '2023-04-07 09:42:38', 9),
('tanmann', '$2b$12$nGTAqcrUKCigSbO67.Cxte68unyKhqhFPMcvuBnE.FG11OVbfnwcu', 'check-ups', '8998989898', '2023-05-01 08:09:09', 10);

-- --------------------------------------------------------

--
-- Table structure for table `patient_users`
--

CREATE TABLE `patient_users` (
  `sr_no` int(10) NOT NULL,
  `p_name` varchar(233) NOT NULL,
  `number` varchar(333) NOT NULL,
  `email` varchar(333) NOT NULL,
  `password1` varchar(333) NOT NULL,
  `address` varchar(333) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `patient_users`
--

INSERT INTO `patient_users` (`sr_no`, `p_name`, `number`, `email`, `password1`, `address`, `created_at`) VALUES
(1, 'Asher Lopes', '07378772683', 'john_lopes@rediffmail.com', '$2b$12$C0wrx4vt5.Wsu8hx/MDkM.v8nj4GZE4VRz6sHvJ70cD.RlhwuTRwK', '401 Adarsh,plotNo.44', '2023-01-26 17:19:22'),
(2, 'rahul', '8998989898', 'rahul12@gmail.com', '$2b$12$g2sYa0qGStbRJLbcH2WsU.vLcOFAKR1dNeF82y1yM0o7en9aqYMQq', 'yogi nagar', '2023-02-02 19:24:06'),
(3, 'Ash', '07378772683', 'Ash12@gmail.com', '', '401 Adarsh,plotNo.44', '2023-04-06 08:32:30'),
(4, 'abc', '7878787877', 'abc12@gmail.com', '1234', '401 Adarsh,plotNo.44', '2023-04-06 08:36:32'),
(5, 'def', '07378772683', 'def12@gmail.com', '$2b$12$ooYARQZuTpJyrL0JmskMsOz2ptP0gJRftnd3Nc7pJ5tN8vWTugduK', '401 Adarsh,plotNo.44', '2023-04-06 08:46:36'),
(6, 'Asher', '7378772683', 'asherlopes4420@gmail.com', '$2b$12$d8aBnjEdix5PtkIsV4ZCaeSqOmGpc3MFjcSwOAMDBNsq7cNW4fpge', 'mumbai', '2023-05-01 07:58:52'),
(7, 'Asher ', '9378772683', 'asher12@gmail.com', '$2b$12$2gafpVxRwkfoMyIkmW.8huFL3Kkgrdw12lsoz7V6WcYo3rVX.u5rO', 'mumbai plot.44', '2023-05-01 08:05:51'),
(8, 'Asher Lopes', '898989898', 'Asher122@gmail.com', '$2b$12$.exLNp80PLFqqi3FgOWQoubgjhWG3EP6OGDfF0nIzratQb9dvEa4G', '401 Adarsh,plotNo.44', '2023-05-05 13:35:09');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `add_check`
--
ALTER TABLE `add_check`
  ADD PRIMARY KEY (`add_id`);

--
-- Indexes for table `b_donation`
--
ALTER TABLE `b_donation`
  ADD PRIMARY KEY (`b_id`);

--
-- Indexes for table `doc_user`
--
ALTER TABLE `doc_user`
  ADD PRIMARY KEY (`sr_no`);

--
-- Indexes for table `ngo_users`
--
ALTER TABLE `ngo_users`
  ADD PRIMARY KEY (`sr_no`);

--
-- Indexes for table `patient_users`
--
ALTER TABLE `patient_users`
  ADD PRIMARY KEY (`sr_no`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `add_check`
--
ALTER TABLE `add_check`
  MODIFY `add_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `b_donation`
--
ALTER TABLE `b_donation`
  MODIFY `b_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `doc_user`
--
ALTER TABLE `doc_user`
  MODIFY `sr_no` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `ngo_users`
--
ALTER TABLE `ngo_users`
  MODIFY `sr_no` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `patient_users`
--
ALTER TABLE `patient_users`
  MODIFY `sr_no` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
