#!/bin/bash

vid=04D8 # very important - write the HEX number with capital letters
pid=00DE # very important - write the HEX number with capital letters

#check to see if sysfs is mounted
sysfs_path=`awk '/^sysfs/{ print $2 }' < /proc/mounts`
curr_path=`pwd`

contains()
{
  string="$1"
  substring="$2"
  if [ "${string#*$substring}" != "$string" ]; then
    echo "found"	# $substring is in $string
  else
    echo ""	# $substring is not in $string
  fi
}

#if variable is empty, we should exit. No SYSFS found
if [[ -z $sysfs_path ]]; then
	echo "No sysfs in this system! Exiting..."
	exit 1
fi

usb_device_path=${sysfs_path}/bus/usb/devices
usb_path=${usb_device_path}

for usbdev in $(ls $usb_device_path); do
	usb_path=${usb_device_path}/${usbdev}
	idvendor=${usb_path}/idVendor
	idproduct=${usb_path}/idProduct
	if [[ -f $idvendor ]]; then
		dev_vid=`grep -i $vid < $idvendor`
		dev_pid=`grep -i $pid < $idproduct`
		if [[ -n $dev_vid ]] && [[ -n $dev_pid ]]; then
			echo "I found the requested VID/PID:  $dev_vid, $dev_pid"
			for usbdevice in $(ls ${usb_device_path}/${usbdev}); do
				tmp=$(contains ${usbdevice} ${usbdev})
				usb_path2=${usb_path}/${usbdevice}
				if [[ $tmp == "found" ]] && [[ -d ${usb_path2} ]]; then
					for usbinterface in $(ls ${usb_path2}); do
						usb_path3=${usb_path2}/${usbinterface}
						if [[ -d ${usb_path3} ]]; then
							identifyvid=$(contains ${usbinterface} ${vid})
							identifypid=$(contains ${usbinterface} ${pid})
							if [[ -n ${identifyvid} ]] && [[ -n ${identifypid} ]]; then
								if [[ -d ${usb_path3}/hidraw ]]; then
									usb_path4=${usb_path3}/hidraw
									for usbdriver in $(ls ${usb_path4}); do
										identifydriveridx=$(contains ${usbdriver} hidraw)
										if [[ ${identifydriveridx} == "found" ]]; then
											echo "MCP2210 can be found at \"/dev/${usbdriver}\""
										fi
									done
								fi
							fi
						fi
					done
				fi
			done
		fi
	fi
done



