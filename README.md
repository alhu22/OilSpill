
ip addr show enP8p1s0
Jetson has a static IP of 192.168.144.20/24 on the ethernet port, which matches the 192.168.144.x subnet that HereLink/CubePilot equipment typically uses. So the interface itself is properly configured.

ping 192.168.144.10   workes.


Streaming configuration:
camera → Air Unit (encode + RTSP serve) → Ethernet → Jetson (FFmpeg pulls + decodes) → OpenCV frames.
