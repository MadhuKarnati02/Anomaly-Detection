/*
SQLyog Community Edition- MySQL GUI v7.15 
MySQL - 5.5.29 : Database - shiftallocation
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`shiftallocation` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `shiftallocation`;

/*Table structure for table `admin` */

DROP TABLE IF EXISTS `admin`;

CREATE TABLE `admin` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `mobile` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `admin` */

insert  into `admin`(`id`,`username`,`password`,`email`,`dob`,`address`,`mobile`) values (1,'bhushan','123','bhushan@gmail.com','2020-05-29','3-119,','0123456789');

/*Table structure for table `assignedprojects` */

DROP TABLE IF EXISTS `assignedprojects`;

CREATE TABLE `assignedprojects` (
  `sno` int(10) NOT NULL AUTO_INCREMENT,
  `proid` varchar(100) DEFAULT NULL,
  `projectname` varchar(100) DEFAULT NULL,
  `empid` varchar(100) DEFAULT NULL,
  `empname` varchar(100) DEFAULT NULL,
  `department` varchar(100) DEFAULT NULL,
  `designation` varchar(100) DEFAULT NULL,
  `shift` varchar(100) DEFAULT NULL,
  `status` varbinary(100) DEFAULT 'Pending',
  UNIQUE KEY `sno` (`sno`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `assignedprojects` */

insert  into `assignedprojects`(`sno`,`proid`,`projectname`,`empid`,`empname`,`department`,`designation`,`shift`,`status`) values (2,'312','python','emp111','bhuuuu','asdad','abc','a','pending');

/*Table structure for table `departments` */

DROP TABLE IF EXISTS `departments`;

CREATE TABLE `departments` (
  `sno` int(10) NOT NULL AUTO_INCREMENT,
  `depid` varchar(100) NOT NULL,
  `depname` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`sno`,`depid`),
  UNIQUE KEY `sno` (`sno`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `departments` */

insert  into `departments`(`sno`,`depid`,`depname`) values (1,'dep761','Developer'),(2,'dep567','asdad');

/*Table structure for table `projects` */

DROP TABLE IF EXISTS `projects`;

CREATE TABLE `projects` (
  `sno` int(10) NOT NULL AUTO_INCREMENT,
  `proid` varchar(100) NOT NULL,
  `proname` varchar(100) DEFAULT NULL,
  `start` date DEFAULT NULL,
  `deadline` date DEFAULT NULL,
  `status` varchar(100) DEFAULT 'Pending',
  PRIMARY KEY (`sno`,`proid`),
  UNIQUE KEY `sno` (`sno`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `projects` */

insert  into `projects`(`sno`,`proid`,`proname`,`start`,`deadline`,`status`) values (1,'pro229','python','2020-05-01','2020-05-31','Pending'),(2,'pro861','python','2020-05-01','2020-05-31','Pending'),(3,'pro900','python','2020-05-01','2020-05-31','Completed');

/*Table structure for table `requests` */

DROP TABLE IF EXISTS `requests`;

CREATE TABLE `requests` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `empid` varchar(100) DEFAULT NULL,
  `empname` varchar(100) DEFAULT NULL,
  `request` varchar(2000) DEFAULT NULL,
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `requests` */

insert  into `requests`(`id`,`empid`,`empname`,`request`) values (2,'emp1389','bhushan','            hello\r\n            ');

/*Table structure for table `shifts` */

DROP TABLE IF EXISTS `shifts`;

CREATE TABLE `shifts` (
  `sno` int(10) NOT NULL AUTO_INCREMENT,
  `shiftname` varchar(100) DEFAULT NULL,
  `starttime` time DEFAULT NULL,
  `endtime` time DEFAULT NULL,
  UNIQUE KEY `sno` (`sno`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `shifts` */

insert  into `shifts`(`sno`,`shiftname`,`starttime`,`endtime`) values (1,'a','06:00:00','14:00:00');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` varchar(10) NOT NULL,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `depid` varchar(10) DEFAULT 'Pending',
  `department` varchar(100) DEFAULT 'Pending',
  `designation` varchar(100) DEFAULT 'Pending',
  `dob` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `mobile` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`id`,`username`,`password`,`email`,`depid`,`department`,`designation`,`dob`,`address`,`mobile`) values ('emp1389','bhushan','123','thummalanageswararao234@gmail.com','dep761','Developer','SSE','2020-05-22','3-119, ','0123456789');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
