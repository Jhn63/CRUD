-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: base
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `productCod` int NOT NULL,
  `productName` varchar(50) NOT NULL,
  `productMeasure` varchar(50) NOT NULL,
  `productBrand` varchar(50) NOT NULL,
  `productPrice` float NOT NULL,
  PRIMARY KEY (`productCod`),
  UNIQUE KEY `productCod` (`productCod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (100,'Leite Integral','1 Litro','Betânia',6.5),(101,'Leite Integral','1 Litro','Italac',8),(102,'Achocolatado','200 g','Nescau',3.5),(103,'Cafe','500 g','Pilao',10),(104,'Feijao','1 kg','Cometa',8),(105,'Cafe','500 g','Santa Clara',10),(106,'Amido de milho','200 g','Maizena',4.5),(107,'Agua mineral','500 g','Cristal',2),(108,'Creme Dental','180 g','Colgate Palmolive',7),(109,'Leite em pó','250 g','Ninho',15),(110,'Arroz Branco','1 kg','Camil',6.8),(111,'Leite Desnatado','1 Litro','Piracanjuba',5),(112,'Creme de Leite','200 g','Italac',4),(113,'Arroz Parboilizado','1 kg','Camil',6.7),(114,'Arroz Parboilizado','1 kg','Qualitá',5.8),(115,'Macarrão','500 g','Barilla',11),(116,'Macarrão','500 g','Galo',3.5),(117,'Azeite de Oliva','500 ml','Galo',28.9),(118,'Azeite de Oliva','450','O-LIVE',24.5),(119,'Azeite de Oliva','500 ml','Andorinha',33),(120,'Açucar Refinado','1 kg','Qualitá',2.8),(121,'Açucar Refinado','1 kg','União',5.2),(122,'Açucar Mascavo','500 g','Minamel',7),(123,'Detergente Neutro','500 ml','Ypê',3.4),(124,'Iogurte sabor Morango','900 g','Betânia',14),(125,'Iogurte sabor Ameixa','900 g','Betânia',14),(126,'Leite Condensado','395 g','Betânia',5.1),(127,'Açucar Cristal','1 kg','Alegre',4);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-04  9:40:31
