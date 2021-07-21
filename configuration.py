class Configuration:
    browser_type: str = 'web'   # Can be 'web or 'mobile'
    browser_size: str = None
    base_url: str = 'https://www.eapteka.ru/'
    port: int = None
    timeout: int = 5    # Cannot be None
    headless: bool = False
    mobile_device: str = None
    supported_devices: list = ["Nexus 5", "iPhone 5/SE", "iPhone 6/7/8", "iPhone 6/7/8 Plus", "iPhone X",
                               "Nexus 4", "Nexus 5X", "Nexus 6P", "Nexus 7", "Pixel 2", "Pixel 2 XL", "BlackBerry Z30",
                               "Microsoft Lumia 550", "Microsoft Lumia 950", "Galaxy S III", "Nexus 6", "Galaxy S5",
                               "iPad Mini", "iPad", "iPad Pro", "Blackberry PlayBook", "Nexus 10", "Galaxy Note 3",
                               "Galaxy Note II"]

    remote_driver_url: str = 'http://172.30.96.1:4444/wd/hub'
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "91.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }
