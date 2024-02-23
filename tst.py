import usb
id_device = 0x00DE
id_vendor = 0x04D8
product_id = 0x00DE
vendor_id = 0x04D8
dev = usb.core.find(idProduct=id_device)
# print(dev)
serialNumber = usb.util.get_string( dev, dev.iSerialNumber )
print('found serial number \'{0}\' of device \'{1}\'' .format(serialNumber,usb.util.get_string( dev, dev.iProduct )))
# quit()
# serialNumber = '0001007645'
# serial_number = '0001007645'
import time,random
# from mcp2210 import Mcp2210, Mcp2210GpioDesignation, Mcp2210GpioDirection



from mymcp2210 import myMcp2210

mcp = myMcp2210(serial_number=serialNumber)

print(mcp.get_config_spi_timing())
mcp.configure_spi_timing(chip_select_to_data_delay=random.randrange(10),
                         last_data_byte_to_cs=random.randrange(10),
                         delay_between_bytes=random.randrange(10),
                         bit_rate=random.randrange(1500)+1500
                         )
print(mcp.get_config_spi_timing())

mcp.configure_spi_timing(chip_select_to_data_delay=0,
                         last_data_byte_to_cs=0,
                         delay_between_bytes=0,
                         bit_rate=1500
                         )

print(mcp.get_config_spi_timing())
quit()

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
mcp.spi_exchange(bytes([0,0,0x44,0xff,0,0,0,0]), cs_pin_number=pin)
mcp.spi_exchange(bytes([0,0,0,0]), cs_pin_number=pin)

# quit()

while True : 
    time.sleep(0.25)
    resp=mcp.spi_exchange(bytes([0,0]), cs_pin_number=pin)
    resp = int.from_bytes(resp,'big')*2**(13-2*8)*0.0625
    print(resp)

# id_device = 0x00DE
# id_vendor = 0x04D8
# from mcp2210 import MCP2210
# dev = MCP2210(id_vendor, id_device)
