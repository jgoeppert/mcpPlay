import usb
id_device = 0x00DE
id_vendor = 0x04D8
product_id = 0x00DE
vendor_id = 0x04D8
dev = usb.core.find(idProduct=id_device)
serialNumber = usb.util.get_string( dev, dev.iSerialNumber )
print('found device serial number: {}' .format(serialNumber))
# quit()
# serialNumber = '0001007645'
# serial_number = '0001007645'
import time
from mcp2210 import Mcp2210, Mcp2210GpioDesignation, Mcp2210GpioDirection


class myMcp2210(Mcp2210):
    def configure_spi_timing(self
        , chip_select_to_data_delay: int = None
        , last_data_byte_to_cs: int = None
        , delay_between_bytes: int = None
        , bit_rate: int = None
    ):
        if chip_select_to_data_delay is not None:
            self._spi_settings.chip_select_to_data_delay = chip_select_to_data_delay
        if last_data_byte_to_cs is not None:
            self._spi_settings.last_data_byte_to_cs_delay = last_data_byte_to_cs
        if delay_between_bytes is not None:
            self._spi_settings.delay_between_bytes = delay_between_bytes
        if bit_rate is not None:
            self._spi_settings.bit_rate = bit_rate
        self._set_spi_configuration()

# import myMcp2210

mcp = myMcp2210(serial_number=serialNumber)
mcp.configure_spi_timing(chip_select_to_data_delay=0,
                         last_data_byte_to_cs=0,
                         delay_between_bytes=0,
                         bit_rate=1500
                         )

for pin in range(9) : mcp.set_gpio_designation(pin, Mcp2210GpioDesignation.GPIO)

pin = 7
mcp.set_gpio_designation(pin, Mcp2210GpioDesignation.CHIP_SELECT)
tx_data = bytes(range(2))
# tx_data = bytes(6,0xff,0xff)
# rList = [6, 0xff, 0xff]
# tx_data = bytes(rList)
# mcp.spi_exchange(tx_data, cs_pin_number=pin)


# tx_data = bytes([0xff,0xff,0xff,0xff])
# tx_data = bytes([0xff,0xff,0,0])
# # tx_data = bytes([0xff,0xff])
# # tx_data = bytes([0,0])
# # mcp.spi_exchange(tx_data, cs_pin_number=pin)

# mcp.spi_exchange(bytes([0,0,0x44,0xff,0,0,0,0])
# mcp.spi_exchange(bytes([0,0,0x44,0xff,0,0,0,0]), cs_pin_number=pin)

# quit()

while True : 
    time.sleep(0.25)
    resp=mcp.spi_exchange(bytes([0,0]), cs_pin_number=pin)
    resp = int.from_bytes(resp)*2**(13-2*8)*0.0625
    print(resp)

# id_device = 0x00DE
# id_vendor = 0x04D8
# from mcp2210 import MCP2210
# dev = MCP2210(id_vendor, id_device)
