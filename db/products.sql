-- MariaDB dump 10.17  Distrib 10.4.6-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: products
-- ------------------------------------------------------
-- Server version	10.4.6-MariaDB

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
-- Table structure for table `product_detail`
--

DROP TABLE IF EXISTS `product_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product_detail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `stock` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  `supplier` varchar(30) NOT NULL,
  `description` varchar(200) NOT NULL,
  `time_added` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_detail`
--

/*LOCK TABLES `product_detail` WRITE;
/*!40000 ALTER TABLE `product_detail` DISABLE KEYS */;
INSERT INTO `product_detail` VALUES (1,'Cowboy Hat Yeehaw',25,250000,'PT Koboi Kobokan','A classic yet classy hat, already worn by Indiana Jones!','2020-12-12 19:57:29'),(2,'Brown Pants X-276',45,100000,'PT Maju Mundur','You don\'t wanna miss this comfortable pants, suitable for casual walking and parties!','2020-12-12 19:58:15'),(3,'Jonas\' Yellow Raincoat from DARK',1,1000000,'Netflix Deutschland','The one and only jacket used by Jonas in DARK season 1, 2, and 3. This jacket has been through all the rains in Winden!','2020-12-12 19:58:58'),(4,'Baseball Cap H-121',30,250000,'PT Berang Berang','A number one cap for sure for baseball lovers!','2020-12-12 20:01:56'),(5,'Blue Jeans Tennessee',24,480000,'PT Barnum','Blue tight jeans of highest quality','2020-12-12 20:02:46'),(6,'Manchester United 3rd Kit',15,950000,'Manchester United F.C','Feel like zebra!','2020-12-12 20:04:25'),(7,'Manchester United Away Kit',15,800000,'Manchester United F.C','A lil bit cooler than the 3rd one!','2020-12-12 20:05:05'),(8,'Fatty Sneakers',1,480000,'Tafia Alifianty','Shoes of highest quality!','2020-12-12 20:05:32'),(9,'Soldier Cap',1,150000,'TNI','Limited edition!','2020-12-12 20:06:13'),(10,'Otis Milburn Jacket',1,1200000,'Netflix UK','-','2020-12-12 20:06:41');
/*!40000 ALTER TABLE `product_detail` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-15  0:12:08
