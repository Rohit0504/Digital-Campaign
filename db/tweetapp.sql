-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 31, 2024 at 03:38 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tweetapp`
--

-- --------------------------------------------------------

--
-- Table structure for table `tweet_comments`
--

CREATE TABLE `tweet_comments` (
  `tweet_id` varchar(100) NOT NULL,
  `comment` varchar(255) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `tweet_comments`
--

INSERT INTO `tweet_comments` (`tweet_id`, `comment`) VALUES
('1774312113126756856', 'In 1961, the then PM Nehru was ready to give up #Katchatheevu island to Sri Lanka. He said that this island is not important to us. In 1974, Indira Gandhi fulfilled dream of Nehru and gave up Katchatheevu island to Sri Lanka.'),
('1774312113126756856', 'Congress blunders: North: Nehru gave away Kashmir to Pakistan. South: Nehru gave away Katchatheevu to Sri Lanka.'),
('1774312113126756856', 'But every Hindu hating and corrupt person is welcome in BJP how ironic'),
('1774312113126756856', 'Way to let the unity and integrity slide, Congress! ? Keep those traditions strong, right? ?'),
('1774312113126756856', 'That\'s good to hear'),
('1774101911328723034', 'In Tamil Nadu, so many deposit cheating cases have been filed. Incapable people in power in Tamil Nadu have not solved a single case for the past three years. CBI investigation is required to save the lakhs of people who lost their money.'),
('1774101911328723034', 'Gujarat Scam'),
('1774101911328723034', 'Jay Hind'),
('1774101911328723034', 'Must watch how the national thieves got washed in the #BJPWashingMachine and became national saints.'),
('1774099827627843926', 'Such a difficult task. Every government employee is engaged in elections for BJP. The difference between worker or officer has disappeared.'),
('1774099827627843926', 'We are all waiting for June'),
('1774099827627843926', 'Reality of Modi and BJP let’s Vote out Modi'),
('1774099827627843926', 'When it is election time Modi takes the name of Karyakartas and party workers to fool the people when elections are over he says that he is boss of 140 crore people but in reality only 35 lacs electing him'),
('1774099827627843926', 'Sir, to realize the dream of 400, you will have to do it till Ram Navami, otherwise the dream will not come true, your well-wisher.'),
('1774351392888566226', 'Chanakya had said that when all the thieves are on one side, then understand that the king is honest and the country is in good hands.'),
('1774351392888566226', 'Awesome Awesome Zindabad ???? The Socialist @1socialist1'),
('1774351392888566226', 'Tejashwi Yadav has blown away this time. After Lalu, Lalu\'s son has ruined the BJP.'),
('1774351392888566226', 'Bye bye Modi ji'),
('1774351392888566226', 'Arvind Kejriwal sacrificed his life fighting for freedom of India - Sunita Kejriwal');

-- --------------------------------------------------------

--
-- Table structure for table `tweet_detail`
--

CREATE TABLE `tweet_detail` (
  `tweet_id` varchar(200) NOT NULL,
  `party` varchar(20) NOT NULL,
  `tweet_content` varchar(200) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `tweet_detail`
--

INSERT INTO `tweet_detail` (`tweet_id`, `party`, `tweet_content`) VALUES
('1774312113126756856', 'PJP', 'Slow claps for Congress! \r\nThey willingly gave up #Katchatheevu and had no regrets about it either. Sometimes an MP of the Congress speaks about dividing the nation and sometimes they denigrate Indian'),
('1774101911328723034', 'PJP', 'People should be made aware of the political reality in the state of Kerala. They need to understand that LDF and UDF, which are often seen as opposing parties, actually have similar agendas.  '),
('1774099827627843926', 'Congress', 'It is the unwavering dedication and hard work of the Karyakartas at the booth level that ensure Modis triumphs. It is because of your tireless efforts that Modi is where he is today. @narendramodi\r\n ');

-- --------------------------------------------------------

--
-- Table structure for table `user_details`
--

CREATE TABLE `user_details` (
  `user_id` int(11) NOT NULL,
  `user_name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_details`
--

INSERT INTO `user_details` (`user_id`, `user_name`, `email`, `phone`, `password`, `created_at`) VALUES
(1, 'Prithiv', 'test@gmail.com', '123', '123', '2024-03-31 10:26:06'),
(2, 'Ricky', 'ricky@gmail.com', '7898787878', '12345', '2024-03-31 12:19:43');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tweet_detail`
--
ALTER TABLE `tweet_detail`
  ADD PRIMARY KEY (`tweet_id`);

--
-- Indexes for table `user_details`
--
ALTER TABLE `user_details`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `user_details`
--
ALTER TABLE `user_details`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
