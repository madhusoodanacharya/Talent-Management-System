-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: tms
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `basic_info`
--

DROP TABLE IF EXISTS `basic_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `basic_info` (
  `UID` int NOT NULL,
  `FNAME` varchar(20) DEFAULT NULL,
  `LNAME` varchar(20) DEFAULT NULL,
  `PHONE_NO` bigint DEFAULT NULL,
  `CITY` varchar(20) DEFAULT NULL,
  `MAILID` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`UID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `basic_info`
--

LOCK TABLES `basic_info` WRITE;
/*!40000 ALTER TABLE `basic_info` DISABLE KEYS */;
INSERT INTO `basic_info` VALUES (1,'MADHUSOODAN','ACHARYA',9036017507,'MYS','MADHUSOODAN123@GMAIL.COM'),(2,'SRINIDHI','R',6361619540,'MYS','SRINIDHIR123@GMAIL.COM'),(3,'BHARGAV','BHAT',6986768808,'BNG','BHARGAVBHAT123@GMAIL.COM'),(4,'PAVAN','JOIS',8951268808,'BNG','PAVAN123@GMAIL.COM'),(5,'PRATHAM','ACHARYA',8867150507,'MYS','PRATHAM123@GMAIL.COM'),(6,'SRINIVAS','G',9845250507,'BNG','SRINIVASG123@GMAIL.COM');
/*!40000 ALTER TABLE `basic_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login_info`
--

DROP TABLE IF EXISTS `login_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login_info` (
  `LID` int NOT NULL,
  `TYPE` varchar(20) DEFAULT NULL,
  `USERNAME` varchar(20) DEFAULT NULL,
  `PASSWORD` varchar(20) DEFAULT NULL,
  `UID` int DEFAULT NULL,
  PRIMARY KEY (`LID`),
  KEY `UID` (`UID`),
  CONSTRAINT `login_info_ibfk_1` FOREIGN KEY (`UID`) REFERENCES `basic_info` (`UID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login_info`
--

LOCK TABLES `login_info` WRITE;
/*!40000 ALTER TABLE `login_info` DISABLE KEYS */;
INSERT INTO `login_info` VALUES (1,'ADMIN','MADHU182','MADHU182',1),(2,'ADMIN','S123','S123',2),(3,'USER','B123','B123',3),(4,'USER','P123','P123',4),(5,'ADMIN','PR123','PR123',5),(6,'USER','SR123','SR123',6);
/*!40000 ALTER TABLE `login_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `skill_certification`
--

DROP TABLE IF EXISTS `skill_certification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `skill_certification` (
  `CID` int NOT NULL,
  `PLACE_SECURED` int DEFAULT NULL,
  `CERTIFICATE_DESCRIPTION` varchar(20) DEFAULT NULL,
  `SID` int DEFAULT NULL,
  `UID` int DEFAULT NULL,
  PRIMARY KEY (`CID`),
  KEY `SID` (`SID`),
  KEY `UID` (`UID`),
  CONSTRAINT `skill_certification_ibfk_1` FOREIGN KEY (`SID`) REFERENCES `skills` (`SID`) ON DELETE CASCADE,
  CONSTRAINT `skill_certification_ibfk_2` FOREIGN KEY (`UID`) REFERENCES `basic_info` (`UID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `skill_certification`
--

LOCK TABLES `skill_certification` WRITE;
/*!40000 ALTER TABLE `skill_certification` DISABLE KEYS */;
INSERT INTO `skill_certification` VALUES (1,0,'COURSE',1,1),(2,2,'COMPETITION',1,1),(3,0,'COURSE',2,1),(4,0,'COURSE',3,1),(5,0,'COURSE',4,2),(6,1,'COMPETITION',4,2),(7,0,'COURSE',5,2),(8,0,'COURSE',6,3),(9,2,'COMPETITION',6,3),(10,0,'COURSE',7,3),(11,1,'COMPETITION',7,3),(12,0,'COURSE',8,3),(13,0,'COURSE',9,4),(14,1,'COMPETITION',9,4),(15,0,'COURSE',10,4),(16,0,'COURSE',11,5),(17,1,'COMPETITION',11,5),(18,0,'COURSE',12,5),(19,1,'COMPETITION',12,5),(20,0,'COURSE',13,5),(21,0,'COURSE',14,6),(22,0,'COURSE',15,6);
/*!40000 ALTER TABLE `skill_certification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `skill_project`
--

DROP TABLE IF EXISTS `skill_project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `skill_project` (
  `PID` int NOT NULL,
  `PROJECT_DESCRIPTION` varchar(20) DEFAULT NULL,
  `SID` int DEFAULT NULL,
  `UID` int DEFAULT NULL,
  PRIMARY KEY (`PID`),
  KEY `SID` (`SID`),
  KEY `UID` (`UID`),
  CONSTRAINT `skill_project_ibfk_1` FOREIGN KEY (`SID`) REFERENCES `skills` (`SID`) ON DELETE CASCADE,
  CONSTRAINT `skill_project_ibfk_2` FOREIGN KEY (`UID`) REFERENCES `basic_info` (`UID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `skill_project`
--

LOCK TABLES `skill_project` WRITE;
/*!40000 ALTER TABLE `skill_project` DISABLE KEYS */;
INSERT INTO `skill_project` VALUES (1,'TMS',1,1),(2,'BUS MANAGEMENT',1,1),(3,'CAB MANAGEMENT',2,1),(4,'TRAIN BOOKING',2,1),(5,'LIBRARY MANAGEMENT',3,1),(6,'MOBILE FINDER',4,2),(7,'CART MANAGEMENT',5,2),(8,'HEART BEAT TRACKER',6,3),(9,'CAB BOOKIG',7,3),(10,'MOTION DETECTOR',8,3),(11,'BUS MANAGEMENT',8,3),(12,'CAB MANAGEMENT',9,4),(13,'TRAIN FINDER',10,4),(14,'LIBRARY MANAGEMENT',11,5),(15,'LAB MANAGEMENT',12,5),(16,'STUDENT MANAGEMENT',12,5),(17,'WEBPAGE DUPLICATION',13,6),(18,'TRACKER',14,6),(19,'TMS',15,6),(20,'WEBPAGE ',15,6);
/*!40000 ALTER TABLE `skill_project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `skills`
--

DROP TABLE IF EXISTS `skills`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `skills` (
  `SID` int NOT NULL,
  `SKILL` varchar(20) DEFAULT NULL,
  `NO_OF_CERTIFICATES` int DEFAULT NULL,
  `NO_OF_PROJECTS` int DEFAULT NULL,
  `UID` int DEFAULT NULL,
  PRIMARY KEY (`SID`),
  KEY `UID` (`UID`),
  CONSTRAINT `skills_ibfk_1` FOREIGN KEY (`UID`) REFERENCES `basic_info` (`UID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `skills`
--

LOCK TABLES `skills` WRITE;
/*!40000 ALTER TABLE `skills` DISABLE KEYS */;
INSERT INTO `skills` VALUES (1,'PYTHON',2,2,1),(2,'WEB DEVELOPMENT',1,2,1),(3,'C',1,1,1),(4,'JAVA',2,1,2),(5,'APP DEVELOPMENT',1,1,2),(6,'APP DEVELOPMENT',2,1,3),(7,'PYTHON',2,1,3),(8,'DBMS',1,2,3),(9,'C',2,1,4),(10,'DBMS',1,1,4),(11,'C++',2,1,5),(12,'JAVA',2,2,5),(13,'CYBER SECURITY',1,1,5),(14,'C++',1,1,6),(15,'CYBER SECURITY',1,2,6);
/*!40000 ALTER TABLE `skills` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-01-09 18:21:20
