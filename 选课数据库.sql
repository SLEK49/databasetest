/*
SQLyog Enterprise v12.09 (64 bit)
MySQL - 5.5.40 : Database - system_choose_course
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`system_choose_course` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `system_choose_course`;

/*Table structure for table `adminpwd` */

DROP TABLE IF EXISTS `adminpwd`;

CREATE TABLE `adminpwd` (
  `id` varchar(12) DEFAULT NULL,
  `pwd` varchar(12) DEFAULT NULL,
  `name` varchar(12) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `adminpwd` */

insert  into `adminpwd`(`id`,`pwd`,`name`) values ('1','1234','AA'),('2','1234','AB'),('3','1234','AC'),('4','1234','AD');

/*Table structure for table `classroom` */

DROP TABLE IF EXISTS `classroom`;

CREATE TABLE `classroom` (
  `crId` varchar(12) NOT NULL,
  `crNum` int(11) DEFAULT NULL,
  PRIMARY KEY (`crId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `classroom` */

insert  into `classroom`(`crId`,`crNum`) values ('1',50),('2',100),('3',100),('4',50),('5',50);

/*Table structure for table `classroom_arr` */

DROP TABLE IF EXISTS `classroom_arr`;

CREATE TABLE `classroom_arr` (
  `crId` varchar(12) NOT NULL DEFAULT '',
  `cId` varchar(12) NOT NULL DEFAULT '',
  `cTime` varchar(12) DEFAULT NULL,
  PRIMARY KEY (`crId`,`cId`),
  KEY `cId` (`cId`),
  CONSTRAINT `classroom_arr_ibfk_1` FOREIGN KEY (`crId`) REFERENCES `classroom` (`crId`),
  CONSTRAINT `classroom_arr_ibfk_2` FOREIGN KEY (`cId`) REFERENCES `courseinfo` (`cId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `classroom_arr` */

insert  into `classroom_arr`(`crId`,`cId`,`cTime`) values ('1','3','周一1-2，周三7-8'),('2','5','周一3-4，周三5-6'),('3','4','周二1-2，周四7-8'),('4','1','周一7-8，周三3-4'),('5','2','周三1-2，周五3-4');

/*Table structure for table `courseinfo` */

DROP TABLE IF EXISTS `courseinfo`;

CREATE TABLE `courseinfo` (
  `cId` varchar(12) NOT NULL,
  `cName` varchar(12) DEFAULT NULL,
  `cIntro` varchar(50) DEFAULT NULL,
  `cHour` int(11) DEFAULT NULL,
  `cCredit` float DEFAULT NULL,
  `cWeek` varchar(12) DEFAULT NULL,
  PRIMARY KEY (`cId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `courseinfo` */

insert  into `courseinfo`(`cId`,`cName`,`cIntro`,`cHour`,`cCredit`,`cWeek`) values ('1','C','slightly',20,2,'1-6'),('2','java','slightly',25,3,'1-8'),('3','database','slightly',20,1,'1-10'),('4','algorithm','slightly',10,2.5,'6-12'),('5','python','slightly',30,2,'6-14');

/*Table structure for table `sc` */

DROP TABLE IF EXISTS `sc`;

CREATE TABLE `sc` (
  `sId` varchar(12) NOT NULL DEFAULT '',
  `cId` varchar(12) NOT NULL DEFAULT '',
  `grade` float DEFAULT NULL,
  PRIMARY KEY (`sId`,`cId`),
  KEY `cId` (`cId`),
  CONSTRAINT `sc_ibfk_1` FOREIGN KEY (`sId`) REFERENCES `studentinfo` (`sId`),
  CONSTRAINT `sc_ibfk_2` FOREIGN KEY (`cId`) REFERENCES `courseinfo` (`cId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `sc` */

insert  into `sc`(`sId`,`cId`,`grade`) values ('1001','1',NULL),('1001','2',NULL),('1001','3',NULL),('1001','4',NULL),('1001','5',NULL),('1002','1',NULL),('1002','2',NULL),('1002','3',NULL),('1002','4',NULL),('1002','5',NULL),('1003','3',NULL);

/*Table structure for table `studentinfo` */

DROP TABLE IF EXISTS `studentinfo`;

CREATE TABLE `studentinfo` (
  `sId` varchar(12) NOT NULL,
  `major` varchar(12) DEFAULT NULL,
  `name` varchar(12) DEFAULT NULL,
  `dept` varchar(12) DEFAULT NULL,
  `gender` varchar(2) DEFAULT NULL,
  `birthday` varchar(12) DEFAULT NULL,
  PRIMARY KEY (`sId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `studentinfo` */

insert  into `studentinfo`(`sId`,`major`,`name`,`dept`,`gender`,`birthday`) values ('1001','clinical','Mike','medicine','1','2000-02-01'),('1002','math','Jack','CS','2','2000-03-01'),('1003','English','Lili','MA','2','2000-02-06'),('1004','chemistry','Keson','CS','1','2001-05-01'),('1005','physics','Alex','IS','2','2002-06-01');

/*Table structure for table `stupwd` */

DROP TABLE IF EXISTS `stupwd`;

CREATE TABLE `stupwd` (
  `id` varchar(12) DEFAULT NULL,
  `pwd` varchar(12) DEFAULT NULL,
  `name` varchar(12) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `stupwd` */

insert  into `stupwd`(`id`,`pwd`,`name`) values ('1001','1234','Mike'),('1002','1234','Jack'),('1003','1234','Lili'),('1004','1234','Keson'),('1005','1234','Alex');

/*Table structure for table `teach` */

DROP TABLE IF EXISTS `teach`;

CREATE TABLE `teach` (
  `cId` varchar(12) NOT NULL DEFAULT '',
  `tId` varchar(12) NOT NULL DEFAULT '',
  PRIMARY KEY (`tId`,`cId`),
  KEY `cId` (`cId`),
  CONSTRAINT `teach_ibfk_1` FOREIGN KEY (`tId`) REFERENCES `teacherinfo` (`tId`),
  CONSTRAINT `teach_ibfk_2` FOREIGN KEY (`cId`) REFERENCES `courseinfo` (`cId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `teach` */

insert  into `teach`(`cId`,`tId`) values ('1','3'),('2','4'),('3','5'),('4','1'),('5','2');

/*Table structure for table `teacherinfo` */

DROP TABLE IF EXISTS `teacherinfo`;

CREATE TABLE `teacherinfo` (
  `tId` varchar(12) NOT NULL,
  `tName` varchar(12) DEFAULT NULL,
  `university` varchar(12) DEFAULT NULL,
  `tTitle` varchar(12) DEFAULT NULL,
  `eduBg` varchar(12) DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `gender` varchar(2) DEFAULT NULL,
  PRIMARY KEY (`tId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `teacherinfo` */

insert  into `teacherinfo`(`tId`,`tName`,`university`,`tTitle`,`eduBg`,`birthday`,`gender`) values ('1','A','anda','teacher','benke','1990-01-01','1'),('2','B','anlida','teacher','benke','1991-01-01','1'),('3','C','keda','teacher','benke','1993-07-01','2'),('4','D','zheda','teacher','benke','1995-08-09','2'),('5','E','nanda','teacher','benke','1996-08-09','2');

/*Table structure for table `teacherpwd` */

DROP TABLE IF EXISTS `teacherpwd`;

CREATE TABLE `teacherpwd` (
  `id` varchar(12) DEFAULT NULL,
  `pwd` varchar(12) DEFAULT NULL,
  `name` varchar(12) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `teacherpwd` */

insert  into `teacherpwd`(`id`,`pwd`,`name`) values ('1','1234','A'),('2','1234','B'),('3','1234','C'),('4','1234','D'),('5','1234','E');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
