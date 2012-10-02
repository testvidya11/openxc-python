import argparse

def device_options():
    parser = argparse.ArgumentParser(add_help=False)
    device_group = parser.add_mutually_exclusive_group()
    device_group.add_argument("--usb", action="store_true", dest="use_usb", default=True)
    device_group.add_argument("--serial", action="store_true", dest="use_serial", default=False)
    parser.add_argument("--usb-vendor",
            action="store",
            dest="usb_vendor")
    parser.add_argument("--serial-port",
            action="store",
            dest="serial_port",
            help="If using a serial-based CAN translator, use a custom port")
    parser.add_argument("--serial-baudrate",
            action="store",
            dest="baudrate",
            help="If using a serial-based CAN translator, use a custom baudrate")
    return parser
