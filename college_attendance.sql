-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: college
-- ------------------------------------------------------
-- Server version	8.0.23

DROP TABLE IF EXISTS `attendance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attendance` (
  `idattendance` int NOT NULL AUTO_INCREMENT,
  `username` varchar(45) DEFAULT NULL,
  `date` varchar(45) DEFAULT NULL,
  `status` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`idattendance`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `attendance`
--

LOCK TABLES `attendance` WRITE;
INSERT INTO `attendance` VALUES (1,'mark','01/01/2022','P'),(2,'sony','01/01/2022','A'),(3,'abc','01/01/2022','L'),(4,'shuvo','01/01/2022','P'),(5,'(\'mark\',)','02/01/2022','L'),(6,'mark','02/01/2022','A'),(7,'sony','02/01/2022','A'),(8,'abc','02/01/2022','P'),(9,'shuvo','02/01/2022','L');

-- Dump completed on 2022-01-02 11:17:04
