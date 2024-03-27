import requests

def turn_on_plug(shelly_ip):
    url = f"http://{shelly_ip}/rpc/Switch.Set?id=0&on=true"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises a HTTPError if the status is 4xx, 5xx
    except requests.exceptions.RequestException as e:
        print(f"Error turning on the plug: {e}")
        return False
    
    return True

def turn_off_plug(shelly_ip, force=False, power_threshold=30):
    url_status = f"http://{shelly_ip}/rpc/Switch.GetStatus?id=0"
    url_off = f"http://{shelly_ip}/rpc/Switch.Set?id=0&on=false"

    if not force:
        try:
            response = requests.get(url_status)
            response.raise_for_status()
            status = response.json()
            if 'apower' in status:
                power = status['apower']
                if power > power_threshold:
                    print(f"Current power consumption is {power}W, which is above the threshold of {power_threshold}W.")
                    return False
            else:
                print("Error: 'apower' not found in status response")
                return False
        except requests.exceptions.RequestException as e:
            print(f"Error checking power status: {e}")
            return False

    try:
        response = requests.get(url_off)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error turning off the plug: {e}")
        return False

    return True