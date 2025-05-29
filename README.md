# UAV Obstacle Avoidance Demo

Simulated obstacle avoidance logic for drones using DroneKit and ArduPilot. Intended for Raspberry Pi + Pixhawk integration.

## 🚧 What It Does
- Detects simulated obstacles (ultrasonic or stereo vision input)
- Alters flight path to avoid obstacle
- Resumes original waypoint mission after avoidance

## 📡 Use Case
Critical for navigating tight urban or post-disaster environments where static or dynamic obstacles may appear mid-mission.

## 📁 Structure
- `scripts/`: Contains the main reroute logic
- `notebooks/`: Visual simulation of path correction
- `assets/`: Rerouting diagrams and examples

## 🔧 Requirements
- DroneKit
- ArduPilot
- Raspberry Pi + Pixhawk

## 🔮 Future Work
- Real-time depth camera integration
- Obstacle logging for SLAM mapping
