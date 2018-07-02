-- MySQL dump 10.13  Distrib 5.6.40, for Linux (x86_64)
--
-- Host: localhost    Database: gistandard
-- ------------------------------------------------------
-- Server version	5.6.40

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `adm_asset`
--

DROP TABLE IF EXISTS `adm_asset`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `adm_asset` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `assetNum` varchar(128) NOT NULL,
  `brand` varchar(20) DEFAULT NULL,
  `model` varchar(30) NOT NULL,
  `warehouse` varchar(20) NOT NULL,
  `price` int(11) DEFAULT NULL,
  `buyDate` date NOT NULL,
  `warrantyDate` date NOT NULL,
  `status` varchar(20) NOT NULL,
  `customer` varchar(80) DEFAULT NULL,
  `operator` varchar(20) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `desc` longtext,
  `assetType_id` int(11) DEFAULT NULL,
  `owner_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `adm_asset_assetType_id_8ff054dc_fk_adm_assettype_id` (`assetType_id`),
  KEY `adm_asset_owner_id_7dbcc0e1_fk_users_userprofile_id` (`owner_id`),
  CONSTRAINT `adm_asset_assetType_id_8ff054dc_fk_adm_assettype_id` FOREIGN KEY (`assetType_id`) REFERENCES `adm_assettype` (`id`),
  CONSTRAINT `adm_asset_owner_id_7dbcc0e1_fk_users_userprofile_id` FOREIGN KEY (`owner_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adm_asset`
--

LOCK TABLES `adm_asset` WRITE;
/*!40000 ALTER TABLE `adm_asset` DISABLE KEYS */;
INSERT INTO `adm_asset` VALUES (1,'SN012122681453','微软','surface Pro','0',8200,'2018-05-10','2020-05-10','1',NULL,'陈晨','2018-06-21 12:31:45.538531','',1,32),(2,'NT008912831','网御星云','FW2100','0',100000,'2017-03-20','2020-03-20','1','林城市技侦支队：荣誉：1862532332','陈晨','2018-06-21 12:38:25.944720','公司测试用设备',2,33);
/*!40000 ALTER TABLE `adm_asset` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `adm_assetfile`
--

DROP TABLE IF EXISTS `adm_assetfile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `adm_assetfile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `upload_user` varchar(20) NOT NULL,
  `file_content` varchar(100) DEFAULT NULL,
  `add_time` datetime(6) NOT NULL,
  `asset_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `adm_assetfile_asset_id_60c8e487_fk_adm_asset_id` (`asset_id`),
  CONSTRAINT `adm_assetfile_asset_id_60c8e487_fk_adm_asset_id` FOREIGN KEY (`asset_id`) REFERENCES `adm_asset` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adm_assetfile`
--

LOCK TABLES `adm_assetfile` WRITE;
/*!40000 ALTER TABLE `adm_assetfile` DISABLE KEYS */;
INSERT INTO `adm_assetfile` VALUES (1,'陈晨','asset_file/2018/06/surface.jpg','2018-06-21 12:33:15.831878',1),(2,'陈晨','asset_file/2018/06/surface01.jpg','2018-06-21 12:35:06.422585',1),(3,'陈晨','asset_file/2018/06/fw01.jpg','2018-06-21 12:38:42.592305',2);
/*!40000 ALTER TABLE `adm_assetfile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `adm_assetlog`
--

DROP TABLE IF EXISTS `adm_assetlog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `adm_assetlog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `operator` varchar(20) NOT NULL,
  `desc` longtext NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `asset_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `adm_assetlog_asset_id_66a32c81_fk_adm_asset_id` (`asset_id`),
  CONSTRAINT `adm_assetlog_asset_id_66a32c81_fk_adm_asset_id` FOREIGN KEY (`asset_id`) REFERENCES `adm_asset` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adm_assetlog`
--

