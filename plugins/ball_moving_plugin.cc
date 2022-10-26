#include <gazebo/gazebo.hh>
#include <ignition/math/Vector3.hh>

namespace gazebo
{
  class Ball_moving_plugin : public ModelPlugin
  {

    // Pointer to the model
    private: physics::ModelPtr model;
    // Pointer to the update event connection
    private: event::ConnectionPtr updateConnection;

    public: void Load(physics::ModelPtr _model, sdf::ElementPtr _sdf)
    {
        this->model = _model;

        // Listen to the update event. This event is broadcast every
        // simulation iteration.
        this->updateConnection = event::Events::ConnectWorldUpdateBegin(
                                 std::bind(&Ball_moving_plugin::OnUpdate, this));
    }

    // Called by the world update start event
    public: void OnUpdate()
    {
      this->model->SetLinearVel(ignition::math::Vector3d(.3, 0, 0));
    }

  };

  // Register this plugin with the simulator
  GZ_REGISTER_MODEL_PLUGIN(Ball_moving_plugin)
}