This sample code use the skeleton from MCP2210 linux library. 
The user could specify the data sequence to sent to the slave and the clock speed.

You will need the following packages/tools:
- GCC compiler
- binutils

Steps:
Open a terminal window. Type "make" to start the building process.

Before running the sample code, we need to identify the driver
entries for the connected MCP2210 chips.
Run the provided script ("runme.sh"). Please type:
"./runme.sh"(or bash runme.sh)

Its output should show something like this when at least one MCP2210 chip is
detected:

I found the requested VID/PID:  04d8, 00de
MCP2210 can be found at "/dev/hidraw1"

After that, sample code could be run(admin rights are needed) using the following command:
"sudo ./sample_code_demo [hid_raw_index] [data_to_sent] [speed]"
Where:

hid_raw_index - The path to the MCP2210
data_to_sent - Data to send to the slave(in decimal). Every byte must be comma separated.
speed - SPI clock-rate(in decimal)

example: sudo ./sample_code_demo /dev/hidraw0 1,2,3,4 1000000 

This sample code use GP0 as active CS and there are no delays(cs-to-data, data-to-data and data-to-cs).

