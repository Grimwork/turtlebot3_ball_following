#include <gazebo/common/Plugin.hh>
#include <gazebo/common/common.hh>
#include <gazebo/physics/physics.hh>
#include <ignition/math/Vector3.hh>
#include <string.h>

namespace gazebo
{
  class Ball_moving_plugin : public ModelPlugin
  {

    private :
    std::string key;
    float velocity;

    // Pointer to the model
    private: physics::ModelPtr model;
    // Pointer to the update event connection
    private: event::ConnectionPtr updateConnection;

    public: void Load(physics::ModelPtr _model, sdf::ElementPtr _sdf)
    {
        this->model = _model;

        // Print Model name on console when world is loaded (yellow ball here)
        std::cout << "Model Name = " << this->model->GetName() << std::endl; 

        // Listen to the update event. This event is broadcast every
        // simulation iteration.
        this->updateConnection = event::Events::ConnectWorldUpdateBegin(
                                 std::bind(&Ball_moving_plugin::OnUpdate, this));
    }

    // Called by the world update start event
    public: void OnUpdate()
    {
      //apply a small velocity on ball on axis x

    }

  };

  // Register this plugin with the simulator
  GZ_REGISTER_MODEL_PLUGIN(Ball_moving_plugin)
}