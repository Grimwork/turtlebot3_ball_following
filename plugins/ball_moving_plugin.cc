#include <gazebo/gazebo.hh>
#include <gazebo/common/common.hh>
#include <gazebo/physics/physics.hh>
#include <ignition/math/Vector3.hh>
#include <string.h>
#include "ros/ros.h"
#include <geometry_msgs/Twist.h>

namespace gazebo
{

    static geometry_msgs::Twist move_ball_callback(const geometry_msgs::Twist& msg)
    {
      ROS_INFO_STREAM("Subscriber velocities:" << " linear x y z = " << msg.linear.x  << msg.linear.y << msg.linear.z 
                      << " angular x y z = " << msg.angular.x << msg.angular.y << msg.angular.z);
    }

  class Ball_moving_plugin : public ModelPlugin
  {
    // Pointer to the model
    private: physics::ModelPtr model;
    // Pointer to the update event connection
    private: event::ConnectionPtr updateConnection;

    private: std::unique_ptr<ros::NodeHandle> rosNode;

    private: ros::Subscriber rosSub;

    public: void Load(physics::ModelPtr _model, sdf::ElementPtr _sdf)
    {
      this->model = _model;

      // Print Model name on console when world is loaded (yellow ball here)
      std::cout << "Model Name = " << this->model->GetName() << std::endl; 

      // Subscribe to the Ball info topic
      this->rosSub = rosNode.subscribe("ball_moving_info", 1000, move_ball_callback);

      // Listen to the update event. This event is broadcast every
      // simulation iteration.
      this->updateConnection = event::Events::ConnectWorldUpdateBegin(
                                std::bind(&Ball_moving_plugin::OnUpdate, this));
    }

    // Called by the world update start event
    public: void OnUpdate()
    {
      //ros::Subscriber sub = n.subscribe("ball_moving_info", std::string, );
      //apply a small velocity on ball on axis x
      this->model->SetLinearVel(ignition::math::Vector3d(.3, 0, 0));
    }

  };

  // Register this plugin with the simulator
  GZ_REGISTER_MODEL_PLUGIN(Ball_moving_plugin)
}