/*
 Navicat Premium Data Transfer

 Source Server         : 120.79.200.146
 Source Server Type    : MySQL
 Source Server Version : 80029
 Source Host           : 120.79.200.146:3306
 Source Schema         : onlineHotel

 Target Server Type    : MySQL
 Target Server Version : 80029
 File Encoding         : 65001

 Date: 09/07/2022 10:11:40
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for hotel
-- ----------------------------
DROP TABLE IF EXISTS `hotel`;
CREATE TABLE `hotel`  (
  `AutoID` bigint(0) NOT NULL AUTO_INCREMENT COMMENT '自增主键',
  `HotelID` bigint(0) NULL DEFAULT NULL COMMENT '酒店id',
  `HotelName` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '酒店名称',
  `HotelAccount` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '酒店账号昵称',
  `Password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '酒店登录密码',
  `Phone` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '酒店联系电话',
  `Email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '酒店邮箱',
  `Province` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '酒店所在省',
  `City` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '酒店所在市',
  `Area` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '酒店所在区',
  `Address` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '酒店所在地址',
  `HotelPicUrl` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '酒店图片地址',
  `HotelLabels` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '酒店标签，用\'/‘隔开',
  `HotelDist` float NULL DEFAULT 100 COMMENT '酒店离市中心距离',
  `IsDeleted` tinyint(0) NULL DEFAULT 0 COMMENT '0--未删除，1--删除',
  `CreateTime` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '创建时间',
  PRIMARY KEY (`AutoID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 21 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '该表主要用于保存宾馆信息' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for order_form
-- ----------------------------
DROP TABLE IF EXISTS `order_form`;
CREATE TABLE `order_form`  (
  `AutoID` bigint(0) NOT NULL AUTO_INCREMENT COMMENT '自增的主键',
  `OrderFormID` bigint(0) NULL DEFAULT NULL COMMENT '订单id',
  `UserID` bigint(0) NULL DEFAULT NULL COMMENT '订单用户id',
  `GuestID` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '住客身份证',
  `GuestName` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '住客姓名',
  `GuestPhone` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '住客电话',
  `HotelID` bigint(0) NULL DEFAULT NULL COMMENT '订单所属宾馆id',
  `RoomID` bigint(0) NULL DEFAULT NULL COMMENT '房间信息',
  `ArrivalTime` datetime(0) NULL DEFAULT NULL COMMENT '到店时间',
  `CheckOutTime` datetime(0) NULL DEFAULT NULL COMMENT '离店时间',
  `OrderFormStatus` tinyint(0) NULL DEFAULT 0 COMMENT '0--未入住  1--入住  2--订单完成',
  `IsDeleted` tinyint(0) NULL DEFAULT 0 COMMENT '0--未删除，1--删除',
  `CreateTime` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '创建时间',
  PRIMARY KEY (`AutoID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 14 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '该表主要用户保存订单信息' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for remark
-- ----------------------------
DROP TABLE IF EXISTS `remark`;
CREATE TABLE `remark`  (
  `AutoID` bigint(0) NOT NULL AUTO_INCREMENT COMMENT '自增的主键',
  `RemarkID` bigint(0) NULL DEFAULT NULL COMMENT '评论id',
  `RemarkContent` varchar(600) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '评论内容',
  `HotelID` bigint(0) NULL DEFAULT NULL COMMENT '评论酒店id',
  `RemarkUserID` bigint(0) NULL DEFAULT NULL COMMENT '评论用户id',
  `IsDeleted` tinyint(0) NULL DEFAULT 0 COMMENT '0--未删除，1--删除',
  `CreateTime` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '创建时间',
  PRIMARY KEY (`AutoID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '该表主要用于保存用户评论信息' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for room
-- ----------------------------
DROP TABLE IF EXISTS `room`;
CREATE TABLE `room`  (
  `AutoID` bigint(0) NOT NULL AUTO_INCREMENT COMMENT '自增的主键',
  `RoomID` bigint(0) NULL DEFAULT NULL COMMENT '房间id',
  `HotelID` bigint(0) NULL DEFAULT NULL COMMENT '酒店id',
  `RoomNum` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '房间号',
  `RoomTypeID` bigint(0) NULL DEFAULT NULL COMMENT '房间种类id',
  `RoomStatus` tinyint(0) NULL DEFAULT 0 COMMENT '0---空闲，1---占用',
  `IsDeleted` tinyint(0) NULL DEFAULT 0 COMMENT '0--未删除，1--删除',
  `CreateTime` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '创建时间',
  PRIMARY KEY (`AutoID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '主要用于保存宾馆房间信息' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for room_type
-- ----------------------------
DROP TABLE IF EXISTS `room_type`;
CREATE TABLE `room_type`  (
  `AutoID` bigint(0) NOT NULL AUTO_INCREMENT COMMENT '自增的主键',
  `RoomTypeID` bigint(0) NULL DEFAULT NULL COMMENT '房间种类id',
  `HotelID` bigint(0) NULL DEFAULT NULL COMMENT '所属酒店id',
  `RoomTypeName` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '类型名称',
  `Square` float(10, 1) NULL DEFAULT NULL COMMENT '房间大小',
  `Floor` int(0) NULL DEFAULT NULL COMMENT '房间楼层',
  `WindowDescription` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '房间窗户描述',
  `Price` float(10, 2) NULL DEFAULT NULL COMMENT '房间定价',
  `RoomTypeBrief` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '房间类型简介',
  `RoomPicUrl` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '房间类型图片地址',
  `IsDeleted` tinyint(0) NULL DEFAULT 0 COMMENT '0--未删除，1--删除',
  `CreateTime` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '创建时间',
  PRIMARY KEY (`AutoID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '主要用于保存宾馆房间种类' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `AutoID` bigint(0) NOT NULL AUTO_INCREMENT COMMENT '自增的主键',
  `UserID` bigint(0) NULL DEFAULT NULL COMMENT '用户id',
  `UserName` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '用户名称',
  `Password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '用户密码',
  `Phone` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '用户电话',
  `Email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '邮箱',
  `IsInRoom` tinyint(0) NULL DEFAULT 0 COMMENT '0--未入住，1--入住',
  `FaceUrl` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '用户头像地址',
  `IsDeleted` tinyint(0) NULL DEFAULT 0 COMMENT '0--未删除，1--删除',
  `CreateTime` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '创建时间',
  PRIMARY KEY (`AutoID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '主要用于保存住客信息' ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
