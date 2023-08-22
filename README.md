# Ros_6072_basic
Miniproject for Fra502
## Prerequistes
- Ubuntu 18.04
- Ros Melodic 
- Gazebo 9
### Run gazebo and teleop keyboard
Use gazebo and keyboard for simulation
```sh
roslaunch robotblack_gazebo robotblack_gazebo.launch 
```
Use the keyboard only and Close Terminal with b button ,Condition of keyboard W='Go' A='left' S='Stop' D='right' X='back' R='Speed up' F='reduce speed'
```sh
roslaunch robotblack_gazebo teleop_Rb.launch 
```
### Navigation and create map
To create map by slam gmapping
```sh
roslaunch robotblack_slam slam_gmapping.launch 
```
Save map with map saver
```sh
rosrun map_server map_saver -f mymap
```
Navigation robot
```sh
roslaunch robotblack_navigation robotblack_navigation.launch
```
[![Example project ros]
https://www.youtube.com/watch?v=p-w7WgIr49I
