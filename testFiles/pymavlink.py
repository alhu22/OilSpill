"""testing pymavlink connection and telemetry display from pixhawk"""


from pymavlink import mavutil

master = mavutil.mavlink_connection('COM5', baud=115200)
print("Waiting for heartbeat...")
master.wait_heartbeat()
print(f"✅ Connected! System: {master.target_system}, Component: {master.target_component}")

print("\n📡 Live telemetry (Ctrl+C to stop):\n")

while True:
    msg = master.recv_match(blocking=True, timeout=2)
    if msg is None:
        continue

    msg_type = msg.get_type()

    if msg_type == 'ATTITUDE':
        print(f"🧭 Roll: {msg.roll:.2f}  Pitch: {msg.pitch:.2f}  Yaw: {msg.yaw:.2f}")

    elif msg_type == 'GLOBAL_POSITION_INT':
        lat = msg.lat / 1e7
        lon = msg.lon / 1e7
        alt = msg.relative_alt / 1000
        print(f"📍 Lat: {lat:.6f}  Lon: {lon:.6f}  Alt: {alt:.2f}m")

    elif msg_type == 'SYS_STATUS':
        voltage = msg.voltage_battery / 1000
        print(f"🔋 Battery: {voltage:.2f}V")

    elif msg_type == 'HEARTBEAT':
        modes = {
            0: 'STABILIZE', 2: 'ALT_HOLD', 3: 'AUTO',
            4: 'GUIDED', 5: 'LOITER', 6: 'RTL', 9: 'LAND'
        }
        mode = modes.get(msg.custom_mode, f'MODE({msg.custom_mode})')
        armed = "🔴 ARMED" if msg.base_mode & 0x80 else "⚪ DISARMED"
        print(f"💚 Mode: {mode}  Status: {armed}")