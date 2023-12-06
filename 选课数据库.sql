/*
 Navicat Premium Data Transfer

 Source Server         : MySQL
 Source Server Type    : MySQL
 Source Server Version : 80035
 Source Host           : localhost:3306
 Source Schema         : system_choose_course

 Target Server Type    : MySQL
 Target Server Version : 80035
 File Encoding         : 65001

 Date: 05/12/2023 19:15:36
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for adminpwd
-- ----------------------------
DROP TABLE IF EXISTS `adminpwd`;
CREATE TABLE `adminpwd`  (
  `id` varchar(12) CHARACTER SET latin1 COLLATE latin1_swedish_ci DEFAULT NULL,
  `pwd` varchar(12) CHARACTER SET latin1 COLLATE latin1_swedish_ci DEFAULT NULL,
  `name` varchar(12) CHARACTER SET latin1 COLLATE latin1_swedish_ci DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of adminpwd
-- ----------------------------
INSERT INTO `adminpwd` VALUES ('1', '1234', 'AA');
INSERT INTO `adminpwd` VALUES ('2', '1234', 'AB');
INSERT INTO `adminpwd` VALUES ('3', '1234', 'AC');
INSERT INTO `adminpwd` VALUES ('4', '1234', 'AD');

-- ----------------------------
-- Table structure for classroom
-- ----------------------------
DROP TABLE IF EXISTS `classroom`;
CREATE TABLE `classroom`  (
  `crId` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `crNum` int(0) DEFAULT NULL,
  PRIMARY KEY (`crId`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of classroom
-- ----------------------------
INSERT INTO `classroom` VALUES ('1', 50);
INSERT INTO `classroom` VALUES ('100', 100);
INSERT INTO `classroom` VALUES ('2', 100);
INSERT INTO `classroom` VALUES ('3', 100);
INSERT INTO `classroom` VALUES ('4', 50);
INSERT INTO `classroom` VALUES ('5', 50);

-- ----------------------------
-- Table structure for classroom_arr
-- ----------------------------
DROP TABLE IF EXISTS `classroom_arr`;
CREATE TABLE `classroom_arr`  (
  `crId` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL DEFAULT '',
  `cId` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL DEFAULT '',
  `cTime` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  PRIMARY KEY (`crId`, `cId`) USING BTREE,
  INDEX `cId`(`cId`) USING BTREE,
  CONSTRAINT `classroom_arr_ibfk_1` FOREIGN KEY (`crId`) REFERENCES `classroom` (`crId`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `classroom_arr_ibfk_2` FOREIGN KEY (`cId`) REFERENCES `courseinfo` (`cId`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of classroom_arr
-- ----------------------------
INSERT INTO `classroom_arr` VALUES ('1', '3', '周一1-2，周三7-8');
INSERT INTO `classroom_arr` VALUES ('100', '100', '周三1-2，周五3-4');
INSERT INTO `classroom_arr` VALUES ('2', '5', '周一3-4，周三5-6');
INSERT INTO `classroom_arr` VALUES ('3', '4', '周二1-2，周四7-8');
INSERT INTO `classroom_arr` VALUES ('4', '1', '周一7-8，周三3-4');
INSERT INTO `classroom_arr` VALUES ('5', '2', '周三1-2，周五3-4');

-- ----------------------------
-- Table structure for courseinfo
-- ----------------------------
DROP TABLE IF EXISTS `courseinfo`;
CREATE TABLE `courseinfo`  (
  `cId` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `cName` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `cIntro` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `cHour` float DEFAULT NULL,
  `cCredit` float DEFAULT NULL,
  `cWeek` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  PRIMARY KEY (`cId`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of courseinfo
-- ----------------------------
INSERT INTO `courseinfo` VALUES ('1', 'C', 'slightly', 20, 2, '1-6');
INSERT INTO `courseinfo` VALUES ('100', 'test', 'slightly', 30, 3, '1-7');
INSERT INTO `courseinfo` VALUES ('2', 'java', 'slightly', 25, 3, '1-8');
INSERT INTO `courseinfo` VALUES ('3', 'database', 'slightly', 20, 1, '1-10');
INSERT INTO `courseinfo` VALUES ('4', 'algorithm', 'slightly', 10, 2.5, '6-12');
INSERT INTO `courseinfo` VALUES ('5', 'python', 'slightly', 30, 2, '6-14');

-- ----------------------------
-- Table structure for sc
-- ----------------------------
DROP TABLE IF EXISTS `sc`;
CREATE TABLE `sc`  (
  `sId` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL DEFAULT '',
  `cId` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL DEFAULT '',
  `grade` float DEFAULT NULL,
  PRIMARY KEY (`sId`, `cId`) USING BTREE,
  INDEX `cId`(`cId`) USING BTREE,
  CONSTRAINT `sc_ibfk_1` FOREIGN KEY (`sId`) REFERENCES `studentinfo` (`sId`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `sc_ibfk_2` FOREIGN KEY (`cId`) REFERENCES `courseinfo` (`cId`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sc
-- ----------------------------
INSERT INTO `sc` VALUES ('1001', '1', 0);
INSERT INTO `sc` VALUES ('1001', '100', 0);
INSERT INTO `sc` VALUES ('1001', '2', 0);
INSERT INTO `sc` VALUES ('1001', '3', 0);
INSERT INTO `sc` VALUES ('1001', '4', 0);
INSERT INTO `sc` VALUES ('1001', '5', 0);
INSERT INTO `sc` VALUES ('1002', '1', 0);
INSERT INTO `sc` VALUES ('1002', '2', 0);
INSERT INTO `sc` VALUES ('1002', '3', 0);
INSERT INTO `sc` VALUES ('1002', '4', 0);
INSERT INTO `sc` VALUES ('1002', '5', 0);
INSERT INTO `sc` VALUES ('1003', '3', 0);

-- ----------------------------
-- Table structure for studentinfo
-- ----------------------------
DROP TABLE IF EXISTS `studentinfo`;
CREATE TABLE `studentinfo`  (
  `sId` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `major` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `name` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `dept` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `gender` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `birthday` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  PRIMARY KEY (`sId`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of studentinfo
-- ----------------------------
INSERT INTO `studentinfo` VALUES ('1001', 'clinical', 'Mike', 'medicine', '1', '2000-02-01');
INSERT INTO `studentinfo` VALUES ('1002', 'math', 'Jack', 'CS', '2', '2000-03-01');
INSERT INTO `studentinfo` VALUES ('1003', 'English', 'Lili', 'MA', '2', '2000-02-06');
INSERT INTO `studentinfo` VALUES ('1004', 'chemistry', 'Keson', 'CS', '1', '2001-05-01');
INSERT INTO `studentinfo` VALUES ('1005', 'physics', 'Alex', 'IS', '2', '2002-06-01');

-- ----------------------------
-- Table structure for stupwd
-- ----------------------------
DROP TABLE IF EXISTS `stupwd`;
CREATE TABLE `stupwd`  (
  `id` varchar(12) CHARACTER SET latin1 COLLATE latin1_swedish_ci DEFAULT NULL,
  `pwd` varchar(12) CHARACTER SET latin1 COLLATE latin1_swedish_ci DEFAULT NULL,
  `name` varchar(12) CHARACTER SET latin1 COLLATE latin1_swedish_ci DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of stupwd
-- ----------------------------
INSERT INTO `stupwd` VALUES ('1001', '1234', 'Mike');
INSERT INTO `stupwd` VALUES ('1002', '1234', 'Jack');
INSERT INTO `stupwd` VALUES ('1003', '1234', 'Lili');
INSERT INTO `stupwd` VALUES ('1004', '1234', 'Keson');
INSERT INTO `stupwd` VALUES ('1005', '1234', 'Alex');

-- ----------------------------
-- Table structure for teach
-- ----------------------------
DROP TABLE IF EXISTS `teach`;
CREATE TABLE `teach`  (
  `cId` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL DEFAULT '',
  `tId` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL DEFAULT '',
  PRIMARY KEY (`tId`, `cId`) USING BTREE,
  INDEX `cId`(`cId`) USING BTREE,
  CONSTRAINT `teach_ibfk_1` FOREIGN KEY (`tId`) REFERENCES `teacherinfo` (`tId`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `teach_ibfk_2` FOREIGN KEY (`cId`) REFERENCES `courseinfo` (`cId`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of teach
-- ----------------------------
INSERT INTO `teach` VALUES ('1', '3');
INSERT INTO `teach` VALUES ('100', '100');
INSERT INTO `teach` VALUES ('2', '4');
INSERT INTO `teach` VALUES ('3', '5');
INSERT INTO `teach` VALUES ('4', '1');
INSERT INTO `teach` VALUES ('5', '2');

-- ----------------------------
-- Table structure for teacherinfo
-- ----------------------------
DROP TABLE IF EXISTS `teacherinfo`;
CREATE TABLE `teacherinfo`  (
  `tId` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `tName` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `university` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `tTitle` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `eduBg` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `birthday` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `gender` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  PRIMARY KEY (`tId`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of teacherinfo
-- ----------------------------
INSERT INTO `teacherinfo` VALUES ('1', 'A', 'anda', 'teacher', 'benke', '2000-01-01', '1');
INSERT INTO `teacherinfo` VALUES ('100', 'test teacher', 'none', 'none', 'none', '2000-01-01', '1');
INSERT INTO `teacherinfo` VALUES ('2', 'B', 'anlida', 'teacher', 'benke', '2000-01-01', '1');
INSERT INTO `teacherinfo` VALUES ('3', 'C', 'keda', 'teacher', 'benke', '2000-01-01', '2');
INSERT INTO `teacherinfo` VALUES ('4', 'D', 'zheda', 'teacher', 'benke', '2000-01-01', '2');
INSERT INTO `teacherinfo` VALUES ('5', 'E', 'nanda', 'teacher', 'benke', '2000-01-01', '2');

-- ----------------------------
-- Table structure for teacherpwd
-- ----------------------------
DROP TABLE IF EXISTS `teacherpwd`;
CREATE TABLE `teacherpwd`  (
  `id` varchar(12) CHARACTER SET latin1 COLLATE latin1_swedish_ci DEFAULT NULL,
  `pwd` varchar(12) CHARACTER SET latin1 COLLATE latin1_swedish_ci DEFAULT NULL,
  `name` varchar(12) CHARACTER SET latin1 COLLATE latin1_swedish_ci DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of teacherpwd
-- ----------------------------
INSERT INTO `teacherpwd` VALUES ('1', '1234', 'A');
INSERT INTO `teacherpwd` VALUES ('2', '1234', 'B');
INSERT INTO `teacherpwd` VALUES ('3', '1234', 'C');
INSERT INTO `teacherpwd` VALUES ('4', '1234', 'D');
INSERT INTO `teacherpwd` VALUES ('5', '1234', 'E');
INSERT INTO `teacherpwd` VALUES ('100', '1234', 'test teacher');

SET FOREIGN_KEY_CHECKS = 1;