LOCK TABLES `adm_assetlog` WRITE;
/*!40000 ALTER TABLE `adm_assetlog` DISABLE KEYS */;
INSERT INTO `adm_assetlog` VALUES (1,'陈晨','\n            用户信息：None  || 责任人：张晓明  || 资产状态：在用','2018-06-21 16:20:59.000000',1),(2,'陈晨','\n            用户信息：京州市检察院：吕梁贤： 18632598521  || 责任人：张晓明  || 资产状态：在用','2018-05-03 16:39:18.000000',2),(3,'陈晨','\n            用户信息：京州市中级人民法院：宋荣辉：16832356323  || 责任人：孙宏宇  || 资产状态：在用','2018-06-02 08:40:14.000000',2),(4,'陈晨','\n            用户信息：林城市技侦支队：荣誉：1862532332  || 责任人：孙宏宇  || 资产状态：在用','2018-06-21 12:41:18.084277',2);
/*!40000 ALTER TABLE `adm_assetlog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `adm_assettype`
--

DROP TABLE IF EXISTS `adm_assettype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `adm_assettype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `desc` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adm_assettype`
--

LOCK TABLES `adm_assettype` WRITE;
/*!40000 ALTER TABLE `adm_assettype` DISABLE KEYS */;
INSERT INTO `adm_assettype` VALUES (1,'办公电脑',''),(2,'防火墙',''),(3,'数据库审计',''),(4,'授权文件','');
/*!40000 ALTER TABLE `adm_assettype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `adm_customer`
--

DROP TABLE IF EXISTS `adm_customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `adm_customer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `unit` varchar(50) NOT NULL,
  `address` varchar(100) NOT NULL,
  `name` varchar(20) NOT NULL,
  `phone` varchar(30) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `desc` longtext,
  `add_time` datetime(6) NOT NULL,
  `belongs_to_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `adm_customer_belongs_to_id_e4e83cb1_fk_users_userprofile_id` (`belongs_to_id`),
  CONSTRAINT `adm_customer_belongs_to_id_e4e83cb1_fk_users_userprofile_id` FOREIGN KEY (`belongs_to_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adm_customer`
--

LOCK TABLES `adm_customer` WRITE;
/*!40000 ALTER TABLE `adm_customer` DISABLE KEYS */;
INSERT INTO `adm_customer` VALUES (1,'林城市出入境检验检疫局','林城市润扬中路128号','黄亮','136259852562',1,'','2018-06-21 12:03:31.869720',32),(2,'林城汇丰银行','林城区开放路113号','万山','16985623651',1,'','2018-06-21 12:07:04.131528',32),(3,'林城华瑞机电有限公司','林城八桥北路68号','邢学文','16896539851',1,'','2018-06-21 12:08:31.683875',32),(4,'晨光集团（京州）有限公司','京州市环城北路12号','林海','185269865211',1,'','2018-06-21 12:10:26.453175',33),(5,'京州市政府信息中心','京州市永嘉路市政府大厦','陆路','15636985656',1,'','2018-06-21 12:11:47.480796',33),(6,'吕州市公安局','吕州市平安路9号','聂永辉','15638956235',1,'','2018-06-21 12:13:38.713749',34),(7,'吕州市地税局','吕州市楚桥北路126号','赵云','15369865322',1,'','2018-06-21 12:15:12.941428',34),(8,'京州市嘉禾政通文化传媒有限公司','京州市丰台路290号','吕鑫鑫','1563589892',1,'','2018-06-21 12:22:03.000953',35),(9,'京州市金融服务中心','京州市虎踞南路240号','王旭','16853565235',1,'','2018-06-21 12:24:31.697595',35);
/*!40000 ALTER TABLE `adm_customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `adm_equipment`
--

DROP TABLE IF EXISTS `adm_equipment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `adm_equipment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` varchar(30) NOT NULL,
  `equipment_model` varchar(50) NOT NULL,
  `buy_date` date NOT NULL,
  `warranty_date` date NOT NULL,
  `config_desc` longtext,
  `customer_id` int(11) DEFAULT NULL,
  `equipment_type_id` int(11) DEFAULT NULL,
  `supplier_id` int(11) DEFAULT NULL,
  `accounting` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `adm_equipment_customer_id_b2df97df_fk_adm_customer_id` (`customer_id`),
  KEY `adm_equipment_equipment_type_id_51991b84_fk_adm_equipmenttype_id` (`equipment_type_id`),
  KEY `adm_equipment_supplier_id_1681cded_fk_adm_supplier_id` (`supplier_id`),
  CONSTRAINT `adm_equipment_customer_id_b2df97df_fk_adm_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `adm_customer` (`id`),
  CONSTRAINT `adm_equipment_equipment_type_id_51991b84_fk_adm_equipmenttype_id` FOREIGN KEY (`equipment_type_id`) REFERENCES `adm_equipmenttype` (`id`),
  CONSTRAINT `adm_equipment_supplier_id_1681cded_fk_adm_supplier_id` FOREIGN KEY (`supplier_id`) REFERENCES `adm_supplier` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=416 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adm_equipment`
--

LOCK TABLES `adm_equipment` WRITE;
/*!40000 ALTER TABLE `adm_equipment` DISABLE KEYS */;
INSERT INTO `adm_equipment` VALUES (1,'NT00126767','Power V-1424','2012-03-16','2015-04-10','None',1,1,NULL,0),(2,'NT00121686','N120','2012-01-04','2015-04-10','None',9,3,NULL,0),(3,'NT00126222','Power V-320IPS','2012-02-29','2015-04-10','None',9,4,NULL,0),(4,'NT00175974','Power V6000-F53EC-N','2014-04-21','2017-04-21','None',1,1,NULL,1),(5,'NT00179830','SIS-3000-Z1101-H','2014-06-09','2017-06-09',NULL,1,2,NULL,1),(6,'NT00133081','SAG-1100','2012-11-22','2015-11-22','None',9,9,NULL,0),(7,'NT00133079','SAG-1100','2012-07-20','2015-07-20','None',8,9,NULL,0),(8,'NT00229406','Power V6000-F832C-N','2015-11-25','2018-11-25','None',7,1,NULL,0),(9,'NT00140770','Leadsec-C5000','2015-11-13','2018-11-13','None',7,5,NULL,0),(10,'NT00923425','power v6000-F8350','2008-11-17','2011-11-17','None',6,1,NULL,0),(11,'NT00141619','Leadsec-100WAF','2012-11-20','2015-11-20','None',5,10,NULL,0),(12,'NT00142146','Power V-8400C','2012-10-12','2015-10-12','None',5,1,NULL,0),(13,'NT00091658','Power V-322A-H','2010-12-30','2013-12-30','None',4,1,NULL,0),(14,'NT00245965','Power V6000-F23DS-DC','2016-07-21','2019-07-21','None',3,1,NULL,0),(15,'NT00251297','TS-SC1040','2016-09-23','2019-09-23','None',2,14,NULL,1),(16,'NT00252794','power v6000-F8350','2016-09-28','2019-09-28',NULL,2,1,NULL,1),(17,'NT00245819','leadsecACM-C2580','2016-09-23','2019-09-23','None',1,5,NULL,0),(18,'NT00307434','ISM—TX-CONPR','2016-10-07','2019-10-07','None',1,8,NULL,0),(19,'NT00232734','power v6000-F3330','2015-12-22','2018-12-22','None',3,1,NULL,0);
/*!40000 ALTER TABLE `adm_equipment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `adm_equipment_service_info`
--

DROP TABLE IF EXISTS `adm_equipment_service_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `adm_equipment_service_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `equipment_id` int(11) NOT NULL,
  `serviceinfo_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `adm_equipment_service_in_equipment_id_serviceinfo_eb6d8cdc_uniq` (`equipment_id`,`serviceinfo_id`),
  KEY `adm_equipment_servic_serviceinfo_id_164b58fe_fk_adm_servi` (`serviceinfo_id`),
  CONSTRAINT `adm_equipment_servic_equipment_id_a2dc894b_fk_adm_equip` FOREIGN KEY (`equipment_id`) REFERENCES `adm_equipment` (`id`),
  CONSTRAINT `adm_equipment_servic_serviceinfo_id_164b58fe_fk_adm_servi` FOREIGN KEY (`serviceinfo_id`) REFERENCES `adm_serviceinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adm_equipment_service_info`
--

LOCK TABLES `adm_equipment_service_info` WRITE;
/*!40000 ALTER TABLE `adm_equipment_service_info` DISABLE KEYS */;
INSERT INTO `adm_equipment_service_info` VALUES (1,19,1),(2,19,2),(3,19,3),(4,19,4);
/*!40000 ALTER TABLE `adm_equipment_service_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `adm_equipmenttype`
--

DROP TABLE IF EXISTS `adm_equipmenttype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `adm_equipmenttype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `desc` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adm_equipmenttype`
--

LOCK TABLES `adm_equipmenttype` WRITE;
/*!40000 ALTER TABLE `adm_equipmenttype` DISABLE KEYS */;
INSERT INTO `adm_equipmenttype` VALUES (1,'防火墙',''),(2,'入侵检测',''),(3,'上网行为管理',''),(4,'堡垒机',''),(5,'Web应用安全防护',''),(6,'安全网关',''),(7,'VPN网关SAG',''),(8,'漏洞扫描',''),(9,'入侵检测',''),(10,'入侵防御',''),(11,'网闸',''),(12,'日志审计RS',''),(13,'内网安全管理',''),(14,'安全管理系统BSM','');
/*!40000 ALTER TABLE `adm_equipmenttype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `adm_serviceinfo`
--

DROP TABLE IF EXISTS `adm_serviceinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `adm_serviceinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` longtext NOT NULL,
  `is_reminding` tinyint(1) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `writer_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `adm_serviceinfo_writer_id_911d31a1_fk_users_userprofile_id` (`writer_id`),
  CONSTRAINT `adm_serviceinfo_writer_id_911d31a1_fk_users_userprofile_id` FOREIGN KEY (`writer_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adm_serviceinfo`
--

LOCK TABLES `adm_serviceinfo` WRITE;
/*!40000 ALTER TABLE `adm_serviceinfo` DISABLE KEYS */;
INSERT INTO `adm_serviceinfo` VALUES (1,'远程协助用户更新策略，新增加地址映射规则',0,'2018-05-16 10:58:07.000000',11),(2,'完成年中设备巡检工作，设备运行状态良好，设备还有半年质保就要到期，和用户介绍了下目前续保优惠政策',0,'2018-06-08 13:00:01.000000',11),(3,'整理巡检报告和配置备份资料，已经邮件发送给用户',0,'2018-06-08 14:00:26.000000',11),(4,'今天用户打电话咨询服务续保详情，已经转交给销售人员',0,'2018-06-14 16:01:06.000000',11);
/*!40000 ALTER TABLE `adm_serviceinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `adm_supplier`
--

DROP TABLE IF EXISTS `adm_supplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `adm_supplier` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `company` varchar(30) NOT NULL,
  `address` varchar(100) NOT NULL,
  `linkname` varchar(20) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `desc` longtext,
  `add_time` datetime(6) NOT NULL,
  `belongs_to_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `adm_supplier_belongs_to_id_f72b527a_fk_users_userprofile_id` (`belongs_to_id`),
  CONSTRAINT `adm_supplier_belongs_to_id_f72b527a_fk_users_userprofile_id` FOREIGN KEY (`belongs_to_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adm_supplier`
--

LOCK TABLES `adm_supplier` WRITE;
/*!40000 ALTER TABLE `adm_supplier` DISABLE KEYS */;
/*!40000 ALTER TABLE `adm_supplier` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can view group',2,'view_group'),(8,'Can view permission',1,'view_permission'),(9,'Can add content type',3,'add_contenttype'),(10,'Can change content type',3,'change_contenttype'),(11,'Can delete content type',3,'delete_contenttype'),(12,'Can view content type',3,'view_contenttype'),(13,'Can add session',4,'add_session'),(14,'Can change session',4,'change_session'),(15,'Can delete session',4,'delete_session'),(16,'Can view session',4,'view_session'),(17,'Can add 用户信息',5,'add_userprofile'),(18,'Can change 用户信息',5,'change_userprofile'),(19,'Can delete 用户信息',5,'delete_userprofile'),(20,'Can add 组织架构',6,'add_structure'),(21,'Can change 组织架构',6,'change_structure'),(22,'Can delete 组织架构',6,'delete_structure'),(23,'Can view 组织架构',6,'view_structure'),(24,'Can view 用户信息',5,'view_userprofile'),(25,'Can add 菜单',7,'add_menu'),(26,'Can change 菜单',7,'change_menu'),(27,'Can delete 菜单',7,'delete_menu'),(28,'Can add 角色',8,'add_role'),(29,'Can change 角色',8,'change_role'),(30,'Can delete 角色',8,'delete_role'),(31,'Can view 菜单',7,'view_menu'),(32,'Can view 角色',8,'view_role'),(33,'Can add 发件邮箱设置',9,'add_emailsetup'),(34,'Can change 发件邮箱设置',9,'change_emailsetup'),(35,'Can delete 发件邮箱设置',9,'delete_emailsetup'),(36,'Can add 系统设置',10,'add_systemsetup'),(37,'Can change 系统设置',10,'change_systemsetup'),(38,'Can delete 系统设置',10,'delete_systemsetup'),(39,'Can view 发件邮箱设置',9,'view_emailsetup'),(40,'Can view 系统设置',10,'view_systemsetup'),(41,'Can add 资产管理',11,'add_asset'),(42,'Can change 资产管理',11,'change_asset'),(43,'Can delete 资产管理',11,'delete_asset'),(44,'Can add asset file',12,'add_assetfile'),(45,'Can change asset file',12,'change_assetfile'),(46,'Can delete asset file',12,'delete_assetfile'),(47,'Can add asset log',13,'add_assetlog'),(48,'Can change asset log',13,'change_assetlog'),(49,'Can delete asset log',13,'delete_assetlog'),(50,'Can add 资产类型',14,'add_assettype'),(51,'Can change 资产类型',14,'change_assettype'),(52,'Can delete 资产类型',14,'delete_assettype'),(53,'Can add 客户管理',15,'add_customer'),(54,'Can change 客户管理',15,'change_customer'),(55,'Can delete 客户管理',15,'delete_customer'),(56,'Can add 设备管理',16,'add_equipment'),(57,'Can change 设备管理',16,'change_equipment'),(58,'Can delete 设备管理',16,'delete_equipment'),(59,'Can add 设备类型',17,'add_equipmenttype'),(60,'Can change 设备类型',17,'change_equipmenttype'),(61,'Can delete 设备类型',17,'delete_equipmenttype'),(62,'Can add service info',18,'add_serviceinfo'),(63,'Can change service info',18,'change_serviceinfo'),(64,'Can delete service info',18,'delete_serviceinfo'),(65,'Can add 分销商管理',19,'add_supplier'),(66,'Can change 分销商管理',19,'change_supplier'),(67,'Can delete 分销商管理',19,'delete_supplier'),(68,'Can view 资产管理',11,'view_asset'),(69,'Can view asset file',12,'view_assetfile'),(70,'Can view asset log',13,'view_assetlog'),(71,'Can view 资产类型',14,'view_assettype'),(72,'Can view 客户管理',15,'view_customer'),(73,'Can view 设备管理',16,'view_equipment'),(74,'Can view 设备类型',17,'view_equipmenttype'),(75,'Can view service info',18,'view_serviceinfo'),(76,'Can view 分销商管理',19,'view_supplier'),(77,'Can add 工单信息',20,'add_workorder'),(78,'Can change 工单信息',20,'change_workorder'),(79,'Can delete 工单信息',20,'delete_workorder'),(80,'Can add 执行记录',21,'add_workorderrecord'),(81,'Can change 执行记录',21,'change_workorderrecord'),(82,'Can delete 执行记录',21,'delete_workorderrecord'),(83,'Can view 工单信息',20,'view_workorder'),(84,'Can view 执行记录',21,'view_workorderrecord'),(85,'Can add Bookmark',22,'add_bookmark'),(86,'Can change Bookmark',22,'change_bookmark'),(87,'Can delete Bookmark',22,'delete_bookmark'),(88,'Can add log entry',23,'add_log'),(89,'Can change log entry',23,'change_log'),(90,'Can delete log entry',23,'delete_log'),(91,'Can add User Setting',24,'add_usersettings'),(92,'Can change User Setting',24,'change_usersettings'),(93,'Can delete User Setting',24,'delete_usersettings'),(94,'Can add User Widget',25,'add_userwidget'),(95,'Can change User Widget',25,'change_userwidget'),(96,'Can delete User Widget',25,'delete_userwidget');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (11,'adm','asset'),(12,'adm','assetfile'),(13,'adm','assetlog'),(14,'adm','assettype'),(15,'adm','customer'),(16,'adm','equipment'),(17,'adm','equipmenttype'),(18,'adm','serviceinfo'),(19,'adm','supplier'),(2,'auth','group'),(1,'auth','permission'),(3,'contenttypes','contenttype'),(20,'personal','workorder'),(21,'personal','workorderrecord'),(7,'rbac','menu'),(8,'rbac','role'),(4,'sessions','session'),(9,'system','emailsetup'),(10,'system','systemsetup'),(6,'users','structure'),(5,'users','userprofile'),(22,'xadmin','bookmark'),(23,'xadmin','log'),(24,'xadmin','usersettings'),(25,'xadmin','userwidget');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'rbac','0001_initial','2018-06-21 11:25:40.595724'),(2,'contenttypes','0001_initial','2018-06-21 11:25:40.784121'),(3,'contenttypes','0002_remove_content_type_name','2018-06-21 11:25:41.051960'),(4,'auth','0001_initial','2018-06-21 11:25:41.653589'),(5,'auth','0002_alter_permission_name_max_length','2018-06-21 11:25:41.772746'),(6,'auth','0003_alter_user_email_max_length','2018-06-21 11:25:41.840355'),(7,'auth','0004_alter_user_username_opts','2018-06-21 11:25:41.922543'),(8,'auth','0005_alter_user_last_login_null','2018-06-21 11:25:41.986986'),(9,'auth','0006_require_contenttypes_0002','2018-06-21 11:25:42.045986'),(10,'auth','0007_alter_validators_add_error_messages','2018-06-21 11:25:42.120336'),(11,'auth','0008_alter_user_username_max_length','2018-06-21 11:25:42.182379'),(12,'users','0001_initial','2018-06-21 11:25:43.703663'),(13,'adm','0001_initial','2018-06-21 11:25:44.826864'),(14,'adm','0002_auto_20180607_1211','2018-06-21 11:25:46.721973'),(15,'personal','0001_initial','2018-06-21 11:25:47.059342'),(16,'personal','0002_auto_20180607_1211','2018-06-21 11:25:48.020378'),(17,'sessions','0001_initial','2018-06-21 11:25:48.223433'),(18,'system','0001_initial','2018-06-21 11:25:48.483860'),(19,'xadmin','0001_initial','2018-06-21 11:25:49.478191');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('aessvv9cnhg34b1zxn11ngvyatatr9n6','MjA4OWI5MTZhOWI4YmFiOTU5MmVmOWFjOGRkYTAwMGQzZmE2ZjAxZDp7Il9hdXRoX3VzZXJfaWQiOiIzNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6InVzZXJzLnZpZXdzX3VzZXIuVXNlckJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwODBmNmYwMjE1Yjc1MmZkNjAxNDY4ZTQ5NDg3ZmIwNWQ0NTBkZjM3In0=','2018-06-21 15:11:50.509066'),('ih003iyanr9ffjfzl3ptltk8ifrjhpe8','OTk4MjM3OTg1OGE0NGJmYzE2M2E1N2RhYTBkMGUxZjE4YzkwZDVjYTp7Il9hdXRoX3VzZXJfaWQiOiIzMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6InVzZXJzLnZpZXdzX3VzZXIuVXNlckJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4YTE5ODkxZmUwZjkyNGM1MzRhZDYwNzQwMzJhZjY4YTgwMjE1OGFkIn0=','2018-06-21 14:05:15.082430');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personal_workorder`
--

DROP TABLE IF EXISTS `personal_workorder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `personal_workorder` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` varchar(10) NOT NULL,
  `title` varchar(50) NOT NULL,
  `type` varchar(10) NOT NULL,
  `status` varchar(10) NOT NULL,
  `do_time` datetime(6) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `content` varchar(300) NOT NULL,
  `file_content` varchar(100) DEFAULT NULL,
  `approver_id` int(11) DEFAULT NULL,
  `customer_id` int(11) NOT NULL,
  `proposer_id` int(11) DEFAULT NULL,
  `receiver_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `personal_workorder_approver_id_8151e1b9_fk_users_userprofile_id` (`approver_id`),
  KEY `personal_workorder_customer_id_784cd4e0_fk_adm_customer_id` (`customer_id`),
  KEY `personal_workorder_proposer_id_dbe7f650_fk_users_userprofile_id` (`proposer_id`),
  KEY `personal_workorder_receiver_id_b436f6a3_fk_users_userprofile_id` (`receiver_id`),
  CONSTRAINT `personal_workorder_approver_id_8151e1b9_fk_users_userprofile_id` FOREIGN KEY (`approver_id`) REFERENCES `users_userprofile` (`id`),
  CONSTRAINT `personal_workorder_customer_id_784cd4e0_fk_adm_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `adm_customer` (`id`),
  CONSTRAINT `personal_workorder_proposer_id_dbe7f650_fk_users_userprofile_id` FOREIGN KEY (`proposer_id`) REFERENCES `users_userprofile` (`id`),
  CONSTRAINT `personal_workorder_receiver_id_b436f6a3_fk_users_userprofile_id` FOREIGN KEY (`receiver_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personal_workorder`
--

LOCK TABLES `personal_workorder` WRITE;
/*!40000 ALTER TABLE `personal_workorder` DISABLE KEYS */;
INSERT INTO `personal_workorder` VALUES (1,'SX0000001','林城市出入境设备安装','0','5','2018-05-09 10:05:00.000000','2018-05-08 13:13:57.000000','运维审计设备已到货，麻烦安排工程师上门安装','',36,1,32,38),(2,'SX0000002','林城汇丰银行设备授权更新','1','5','2018-05-10 09:05:00.000000','2018-05-09 13:16:18.000000','设备授权更新-请支持','',36,2,32,37),(3,'SX0000003','测试工单数据','2','1','2018-05-17 09:30:00.000000','2018-05-16 13:18:07.000000','工单测数据','',36,2,32,NULL),(4,'SX0000004','工单测数据','2','5','2018-06-05 09:06:00.000000','2018-06-04 13:18:58.000000','工单测数据','',36,3,32,38),(5,'SX0000005','工单测数据','1','5','2018-06-08 02:06:00.000000','2018-06-04 13:20:53.000000','工单测数据','',36,2,32,37),(6,'SX0000006','工单测数据','1','5','2018-06-11 02:06:00.000000','2018-06-09 13:20:53.000000','工单测数据','',36,2,32,37),(7,'SX0000007','工单测数据','1','5','2018-06-09 02:06:00.000000','2018-06-14 13:20:53.000000','工单测数据','',36,2,32,37),(8,'SX0000008','工单测数据','1','0','2018-06-20 14:06:00.000000','2018-06-19 13:20:53.000000','工单测数据','',36,2,32,NULL),(9,'SX0000009','工单测数据','1','5','2018-06-19 12:06:00.000000','2018-06-18 13:20:53.000000','工单测数据','',36,2,32,38),(10,'SX0000010','晨光集团新设备安装','0','2','2018-05-31 21:00:00.000000','2018-05-29 13:42:19.000000','用户新设备安装，设备在网络出口，需要晚上才能停业务进行安装','',36,4,33,NULL),(11,'SX0000011','京州市政府信息安全建设交流','3','2','2018-05-31 09:00:00.000000','2018-05-23 13:43:22.000000','信息安全建设交流','',36,5,33,NULL),(12,'SX0000012','晨光集团远程协助','2','3','2018-06-05 09:06:00.000000','2018-06-02 13:44:00.000000','远程协助用户修改配置','',36,4,33,38),(13,'SX0000013','吕州市公安局安现场保障服务','1','4','2018-05-31 09:05:00.000000','2018-05-30 14:09:22.000000','重要时期现场保障工作','',36,6,34,37),(14,'SX0000014','吕州地税局新设备安装','0','4','2018-06-21 15:06:00.000000','2018-06-21 14:10:20.203729','新设备安装-记得等级新设备信息','',36,7,34,37),(15,'SX0000015','吕州市公安局防火墙安装','0','3','2018-06-26 13:06:00.000000','2018-06-21 14:11:47.630775','用户新购设备6月25日到货，请安排工程师上门安装','',36,6,34,37),(16,'SX0000016','嘉禾政通产品售前交流','3','2','2018-06-22 10:00:00.000000','2018-06-21 14:15:20.939831','用户新建机房，目前还没有相应的安全设备，请安排工程师去和用户交流安全建设方案','',36,8,35,NULL),(17,'SX0000017','金融服务中心技术支持','1','2','2018-06-25 13:00:00.000000','2018-06-21 14:16:56.701248','请协助用户进行网络调整','',36,9,35,NULL);
/*!40000 ALTER TABLE `personal_workorder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personal_workorderrecord`
--

DROP TABLE IF EXISTS `personal_workorderrecord`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `personal_workorderrecord` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `record_type` varchar(10) NOT NULL,
  `content` varchar(500) NOT NULL,
  `file_content` varchar(100) DEFAULT NULL,
  `add_time` datetime(6) NOT NULL,
  `name_id` int(11) NOT NULL,
  `work_order_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `personal_workorderre_name_id_cf06c8ba_fk_users_use` (`name_id`),
  KEY `personal_workorderre_work_order_id_fe6a58a9_fk_personal_` (`work_order_id`),
  CONSTRAINT `personal_workorderre_name_id_cf06c8ba_fk_users_use` FOREIGN KEY (`name_id`) REFERENCES `users_userprofile` (`id`),
  CONSTRAINT `personal_workorderre_work_order_id_fe6a58a9_fk_personal_` FOREIGN KEY (`work_order_id`) REFERENCES `personal_workorder` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personal_workorderrecord`
--

LOCK TABLES `personal_workorderrecord` WRITE;
/*!40000 ALTER TABLE `personal_workorderrecord` DISABLE KEYS */;
INSERT INTO `personal_workorderrecord` VALUES (1,'1','工单派发测数据','','2018-06-21 13:35:20.941536',36,8),(2,'1','请按时完成工单','','2018-06-21 13:36:21.729640',36,9),(3,'1','派发测试','','2018-06-21 13:38:51.804700',36,7),(4,'1','派发测试','','2018-06-21 13:39:07.238353',36,6),(5,'1','派发测试','','2018-06-21 13:39:18.897430',36,5),(6,'1','派发测试','','2018-06-21 13:39:29.157733',36,4),(7,'1','派发测试','','2018-06-21 13:39:44.918767',36,2),(8,'1','派发测试','','2018-06-21 13:39:57.670128',36,1),(9,'2','已完成','','2018-06-21 14:22:36.128198',38,9),(10,'2','已完成','','2018-06-21 14:22:56.744778',38,4),(11,'2','已完成','','2018-06-21 14:23:31.016831',38,1),(12,'2','已完成','','2018-06-21 14:24:36.123074',37,2),(13,'2','已完成','','2018-06-21 14:24:55.894044',37,5),(14,'2','已完成','','2018-06-21 14:25:08.511189',37,6),(15,'2','已完成','','2018-06-21 14:25:25.748616',37,7),(16,'1','和用户联系，合理安排时间','','2018-06-21 14:28:33.001004',36,12),(17,'1','去之前请联系用户安排好时间，同时将设备配置做好备份上传到系统','','2018-05-30 15:30:37.000000',36,13),(18,'1','已审批','','2018-06-21 14:32:08.473869',36,14),(19,'2','已完成现场保障工作，配置文件已上传','file/2018/06/吕州公安局配置备份.zip','2018-05-31 19:34:26.000000',37,13),(20,'3','已确认','','2018-06-21 14:36:33.970959',32,9),(21,'3','已确认','','2018-06-21 14:36:50.082712',32,7),(22,'3','确认完成','','2018-06-21 14:38:01.390088',32,6),(23,'3','确认完成','','2018-06-21 14:38:11.012101',32,5),(24,'3','确认完成','','2018-06-21 14:38:23.248166',32,4),(25,'3','确认完成','','2018-06-21 14:38:35.212884',32,2),(26,'3','确认完成','','2018-06-21 14:38:48.108647',32,1),(27,'2','设备已经安装部署完成，网络和业务测试都没有问题','file/2018/06/吕州市地税局设备安装报告.zip','2018-06-21 18:42:02.000000',37,14),(28,'0','用户暂时不需要上门服务','','2018-06-21 14:43:32.136738',37,8),(29,'1','联系用户，约好时间','','2018-06-21 14:45:57.194339',36,15);
/*!40000 ALTER TABLE `personal_workorderrecord` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rbac_menu`
--

DROP TABLE IF EXISTS `rbac_menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rbac_menu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(32) NOT NULL,
  `is_top` tinyint(1) NOT NULL,
  `icon` varchar(50) DEFAULT NULL,
  `code` varchar(50) DEFAULT NULL,
  `url` varchar(128) DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`),
  UNIQUE KEY `url` (`url`),
  KEY `rbac_menu_parent_id_60a5b178_fk_rbac_menu_id` (`parent_id`),
  CONSTRAINT `rbac_menu_parent_id_60a5b178_fk_rbac_menu_id` FOREIGN KEY (`parent_id`) REFERENCES `rbac_menu` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=90 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rbac_menu`
--

LOCK TABLES `rbac_menu` WRITE;
/*!40000 ALTER TABLE `rbac_menu` DISABLE KEYS */;
INSERT INTO `rbac_menu` VALUES (1,'系统',1,NULL,'SYSTEM','/system/',NULL),(2,'行政',1,NULL,'ADM','/adm/',NULL),(3,'人事',0,NULL,'PERSONNEL','/personnel/',NULL),(4,'流程',1,NULL,'FLOW','/flow/',NULL),(5,'我的工作台',0,NULL,'PERSONAL','/personal/',NULL),(6,'基础设置',0,'fa fa-gg','SYSTEM-BASIC',NULL,1),(7,'权限管理',0,'fa fa-user-plus','SYSTEM-RBAC',NULL,1),(8,'系统工具',0,'fa fa-wrench','SYSTEM-TOOLS',NULL,1),(9,'组织架构',0,NULL,'SYSTEM-BASIC-STRUCTURE','/system/basic/structure/',6),(10,'用户管理',0,NULL,'SYSTEM-BASIC-USER','/system/basic/user/',6),(11,'菜单管理',0,NULL,'SYSTEM-RBAC-MENU','/system/rbac/menu/',7),(12,'角色管理',0,NULL,'SYSTEM-RBAC-ROLE','/system/rbac/role/',7),(15,'组织架构：列表',0,NULL,'SYSTEM-BASIC-STRUCTURE-LIST','/system/basic/structure/list',9),(16,'组织架构：详情',0,NULL,'SYSTEM-BASIC-STRUCTURE-DETAIL','/system/basic/structure/detail',9),(17,'组织架构：删除',0,NULL,'SYSTEM-BASIC-STRUCTURE-DELETE','/system/basic/structure/delete',9),(18,'组织架构：关联用户',0,NULL,'SYSTEM-BASIC-STRUCTURE-ADD_USER','/system/basic/structure/add_user',9),(19,'用户管理：列表',0,NULL,'SYSTEM-BASIC-USER-LIST','/system/basic/user/list',10),(20,'用户管理：详情',0,NULL,'SYSTEM-BASIC-USER','/system/basic/user/detail',10),(21,'用户管理：修改',0,NULL,'SYSTEM-BASIC-USER-UPDATE','/system/basic/user/update',10),(22,'用户管理：创建',0,NULL,'SYSTEM-BASIC-USER-CREATE','/system/basic/user/create',10),(23,'用户管理：删除',0,NULL,'SYSTEM-BASIC-USER-DELETE','/system/basic/user/delete',10),(24,'用户管理：启用',0,NULL,'SYSTEM-BASIC-USER-ENABLE','/system/basic/user/enable',10),(25,'用户管理：禁用',0,NULL,'SYSTEM-BASIC-USER-DISABLE','/system/basic/user/disable',10),(26,'用户管理：修改用户密码',0,NULL,'SYSTEM-BASIC-USER-AdminPasswdChange','/system/basic/user/adminpasswdchange',10),(27,'角色管理：列表',0,NULL,'SYSTEM-RBAC-ROLE-LIST','/system/rbac/role/list',12),(28,'角色管理：详情-编辑',0,NULL,'SYSTEM-RBAC-ROLE-DETAIL','/system/rbac/role/detail',12),(29,'角色管理：删除',0,NULL,'SYSTEM-RBAC-ROLE-DELETE','/system/rbac/role/delete',12),(30,'角色管理：关联菜单',0,NULL,'SYSTEM-RBAC-ROLE-ROLE_MENU','/system/rbac/role/role_menu',12),(31,'角色管理：菜单列表',0,NULL,'SYSTEM-RBAC-ROLE-ROLE_MENU_LIST','/system/rbac/role/role_menu_list',12),(32,'角色管理：关联用户',0,NULL,'SYSTEM-RBAC-ROLE-ROLE_LIST','/system/rbac/role/role_user',12),(33,'菜单管理：列表',0,NULL,'SYSTEM-RBAC-MENU-LIST','/system/rbac/menu/list',11),(34,'系统设置',0,NULL,'SYSTEM-TOOLS-SYSTEM_SETUP','/system/tools/system_setup/',8),(35,'发件邮箱设置',0,NULL,'SYSTEM-TOOLS-EMAIL_SETUP','/system/tools/email_setup/',8),(36,'基础管理',0,'fa fa-gg','ADM-BSM',NULL,2),(37,'分销商管理',0,NULL,'ADM-BSM-SUPPLIER','/adm/bsm/supplier/',36),(38,'供应商管理：列表',0,NULL,'ADM-BSM-SUPPLIER-LIST','/adm/bsm/supplier/list',37),(39,'基础管理：详情-修改',0,NULL,'ADM-BSM-SUPPLIER-DETAIL','/adm/bsm/supplier/detail',37),(40,'供应商管理：删除',0,NULL,'ADM-BSM-SUPPLIER-DELETE','/adm/bsm/supplier/delete',37),(41,'资产类型',0,NULL,'ADM-BSM-ASSETTYPE','/adm/bsm/assettype/',36),(42,'资产类型：列表',0,NULL,'ADM-BSM-ASSETTYPE-LIST','/adm/bsm/assettype/list',41),(43,'资产类型：编辑-详情',0,NULL,'ADM-BSM-ASSETYPE-DETAIL','/adm/bsm/assettype/detail',41),(44,'资产类型：删除',0,NULL,'ADM-BSM-ASSETTYPE-DELETE','/adm/bsm/assettype/delete',41),(45,'客户信息',0,NULL,'ADM-BSM-CUSTOMER','/adm/bsm/customer/',36),(46,'客户信息：列表',0,NULL,'ADM-BSM-CUSTOMER-LIST','/adm/bsm/customer/list',45),(47,'客户信息：编辑-详情',0,NULL,'ADM-BSM-CUSTOMER-DETAIL','/adm/bsm/customer/detail',45),(48,'客户信息：删除',0,NULL,'ADM-BSM-CUSTOMER-DELETE','/adm/bsm/customer/delete',45),(49,'设备类型',0,NULL,'ADM-BSM-EQUIPMENTTYPE','/adm/bsm/equipmenttype/',36),(50,'资产管理',1,'fa fa-desktop','ADM-ASSET','/adm/asset/',2),(51,'设备管理',0,'fa fa-keyboard-o','ADM-EQUIPMENT','/adm/equipment/',2),(52,'用户管理：修改个人密码',0,NULL,'SYSTEM-BASIC-USER-PASSWDCHANGE','/system/basic/user/passwdchange',10),(53,'设备类型：列表',0,NULL,'ADM-BSM-EQUIPMENTTYPE-LIST','/adm/bsm/equipmenttype/list',49),(54,'设备类型：编辑-详情',0,NULL,'ADM-BSM-EQUIPMENTTYPE-DETAIL','/adm/bsm/equipmenttype/detail',49),(55,'设备类型：删除',0,NULL,'ADM-BSM-EQUIPMENTTYPE-DELETE','/adm/bsm/equipmenttype/delete',49),(56,'设备管理：列表',0,NULL,'ADM-EQUIPMENT-LIST','/adm/equipment/list',51),(57,'设备管理：新建-修改',0,NULL,'ADM-EQUIPMENT-CREATE','/adm/equipment/create',51),(58,'设备管理：删除',0,NULL,'ADM-EQUIPMENT-DELETE','/adm/equipment/delete',51),(59,'设备管理：详情',0,NULL,'ADM-EQUIPMENT-DETAIL','/adm/equipment/detail',51),(60,'设备管理：维保更新',0,NULL,'ADM-EQUIPMENT-SERVICEINFO','/adm/equipment/serviceinfoupdate',51),(61,'个人中心',0,'fa fa-user-plus','PERSONAL-USERINFO','/personal/userinfo',5),(62,'上传头像',0,NULL,'PERSONAL-USERINFO-UPLOADIMAGE','/personal/uploadimage',61),(63,'修改密码',0,NULL,'PERSONAL-USERINFO-PASSWORDCHANGE','/personal/passwordchange',61),(64,'内部通信',0,'fa fa-book','PERSONAL-PHONEBOOK','/personal/phonebook',5),(65,'菜单管理：详情-修改',0,NULL,'SYSTEM-RBAC-MENU-DETAIL','/system/rbac/menu/detail',11),(66,'工单管理',1,'fa fa-list-alt','PERSONAL-WORKORDER',NULL,5),(67,'我创建的工单',1,'fa fa-caret-right','PERSONAL-WORKORDER_ICRT','/personal/workorder_Icrt/',66),(68,'我创建的工单：创建',1,NULL,'PERSONAL-WORKORDER_ICRT-CREATE','/personal/workorder_Icrt/create',67),(69,'我创建的工单：列表',1,NULL,'PERSONAL-WORKORDER_ICRT-LIST','/personal/workorder_Icrt/list',67),(70,'我创建的工单：详情',1,NULL,'PERSONAL-WORKORDER-DETAIL','/personal/workorder_Icrt/detail',67),(71,'我创建的工单：删除',1,NULL,'PERSONAL-WORKORDER_ICRT-DELETE','/personal/workorder_Icrt/delete',67),(72,'我创建的工单：修改',1,NULL,'PERSONAL-WORKORDER-UPDATE','/personal/workorder_Icrt/update',67),(73,'我审批的工单',1,'fa fa-caret-right','PERSONAL-WORKORDER_APP','/personal/workorder_app/',66),(74,'我收到的工单',1,'fa fa-caret-right','PERSONAL-WORKORDER_REC','/personal/workorder_rec/',66),(75,'我审批的工单：派发',1,NULL,'PERSONAL-WORKORDER_APP-SEND','/personal/workorder_app/send',73),(76,'我收到的工单：执行',1,NULL,'PERSONAL-WORKORDER-EXECUTE','/personal/workorder_rec/execute',74),(77,'我收到的工单：确认',1,NULL,'PERSONAL-WORKORDER_REC-FINISH','/personal/workorder_rec/finish',74),(78,'资产管理：列表',1,NULL,'ADM-ASSET-LIST','/adm/asset/list',50),(79,'资产管理：创建',1,NULL,'ADM-ASSET-CREATE','/adm/asset/create',50),(80,'资产管理：修改',1,NULL,'ADM-ASSET-UPDATE','/adm/asset/update',50),(81,'资产管理：详情',1,NULL,'ADM-ASSET-DETAIL','/adm/asset/detail',50),(82,'资产管理：删除',1,NULL,'ADM-ASSET-DELETE','/adm/asset/delete',50),(83,'我创建的工单：上传项目资料',1,NULL,'PERSONAL-WORKORDER-PROJECT_UPLOAD','/personal/workorder_Icrt/upload',67),(84,'我收到的工单：上传配置资料',1,NULL,'PERSONAL-WORKORDER-UPLOAD','/personal/workorder_rec/upload',74),(85,'工单统计',1,NULL,'PERSONAL-WORKORDER-ALL','/personal/workorder_all/',66),(86,'资产管理：上传',1,NULL,'ADM-ASSET-UPLOAD','/adm/asset/upload',50),(87,'我收到的工单：退回',1,NULL,'PERSONAL-WORKORDER-RETURN','/personal/workorder_rec/return',74),(88,'工单文档',1,'fa  fa-folder','PERSONAL-DOCUMENT','/personal/document/',5),(89,'工单文档：列表',1,NULL,'PERSONAL-DOCUMENT-LIST','/personal/document/list',88);
/*!40000 ALTER TABLE `rbac_menu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rbac_role`
--

DROP TABLE IF EXISTS `rbac_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rbac_role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rbac_role`
--

LOCK TABLES `rbac_role` WRITE;
/*!40000 ALTER TABLE `rbac_role` DISABLE KEYS */;
INSERT INTO `rbac_role` VALUES (1,'系统'),(6,'行政'),(7,'人力'),(8,'技术'),(9,'销售'),(10,'管理'),(11,'核算'),(12,'审批');
/*!40000 ALTER TABLE `rbac_role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rbac_role_permissions`
--

DROP TABLE IF EXISTS `rbac_role_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rbac_role_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `role_id` int(11) NOT NULL,
  `menu_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `rbac_role_permissions_role_id_menu_id_8ba9f835_uniq` (`role_id`,`menu_id`),
  KEY `rbac_role_permissions_menu_id_bb73fb9a_fk_rbac_menu_id` (`menu_id`),
  CONSTRAINT `rbac_role_permissions_menu_id_bb73fb9a_fk_rbac_menu_id` FOREIGN KEY (`menu_id`) REFERENCES `rbac_menu` (`id`),
  CONSTRAINT `rbac_role_permissions_role_id_d10416cb_fk_rbac_role_id` FOREIGN KEY (`role_id`) REFERENCES `rbac_role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2874 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rbac_role_permissions`
--

LOCK TABLES `rbac_role_permissions` WRITE;
/*!40000 ALTER TABLE `rbac_role_permissions` DISABLE KEYS */;
INSERT INTO `rbac_role_permissions` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,1,5),(6,1,6),(7,1,7),(8,1,8),(9,1,9),(10,1,10),(11,1,11),(12,1,12),(59,1,15),(54,1,16),(55,1,17),(56,1,18),(57,1,19),(58,1,20),(60,1,21),(61,1,22),(62,1,23),(63,1,24),(64,1,25),(65,1,26),(68,1,27),(69,1,28),(70,1,29),(71,1,30),(72,1,31),(66,1,32),(67,1,33),(78,1,34),(79,1,35),(80,1,36),(81,1,37),(82,1,38),(83,1,39),(84,1,40),(85,1,41),(86,1,42),(87,1,43),(88,1,44),(276,1,45),(277,1,46),(278,1,47),(279,1,48),(371,1,52),(2305,6,2),(2325,6,5),(2306,6,36),(2307,6,37),(2308,6,38),(2309,6,41),(2310,6,42),(2311,6,43),(2312,6,45),(2313,6,46),(2314,6,49),(2316,6,50),(2322,6,51),(2315,6,53),(2323,6,56),(2324,6,59),(2326,6,61),(2327,6,62),(2328,6,63),(2329,6,64),(2330,6,66),(2331,6,67),(2332,6,68),(2333,6,69),(2334,6,70),(2335,6,71),(2336,6,72),(2338,6,74),(2339,6,76),(2340,6,77),(2317,6,78),(2318,6,79),(2319,6,80),(2320,6,81),(2337,6,83),(2341,6,84),(2321,6,86),(1505,7,2),(1525,7,5),(1506,7,36),(1507,7,37),(1508,7,38),(1509,7,39),(1510,7,41),(1511,7,42),(1512,7,43),(1513,7,45),(1514,7,46),(1515,7,47),(1516,7,49),(1519,7,50),(1520,7,51),(1517,7,53),(1518,7,54),(1521,7,56),(1522,7,57),(1523,7,59),(1524,7,60),(1526,7,61),(1527,7,62),(1528,7,63),(1529,7,64),(1530,7,66),(1531,7,67),(1532,7,68),(1533,7,69),(1534,7,70),(1535,7,71),(1536,7,72),(1537,7,74),(1538,7,76),(1539,7,77),(2790,8,2),(2812,8,5),(2791,8,36),(2792,8,37),(2793,8,38),(2794,8,39),(2795,8,41),(2796,8,42),(2797,8,43),(2798,8,45),(2799,8,46),(2800,8,47),(2801,8,49),(2804,8,50),(2807,8,51),(2802,8,53),(2803,8,54),(2808,8,56),(2809,8,57),(2810,8,59),(2811,8,60),(2813,8,61),(2814,8,62),(2815,8,63),(2816,8,64),(2817,8,66),(2818,8,67),(2819,8,68),(2820,8,69),(2821,8,70),(2822,8,71),(2823,8,72),(2825,8,74),(2826,8,76),(2827,8,77),(2805,8,78),(2806,8,81),(2824,8,83),(2828,8,84),(2829,8,87),(2830,8,88),(2831,8,89),(2832,9,2),(2854,9,5),(2833,9,36),(2834,9,37),(2835,9,38),(2836,9,39),(2837,9,41),(2838,9,42),(2839,9,43),(2840,9,45),(2841,9,46),(2842,9,47),(2843,9,49),(2846,9,50),(2849,9,51),(2844,9,53),(2845,9,54),(2850,9,56),(2851,9,57),(2852,9,59),(2853,9,60),(2855,9,61),(2856,9,62),(2857,9,63),(2858,9,64),(2859,9,66),(2860,9,67),(2861,9,68),(2862,9,69),(2863,9,70),(2864,9,71),(2865,9,72),(2867,9,74),(2868,9,76),(2869,9,77),(2847,9,78),(2848,9,81),(2866,9,83),(2870,9,84),(2871,9,87),(2872,9,88),(2873,9,89),(2705,10,1),(2736,10,2),(2767,10,5),(2706,10,6),(2722,10,7),(2733,10,8),(2707,10,9),(2712,10,10),(2723,10,11),(2726,10,12),(2708,10,15),(2709,10,16),(2710,10,17),(2711,10,18),(2713,10,19),(2714,10,20),(2715,10,21),(2716,10,22),(2717,10,23),(2718,10,24),(2719,10,25),(2720,10,26),(2727,10,27),(2728,10,28),(2729,10,29),(2730,10,30),(2731,10,31),(2732,10,32),(2724,10,33),(2734,10,34),(2735,10,35),(2737,10,36),(2738,10,37),(2739,10,38),(2740,10,39),(2741,10,40),(2742,10,41),(2743,10,42),(2744,10,43),(2745,10,44),(2746,10,45),(2747,10,46),(2748,10,47),(2749,10,48),(2750,10,49),(2754,10,50),(2761,10,51),(2721,10,52),(2751,10,53),(2752,10,54),(2753,10,55),(2762,10,56),(2763,10,57),(2764,10,58),(2765,10,59),(2766,10,60),(2768,10,61),(2769,10,62),(2770,10,63),(2771,10,64),(2725,10,65),(2772,10,66),(2773,10,67),(2774,10,68),(2775,10,69),(2776,10,70),(2777,10,71),(2778,10,72),(2780,10,73),(2782,10,74),(2781,10,75),(2783,10,76),(2784,10,77),(2755,10,78),(2756,10,79),(2757,10,80),(2758,10,81),(2759,10,82),(2779,10,83),(2785,10,84),(2787,10,85),(2760,10,86),(2786,10,87),(2788,10,88),(2789,10,89),(1945,12,5),(1946,12,66),(1947,12,73),(1948,12,75);
/*!40000 ALTER TABLE `rbac_role_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_emailsetup`
--

DROP TABLE IF EXISTS `system_emailsetup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `system_emailsetup` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `emailHost` varchar(30) NOT NULL,
  `emailPort` int(11) NOT NULL,
  `emailUser` varchar(100) NOT NULL,
  `emailPassword` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_emailsetup`
--

LOCK TABLES `system_emailsetup` WRITE;
/*!40000 ALTER TABLE `system_emailsetup` DISABLE KEYS */;
/*!40000 ALTER TABLE `system_emailsetup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_systemsetup`
--

DROP TABLE IF EXISTS `system_systemsetup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `system_systemsetup` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `loginTitle` varchar(20) DEFAULT NULL,
  `mainTitle` varchar(20) DEFAULT NULL,
  `headTitle` varchar(20) DEFAULT NULL,
  `copyright` varchar(100) DEFAULT NULL,
  `url` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_systemsetup`
--

LOCK TABLES `system_systemsetup` WRITE;
/*!40000 ALTER TABLE `system_systemsetup` DISABLE KEYS */;
INSERT INTO `system_systemsetup` VALUES (1,NULL,NULL,NULL,NULL,NULL),(2,'江苏沙河','SandBox','SandBox','江苏沙盒',NULL),(3,'江苏沙盒科技','SandBox','SandBox','江苏沙盒科技',NULL),(4,'江苏沙盒科技','SandBox','SandBox','Copyright © 2016-2017 江苏沙盒科技.Version1.0.1',NULL),(5,'江苏沙盒科技','SandBox','SandBox','Copyright © 2016-2017 江苏沙盒科技.Version1.0.1',NULL),(6,'江苏沙盒协同办公平台','SandBox','SandBox','Copyright © 2016-2017 江苏沙盒科技.Version1.0.1',NULL),(7,'江苏沙盒协同办公平台','SandBox','SandBox','Copyright © 2016-2017 江苏沙盒科技.Version2.0.2',NULL),(8,'沙盒协同办公平台','SandBox','SandBox','Copyright © 2016-2017 江苏沙盒科技.Version2.0.2',NULL),(9,'沙盒协同办公平台','SandBox','SandBox','Copyright © 2016-2017 江苏沙盒科技.Version2.0.3',NULL),(10,'沙盒协同办公平台','SandBox','SandBox','Copyright © 2016-2017 江苏沙盒科技.Version2.0.6',NULL),(11,'沙盒协同办公平台','SandBox','SandBox','Copyright © 2017-2018 江苏沙盒科技.Version2.0.6',NULL);
/*!40000 ALTER TABLE `system_systemsetup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_structure`
--

DROP TABLE IF EXISTS `users_structure`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_structure` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(60) NOT NULL,
  `type` varchar(20) NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `users_structure_parent_id_e73fd647_fk_users_structure_id` (`parent_id`),
  CONSTRAINT `users_structure_parent_id_e73fd647_fk_users_structure_id` FOREIGN KEY (`parent_id`) REFERENCES `users_structure` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_structure`
--

LOCK TABLES `users_structure` WRITE;
/*!40000 ALTER TABLE `users_structure` DISABLE KEYS */;
INSERT INTO `users_structure` VALUES (5,'汉东沙盒科技','firm',NULL),(9,'销售部','department',5),(10,'技术部','department',5),(11,'商务中心','department',5),(12,'行政中心','department',5),(13,'财务','department',9),(14,'车队','department',9),(15,'销售部-内','department',5);
/*!40000 ALTER TABLE `users_structure` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_userprofile`
--

DROP TABLE IF EXISTS `users_userprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `name` varchar(20) NOT NULL,
  `birthday` date DEFAULT NULL,
  `gender` varchar(10) NOT NULL,
  `mobile` varchar(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `joined_date` date DEFAULT NULL,
  `department_id` int(11) DEFAULT NULL,
  `superior_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `users_userprofile_department_id_b060d851_fk_users_structure_id` (`department_id`),
  KEY `users_userprofile_superior_id_3869391f_fk_users_userprofile_id` (`superior_id`),
  CONSTRAINT `users_userprofile_department_id_b060d851_fk_users_structure_id` FOREIGN KEY (`department_id`) REFERENCES `users_structure` (`id`),
  CONSTRAINT `users_userprofile_superior_id_3869391f_fk_users_userprofile_id` FOREIGN KEY (`superior_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_userprofile`
--

LOCK TABLES `users_userprofile` WRITE;
/*!40000 ALTER TABLE `users_userprofile` DISABLE KEYS */;
INSERT INTO `users_userprofile` VALUES (11,'pbkdf2_sha256$36000$WVAXQ2NaNvCV$tnXJU9EVveZYBBGQd8OOEqWygxKDndvj62w0Jdhcebk=','2018-06-21 14:44:24.726070',1,'admin','','',1,1,'2017-12-12 16:51:00.000000','管理员',NULL,'male','13813836955','admin@sandbox.com','image/2018/06/timg01.jpg',NULL,NULL,NULL,NULL),(32,'pbkdf2_sha256$36000$aRbfu1jfWnNj$tKWs2LPSrlqV1wOPGkMIAbB9TgOpB5uww/q++w5NEgs=','2018-06-21 14:36:14.981041',0,'zhangxiaoming','','',0,1,'2018-06-21 11:36:27.445102','张晓明',NULL,'male','13656987451','zhangxm@sandbox.com','image/2018/06/01.jpg','销售',NULL,9,NULL),(33,'pbkdf2_sha256$36000$jOOrfm2BmnTy$Y1pglbKwskyP5BTcvO7l6Yp694LKmvQ/+yDCQooVTH0=','2018-06-21 13:40:55.382428',0,'sunhongyu','','',0,1,'2018-06-21 11:38:06.558167','孙宏宇',NULL,'male','13853215981','sunhy@sandbox.com','image/default.jpg','销售',NULL,9,NULL),(34,'pbkdf2_sha256$36000$xd3zLx43ZSF2$vv61FnP3Wx3lwbMf6ikNcAFH2gIPvA3DjC9YHEH45/8=','2018-06-21 14:40:36.605475',0,'wanghonglin','','',0,1,'2018-06-21 11:41:40.227574','王鸿林',NULL,'male','13656869870','wanghl@sandbox.com','image/default.jpg','销售',NULL,9,NULL),(35,'pbkdf2_sha256$36000$OghgMPot4JjQ$OS8FGf/eWVBhTrYjxKOGkC4UnSgUodJNtiBwlJm42nk=','2018-06-21 14:12:28.607434',0,'lvliang','','',0,1,'2018-06-21 11:42:25.845580','吕梁',NULL,'male','15955763468','lvliang@sandbox.com','image/2018/06/05.jpg','销售',NULL,9,NULL),(36,'pbkdf2_sha256$36000$Nr6I27srX7EJ$fuQFiT2Uv/mUhYV9hoqMn8cZj0y523VZd71WvFvuIEI=','2018-06-21 14:45:30.981239',0,'zhenglu','','',0,1,'2018-06-21 11:44:27.005882','郑路',NULL,'male','15963833122','zhenglu@sandbox.com','image/2018/06/07.jpg','工程师',NULL,10,NULL),(37,'pbkdf2_sha256$36000$n3iyG1IwOViQ$x5+E9vE38n8cxlRzshFLyd333XzHtBEt+9ZoBKJNjWM=','2018-06-21 14:40:59.235108',0,'qiuhongyu','','',0,1,'2018-06-21 11:45:55.417890','邱宏宇',NULL,'male','13150645789','qiuhy@sandbox.com','image/2018/06/04.jpg','工程师',NULL,10,NULL),(38,'pbkdf2_sha256$36000$9yf9FG70jO3y$v4Yt3ORlmRc9/OLdXvaoEUb3ZkbZHt02RV6sd5FWdFg=','2018-06-21 14:32:35.406283',0,'hanfeng','','',0,1,'2018-06-21 11:48:20.291609','韩峰',NULL,'male','13602568911','hanfeng@sandbox.com','image/2018/06/06.jpg','工程师',NULL,10,NULL),(39,'pbkdf2_sha256$36000$inAttvJsZ9Dt$l1sYuGkUUgysOlAwBpI4KjvaVILEb62reKPJRf7y6yI=','2018-06-21 12:27:53.830592',0,'chenchen','','',0,1,'2018-06-21 12:27:40.311337','陈晨',NULL,'male','13689656865','chenchen@sandbox.com','image/default.jpg','商务',NULL,12,NULL);
/*!40000 ALTER TABLE `users_userprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_userprofile_groups`
--

DROP TABLE IF EXISTS `users_userprofile_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_userprofile_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_userprofile_groups_userprofile_id_group_id_823cf2fc_uniq` (`userprofile_id`,`group_id`),
  KEY `users_userprofile_groups_group_id_3de53dbf_fk_auth_group_id` (`group_id`),
  CONSTRAINT `users_userprofile_gr_userprofile_id_a4496a80_fk_users_use` FOREIGN KEY (`userprofile_id`) REFERENCES `users_userprofile` (`id`),
  CONSTRAINT `users_userprofile_groups_group_id_3de53dbf_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_userprofile_groups`
--

LOCK TABLES `users_userprofile_groups` WRITE;
/*!40000 ALTER TABLE `users_userprofile_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_userprofile_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_userprofile_roles`
--

DROP TABLE IF EXISTS `users_userprofile_roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_userprofile_roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_userprofile_roles_userprofile_id_role_id_81c255df_uniq` (`userprofile_id`,`role_id`),
  KEY `users_userprofile_roles_role_id_740e5521_fk_rbac_role_id` (`role_id`),
  CONSTRAINT `users_userprofile_ro_userprofile_id_ae49de2a_fk_users_use` FOREIGN KEY (`userprofile_id`) REFERENCES `users_userprofile` (`id`),
  CONSTRAINT `users_userprofile_roles_role_id_740e5521_fk_rbac_role_id` FOREIGN KEY (`role_id`) REFERENCES `rbac_role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_userprofile_roles`
--

LOCK TABLES `users_userprofile_roles` WRITE;
/*!40000 ALTER TABLE `users_userprofile_roles` DISABLE KEYS */;
INSERT INTO `users_userprofile_roles` VALUES (84,11,10),(85,32,9),(86,33,9),(87,34,9),(88,35,9),(94,36,10),(95,36,11),(99,36,12),(97,37,8),(98,38,8),(93,39,6);
/*!40000 ALTER TABLE `users_userprofile_roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_userprofile_user_permissions`
--

DROP TABLE IF EXISTS `users_userprofile_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_userprofile_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_userprofile_user_p_userprofile_id_permissio_d0215190_uniq` (`userprofile_id`,`permission_id`),
  KEY `users_userprofile_us_permission_id_393136b6_fk_auth_perm` (`permission_id`),
  CONSTRAINT `users_userprofile_us_permission_id_393136b6_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `users_userprofile_us_userprofile_id_34544737_fk_users_use` FOREIGN KEY (`userprofile_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_userprofile_user_permissions`
--

LOCK TABLES `users_userprofile_user_permissions` WRITE;
/*!40000 ALTER TABLE `users_userprofile_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_userprofile_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `xadmin_bookmark`
--

DROP TABLE IF EXISTS `xadmin_bookmark`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `xadmin_bookmark` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(128) NOT NULL,
  `url_name` varchar(64) NOT NULL,
  `query` varchar(1000) NOT NULL,
  `is_share` tinyint(1) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_bookmark_content_type_id_60941679_fk_django_co` (`content_type_id`),
  KEY `xadmin_bookmark_user_id_42d307fc_fk_users_userprofile_id` (`user_id`),
  CONSTRAINT `xadmin_bookmark_content_type_id_60941679_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `xadmin_bookmark_user_id_42d307fc_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `xadmin_bookmark`
--

LOCK TABLES `xadmin_bookmark` WRITE;
/*!40000 ALTER TABLE `xadmin_bookmark` DISABLE KEYS */;
/*!40000 ALTER TABLE `xadmin_bookmark` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `xadmin_log`
--

DROP TABLE IF EXISTS `xadmin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `xadmin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `ip_addr` char(39) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` varchar(32) NOT NULL,
  `message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_log_content_type_id_2a6cb852_fk_django_content_type_id` (`content_type_id`),
  KEY `xadmin_log_user_id_bb16a176_fk_users_userprofile_id` (`user_id`),
  CONSTRAINT `xadmin_log_content_type_id_2a6cb852_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `xadmin_log_user_id_bb16a176_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `xadmin_log`
--

LOCK TABLES `xadmin_log` WRITE;
/*!40000 ALTER TABLE `xadmin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `xadmin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `xadmin_usersettings`
--

DROP TABLE IF EXISTS `xadmin_usersettings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `xadmin_usersettings` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `key` varchar(256) NOT NULL,
  `value` longtext NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_usersettings_user_id_edeabe4a_fk_users_userprofile_id` (`user_id`),
  CONSTRAINT `xadmin_usersettings_user_id_edeabe4a_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `xadmin_usersettings`
--

LOCK TABLES `xadmin_usersettings` WRITE;
/*!40000 ALTER TABLE `xadmin_usersettings` DISABLE KEYS */;
INSERT INTO `xadmin_usersettings` VALUES (1,'dashboard:home:pos','',11);
/*!40000 ALTER TABLE `xadmin_usersettings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `xadmin_userwidget`
--

DROP TABLE IF EXISTS `xadmin_userwidget`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `xadmin_userwidget` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `page_id` varchar(256) NOT NULL,
  `widget_type` varchar(50) NOT NULL,
  `value` longtext NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_userwidget_user_id_c159233a_fk_users_userprofile_id` (`user_id`),
  CONSTRAINT `xadmin_userwidget_user_id_c159233a_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `xadmin_userwidget`
--

LOCK TABLES `xadmin_userwidget` WRITE;
/*!40000 ALTER TABLE `xadmin_userwidget` DISABLE KEYS */;
/*!40000 ALTER TABLE `xadmin_userwidget` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-06-21 14:54:22
