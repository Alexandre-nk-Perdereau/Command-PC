import wakeonlan
import sys

def wake_up_pc(mac_address):
    try:
        wakeonlan.send_magic_packet(mac_address)
        print(f"Magic packet sent to {mac_address}")
        return True
    except Exception as e:
        print(f"Error sending magic packet: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python wake_pc.py <mac_address>")
        sys.exit(1)

    mac_address = sys.argv[1]

    if wake_up_pc(mac_address):
        print("PC should be waking up")
    else:
        print("Failed to wake up PC")