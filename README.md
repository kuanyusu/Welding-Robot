# Welding-Robot

## Introduction
Haptic interfaces as assistive technology gained prominence in recent years, which can be used in diverse applications like training, skills assessment, virtual assembly, rehabilitation and remote operation. In this project we successfully demonstrate how to tele-operate a robot model ABB-IRB52 in V-REP simulator to do welding jobs with a TOUCH haptic device. To achieve this purpose, a client program in C language had been developed to exchange data between V-REP and TOUCH. In addition, a remote API command server in LUA language was built in V-REP side.

## TOUCH Haptic Device
Touch is a motorized device that applies force feedback on the user’s hand, allowing them to feel virtual objects and producing true-to-life touch sensations as user manipulates on-screen 3D objects. Leading companies integrate the Touch and haptics into their work to achieve compelling solutions using the realistic sense of touch.

![image](https://github.com/kuanyusu/Welding-Robot/blob/master/fig.1.jpg)
Fig. 1 Technical specifications for TOUCH.

## ABB-IRB52 Robot
With integrated development environment, V-REP is based on a distributed control architecture: each object/model can be individually controlled via an embedded script, a plugin, a ROS node, a remote API client, or a custom solution. This makes V-REP very versatile and ideal for multi-robot applications. Controllers can be written in C/C++, Python, Java, Lua, Matlab, Octave or Urbi.

![image](https://github.com/kuanyusu/Welding-Robot/blob/master/fig.2.jpg)
Fig. 2 The structure of a ABB-IRB52 robot.

## Appendix - Testing Videos
(1)Function Testing: https://reurl.cc/723AYd
