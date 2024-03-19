-- MariaDB dump 10.19  Distrib 10.11.6-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: project_dbws
-- ------------------------------------------------------
-- Server version	10.11.6-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `diabetes_patient`
--

DROP TABLE IF EXISTS `diabetes_patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `diabetes_patient` (
  `health_insurance` varchar(50) DEFAULT NULL,
  `is_high_chol` tinyint(1) DEFAULT NULL,
  `BMI` float DEFAULT NULL,
  `phys_active` tinyint(1) DEFAULT NULL,
  `phys_health` tinyint(1) DEFAULT NULL,
  `high_bp` tinyint(1) DEFAULT NULL,
  KEY `health_insurance` (`health_insurance`),
  CONSTRAINT `diabetes_patient_ibfk_1` FOREIGN KEY (`health_insurance`) REFERENCES `patient` (`health_insurance`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `diabetes_patient`
--

LOCK TABLES `diabetes_patient` WRITE;
/*!40000 ALTER TABLE `diabetes_patient` DISABLE KEYS */;
/*!40000 ALTER TABLE `diabetes_patient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctor`
--

DROP TABLE IF EXISTS `doctor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `doctor` (
  `doctor_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `Specification` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`doctor_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `doctor_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor`
--

LOCK TABLES `doctor` WRITE;
/*!40000 ALTER TABLE `doctor` DISABLE KEYS */;
/*!40000 ALTER TABLE `doctor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `general_practitioner`
--

DROP TABLE IF EXISTS `general_practitioner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `general_practitioner` (
  `doctor_id` int(11) DEFAULT NULL,
  `responsibility_area` varchar(255) DEFAULT NULL,
  KEY `doctor_id` (`doctor_id`),
  CONSTRAINT `general_practitioner_ibfk_1` FOREIGN KEY (`doctor_id`) REFERENCES `doctor` (`doctor_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `general_practitioner`
--

LOCK TABLES `general_practitioner` WRITE;
/*!40000 ALTER TABLE `general_practitioner` DISABLE KEYS */;
/*!40000 ALTER TABLE `general_practitioner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hypertension_patient`
--

DROP TABLE IF EXISTS `hypertension_patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hypertension_patient` (
  `health_insurance` varchar(50) DEFAULT NULL,
  `chest_pain_type` int(11) DEFAULT NULL,
  `resting_blood_pr` float DEFAULT NULL,
  `cholesterol` float DEFAULT NULL,
  `fasting_bld_sugar` int(11) DEFAULT NULL,
  `rest_ecg` int(11) DEFAULT NULL,
  `exrc_induced_ang` int(11) DEFAULT NULL,
  `max_heart_rate` int(11) DEFAULT NULL,
  KEY `health_insurance` (`health_insurance`),
  CONSTRAINT `hypertension_patient_ibfk_1` FOREIGN KEY (`health_insurance`) REFERENCES `patient` (`health_insurance`) ON DELETE CASCADE,
  CONSTRAINT `CONSTRAINT_1` CHECK (`chest_pain_type` >= 0 and `chest_pain_type` <= 3),
  CONSTRAINT `CONSTRAINT_2` CHECK (`fasting_bld_sugar` >= 0 and `fasting_bld_sugar` <= 1),
  CONSTRAINT `CONSTRAINT_3` CHECK (`rest_ecg` >= 0 and `rest_ecg` <= 2),
  CONSTRAINT `CONSTRAINT_4` CHECK (`exrc_induced_ang` >= 0 and `exrc_induced_ang` <= 1)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hypertension_patient`
--

LOCK TABLES `hypertension_patient` WRITE;
/*!40000 ALTER TABLE `hypertension_patient` DISABLE KEYS */;
/*!40000 ALTER TABLE `hypertension_patient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `monitor`
--

DROP TABLE IF EXISTS `monitor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `monitor` (
  `doctor` int(11) DEFAULT NULL,
  `patient` varchar(50) DEFAULT NULL,
  KEY `doctor` (`doctor`),
  KEY `patient` (`patient`),
  CONSTRAINT `monitor_ibfk_1` FOREIGN KEY (`doctor`) REFERENCES `general_practitioner` (`doctor_id`) ON DELETE CASCADE,
  CONSTRAINT `monitor_ibfk_2` FOREIGN KEY (`patient`) REFERENCES `patient` (`health_insurance`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `monitor`
--

LOCK TABLES `monitor` WRITE;
/*!40000 ALTER TABLE `monitor` DISABLE KEYS */;
/*!40000 ALTER TABLE `monitor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `others_doctors`
--

DROP TABLE IF EXISTS `others_doctors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `others_doctors` (
  `doctor_id` int(11) DEFAULT NULL,
  `specification` enum('stroke','hypertension','diabetes') DEFAULT NULL,
  KEY `doctor_id` (`doctor_id`),
  CONSTRAINT `others_doctors_ibfk_1` FOREIGN KEY (`doctor_id`) REFERENCES `doctor` (`doctor_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `others_doctors`
--

LOCK TABLES `others_doctors` WRITE;
/*!40000 ALTER TABLE `others_doctors` DISABLE KEYS */;
/*!40000 ALTER TABLE `others_doctors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient`
--

DROP TABLE IF EXISTS `patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `patient` (
  `health_insurance` varchar(50) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `area` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`health_insurance`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `patient_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient`
--

LOCK TABLES `patient` WRITE;
/*!40000 ALTER TABLE `patient` DISABLE KEYS */;
/*!40000 ALTER TABLE `patient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `report`
--

DROP TABLE IF EXISTS `report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `report` (
  `report_id` int(11) NOT NULL AUTO_INCREMENT,
  `from` int(11) DEFAULT NULL,
  `to` int(11) DEFAULT NULL,
  PRIMARY KEY (`report_id`),
  KEY `from` (`from`),
  KEY `to` (`to`),
  CONSTRAINT `report_ibfk_1` FOREIGN KEY (`from`) REFERENCES `others_doctors` (`doctor_id`) ON DELETE CASCADE,
  CONSTRAINT `report_ibfk_2` FOREIGN KEY (`to`) REFERENCES `general_practitioner` (`doctor_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `report`
--

LOCK TABLES `report` WRITE;
/*!40000 ALTER TABLE `report` DISABLE KEYS */;
/*!40000 ALTER TABLE `report` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stroke_patient`
--

DROP TABLE IF EXISTS `stroke_patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stroke_patient` (
  `health_insurance` varchar(50) DEFAULT NULL,
  `avg_glucose_lvl` float DEFAULT NULL,
  `BMI` float DEFAULT NULL,
  `heart_disease` tinyint(1) DEFAULT NULL,
  `smoking_status` tinyint(1) DEFAULT NULL,
  KEY `health_insurance` (`health_insurance`),
  CONSTRAINT `stroke_patient_ibfk_1` FOREIGN KEY (`health_insurance`) REFERENCES `patient` (`health_insurance`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stroke_patient`
--

LOCK TABLES `stroke_patient` WRITE;
/*!40000 ALTER TABLE `stroke_patient` DISABLE KEYS */;
/*!40000 ALTER TABLE `stroke_patient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `surname` varchar(255) DEFAULT NULL,
  `sex` char(1) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-24 22:36:44
