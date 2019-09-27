# Welding-Robot

## Introduction
Haptic interfaces as assistive technology gained prominence in recent years, which can be used in diverse applications like training, skills assessment, virtual assembly, rehabilitation and remote operation. In this project we successfully demonstrate how to tele-operate a robot model ABB-IRB52 in V-REP simulator to do welding jobs with a TOUCH haptic device. To achieve this purpose, a client program in C language had been developed to exchange data between V-REP and TOUCH. In addition, a remote API command server in LUA language was built in V-REP side.

## TOUCH Haptic Device
Touch is a motorized device that applies force feedback on the user’s hand, allowing them to feel virtual objects and producing true-to-life touch sensations as user manipulates on-screen 3D objects. Leading companies integrate the Touch and haptics into their work to achieve compelling solutions using the realistic sense of touch.

![image](https://github.com/kuanyusu/Welding-Robot/blob/master/fig.1.jpg)
Fig. 1 Technical specifications for TOUCH.

## ABB-IRB52 Robot
The body of ABB-IRB52 is composed of the base and other total 6 pieces of mechanical links, for which 5 revolute joints (J0-J4) are needed to inter-connect those links. A welding torch is held by an extra link (in light-gray color) and connected to the terminal link of the robot by an extra revolute joint (J5). A “flexible” power cable that composed of dozens of rigid bodies and revolute joints is installed between the robot body and the welding torch. 

![image](https://github.com/kuanyusu/Welding-Robot/blob/master/fig.2.jpg)
Fig. 2 The structure of a ABB-IRB52 robot.

## Virtual Welding Demonstration
Fig. 3 illustrates the user interfaces being used in our welding experiments. On the bottom we can find two light-gray colored metal plates intended to be welded up on the stitch line in between. On the top-right corner, there is a graph it will continuously monitor and display the proximity sensor readings (in meters). On the left of the graph is a button which is implemented to change the side of the metal plates. Anytime we want to weld up the other side of the plates we just need to press this button. On the bottom-right corner, we place a virtual camera near the welding torch to get a close-up view, as so an operator can clearly check by visual sense in addition to touch sense to grasp how to perform the welding job well.

![image](https://github.com/kuanyusu/Welding-Robot/blob/master/fig.3.jpg)
Fig. 3 The user interfaces on V-REP for the welding experiments. 

## Appendix - Testing Videos
(1)Functional Testing: https://reurl.cc/723AYd
