/**
* Filename     :   car_loader.cpp
* Description  :   
* Time         :   2022/04/16 12:49:53
* Author       :   Bao Mingxi
* Version      :   1.0
* @Contact     :   baomx1314@163.com
**/

#include "car_Model/car_loader.h"
    
int main(int argc,char** argv){
    ros::init(argc,argv,"ca_model_node");
    ros::NodeHandle nh;
    ros::Rate r(10);
    std::string car_model_path="package://car_Model/meshes/am7f3psa0agw-Car-Model/CarModel/Car.dae";
    ros::Publisher car_pub=nh.advertise<visualization_msgs::Marker>("car_model_bao",1);
    
    while(ros::ok()){
        CAR_MODEL::car_model(car_pub,car_model_path);
        // car_model(car_pub);
        ros::spinOnce();
        r.sleep();
    }
    return 0;
}