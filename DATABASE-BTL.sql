-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th7 09, 2024 lúc 02:50 PM
-- Phiên bản máy phục vụ: 10.4.32-MariaDB
-- Phiên bản PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `python8`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `accounts`
--

CREATE TABLE `accounts` (
  `IDAccount` int(11) NOT NULL,
  `Account` varchar(50) DEFAULT NULL,
  `Password` varchar(50) DEFAULT NULL,
  `EmployeeID` int(11) DEFAULT NULL,
  `role` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `accounts`
--

INSERT INTO `accounts` (`IDAccount`, `Account`, `Password`, `EmployeeID`, `role`) VALUES
(1, 'admin', '123456', 10000, 'admin'),
(2, 'nhanvien1', '123123', 1, 'nhanvien'),
(3, 'nhanvien2', '321321', 2, 'nhanvien'),
(4, 'nhanvien3', '123123', 3, 'nhanvien'),
(6, 'nhanvien5', '123321', 5, 'nhanvien');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `customers`
--

CREATE TABLE `customers` (
  `CustomerID` int(11) NOT NULL,
  `FirstName` varchar(50) DEFAULT NULL,
  `LastName` varchar(50) DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL,
  `Phone` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `customers`
--

INSERT INTO `customers` (`CustomerID`, `FirstName`, `LastName`, `Address`, `Phone`) VALUES
(1, 'Van A', 'Nguyen', 'Hà Nội', '123456789'),
(2, 'Thi B', 'Tran', 'Hà Nam', '987654321'),
(3, 'Minh C', 'Pham', 'Phú Thọ', '246810975'),
(4, 'Thu D', 'Hoang', 'Hải Dương', '135792468'),
(5, 'Tuan E', 'Le', 'Thái Bình', '112233445'),
(6, 'Ngọc Anh', 'Văn Đình', 'Thanh Hóa', '0969261543'),
(9, 'Quốc Cường', 'Nguyễn', 'Quảng Trị', '345986548'),
(10, 'Nguyễn', 'Trung Kiên', 'Phú Thọ', '032165498');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `employees`
--

CREATE TABLE `employees` (
  `EmployeeID` int(11) NOT NULL,
  `FirstName` varchar(50) DEFAULT NULL,
  `LastName` varchar(50) DEFAULT NULL,
  `DateOfBirth` date DEFAULT NULL,
  `Position` varchar(50) DEFAULT NULL,
  `StartDate` date DEFAULT NULL,
  `Salary` decimal(10,2) DEFAULT NULL,
  `Address` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `Phone` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `employees`
--

INSERT INTO `employees` (`EmployeeID`, `FirstName`, `LastName`, `DateOfBirth`, `Position`, `StartDate`, `Salary`, `Address`, `Phone`) VALUES
(1, 'Van A', 'Nguyen', '1990-05-15', 'Sales staff', '2020-07-01', 2500.00, 'Hà Nội', '123456789'),
(2, 'Thi B', 'Tran', '1992-08-20', 'Sales staff', '2018-04-15', 3500.00, 'Hà Nam', '987654321'),
(3, 'Minh C', 'Pham', '1985-12-05', 'Transportation staff', '2017-09-10', 3000.00, 'Phú Thọ', '246810975'),
(4, 'Thu D', 'Hoang', '1988-10-10', 'Marketer', '2019-02-28', 2800.00, 'Hải Dương', '135792468'),
(5, 'Tuan E', 'Le', '1995-03-25', 'Customer advisor', '2021-01-10', 2800.00, 'Thái Bình', '112233445'),
(10000, 'admin', 'null', '0000-00-00', 'admin', '0000-00-00', 0.00, 'null', '0'),
(10004, 'Nguyễn Trung', 'Kiên', '2003-01-17', 'Lao Công', '2023-07-07', 10000.00, 'Phú Thọ', '0321654989');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `orders`
--

CREATE TABLE `orders` (
  `OrderID` int(11) NOT NULL,
  `OrderDate` date DEFAULT NULL,
  `EmployeeID` int(11) DEFAULT NULL,
  `CustomerID` int(11) DEFAULT NULL,
  `ProductID` int(11) DEFAULT NULL,
  `Quantity` int(11) DEFAULT NULL,
  `Status` varchar(50) DEFAULT NULL,
  `TotalPaymentAmount` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `orders`
--

INSERT INTO `orders` (`OrderID`, `OrderDate`, `EmployeeID`, `CustomerID`, `ProductID`, `Quantity`, `Status`, `TotalPaymentAmount`) VALUES
(1, '2024-07-01', 1, 1, 1, 5, 'Completed', 250.00),
(2, '2024-07-02', 2, 2, 2, 10, 'Completed', 789.90),
(3, '2024-07-03', 3, 3, 3, 15, 'Pending', 4035.00),
(4, '2024-07-09', 1, 1, 1, 100, 'Completed', 5000.00),
(5, '2024-07-09', 1, 2, 1, 100, 'Completed', 5000.00),
(6, '2024-07-09', 1, 2, 2, 100, 'Completed', 10000.00),
(7, '2024-07-09', 1, 9, 1, 50, 'Completed', 2500.00),
(8, '2024-07-09', 1, 9, 2, 100, 'Completed', 10000.00),
(9, '2024-07-09', 1, 6, 9, 5, 'Completed', 250.00),
(11, '2024-07-09', 1, 6, 9, 10, 'Completed', 500.00),
(13, '2024-07-09', 1, 5, 9, 20, 'Completed', 1000.00);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `products`
--

CREATE TABLE `products` (
  `ProductID` int(11) NOT NULL,
  `ProductName` varchar(100) DEFAULT NULL,
  `Price` decimal(10,2) DEFAULT NULL,
  `DateAdded` date DEFAULT NULL,
  `inventory` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `products`
--

INSERT INTO `products` (`ProductID`, `ProductName`, `Price`, `DateAdded`, `inventory`) VALUES
(1, 'Khoai Tây', 50.00, '2023-06-01', 250),
(2, 'Cà Rốt', 100.00, '2023-06-05', 400),
(3, 'Táo', 268.00, '2023-06-10', 100),
(8, 'Dưa Hấu', 150.00, '2023-08-01', 200),
(9, 'Lạc', 50.00, '2024-07-07', 200);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `revenue`
--

CREATE TABLE `revenue` (
  `RevenueID` int(11) NOT NULL,
  `OrderID` int(11) DEFAULT NULL,
  `RevenueDate` date DEFAULT NULL,
  `Amount` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `revenue`
--

INSERT INTO `revenue` (`RevenueID`, `OrderID`, `RevenueDate`, `Amount`) VALUES
(2, 2, '2024-07-02', 789.90),
(3, 4, '2024-07-09', 5000.00),
(4, 5, '2024-07-09', 5000.00),
(5, 6, '2024-07-09', 10000.00),
(6, 7, '2024-07-09', 2500.00),
(7, 8, '2024-07-09', 10000.00),
(8, 9, '2024-07-09', 250.00),
(10, 11, '2024-07-09', 500.00),
(12, 13, '2024-07-09', 1000.00);

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `accounts`
--
ALTER TABLE `accounts`
  ADD PRIMARY KEY (`IDAccount`),
  ADD KEY `EmployeeID` (`EmployeeID`);

--
-- Chỉ mục cho bảng `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`CustomerID`);

--
-- Chỉ mục cho bảng `employees`
--
ALTER TABLE `employees`
  ADD PRIMARY KEY (`EmployeeID`);

--
-- Chỉ mục cho bảng `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`OrderID`),
  ADD KEY `CustomerID` (`CustomerID`),
  ADD KEY `ProductID` (`ProductID`),
  ADD KEY `EmployeeID` (`EmployeeID`);

--
-- Chỉ mục cho bảng `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`ProductID`);

--
-- Chỉ mục cho bảng `revenue`
--
ALTER TABLE `revenue`
  ADD PRIMARY KEY (`RevenueID`),
  ADD KEY `OrderID` (`OrderID`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `accounts`
--
ALTER TABLE `accounts`
  MODIFY `IDAccount` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT cho bảng `customers`
--
ALTER TABLE `customers`
  MODIFY `CustomerID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT cho bảng `employees`
--
ALTER TABLE `employees`
  MODIFY `EmployeeID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10005;

--
-- AUTO_INCREMENT cho bảng `orders`
--
ALTER TABLE `orders`
  MODIFY `OrderID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT cho bảng `products`
--
ALTER TABLE `products`
  MODIFY `ProductID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT cho bảng `revenue`
--
ALTER TABLE `revenue`
  MODIFY `RevenueID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `accounts`
--
ALTER TABLE `accounts`
  ADD CONSTRAINT `accounts_ibfk_1` FOREIGN KEY (`EmployeeID`) REFERENCES `employees` (`EmployeeID`) ON DELETE CASCADE;

--
-- Các ràng buộc cho bảng `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`CustomerID`) REFERENCES `customers` (`CustomerID`) ON DELETE CASCADE,
  ADD CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`ProductID`) REFERENCES `products` (`ProductID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `orders_ibfk_3` FOREIGN KEY (`EmployeeID`) REFERENCES `employees` (`EmployeeID`) ON DELETE CASCADE;

--
-- Các ràng buộc cho bảng `revenue`
--
ALTER TABLE `revenue`
  ADD CONSTRAINT `revenue_ibfk_1` FOREIGN KEY (`OrderID`) REFERENCES `orders` (`OrderID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
