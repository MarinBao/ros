/**
* Filename     :   car_loader.h
* Description  :   
* Time         :   2022/04/16 12:50:27
* Author       :   Bao Mingxi
* Version      :   1.0
* @Contact     :   baomx1314@163.com
**/

#pragma once
#include <ros/ros.h>
#include <visualization_msgs/MarkerArray.h>
#include <visualization_msgs/Marker.h>
#include <tf/tf.h>
#include <geometry_msgs/Quaternion.h>


/**
* @brief  rviz中加载车模型
* @param  
* @returns  
* @note  
**/

namespace CAR_MODEL{
    void car_model(ros::Publisher &car_pub,std::string &car_path)
    {
        visualization_msgs::Marker marker;
        marker.header.frame_id="map";
        marker.header.stamp=ros::Time::now();   //  使用和use_sim_time
        marker.id=-100;
        marker.ns="CAR_MODEL";
        marker.type=visualization_msgs::Marker::MESH_RESOURCE;
        marker.action=visualization_msgs::Marker::ADD;
        marker.mesh_resource=car_path;
    
        geometry_msgs::Quaternion q=tf::createQuaternionMsgFromRollPitchYaw(0,0,3.1415926/2);
        marker.pose.orientation.x=q.x;
        marker.pose.orientation.y=q.y;
        marker.pose.orientation.z=q.z;
        marker.pose.orientation.w=q.w;   

        marker.pose.position.x=0;
        marker.pose.position.y=0;
        marker.pose.position.z=-1.73;

        marker.scale.x=1.0;
        marker.scale.y=1.0;
        marker.scale.z=1.0;


        marker.color.r=0.2;
        marker.color.g=0.8;
        marker.color.b=0.8;
        marker.color.a=1.0;

        car_pub.publish(marker);
    }




}