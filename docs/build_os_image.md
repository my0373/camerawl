# Building and using the operating system image for Camerawl.
## What OS are we using ?
After looking at a number of Operating Systems, it's been decided that Ubuntu will be the best choice. This gives us the benefit of support for PI 1,2,3,4 and 4b images. It gives us some benefits of revieving regular patches, as well as a way to easily obtain new packages without having to re-invent the wheel.

At the time of writing, I have a number of RPI 4B's. All of my testing is based around 64bit version of Ubuntu for Rasberry PI.

The OS images i'm using can be found here.
http://cdimage.ubuntu.com/ubuntu-server/daily-preinstalled/current/HEADER.html

## Are we tweaking the images ?
Yes, we...

* download the 64 Ubuntu image
* uncompress it
* load our configuration
* repack the image
* ready for distribution.

We only store code and config in this git repo so we can quickly rebuild the images on demand.

### Instructions for a mac
#### Download the 64 bit image

`$ curl -o groovy-preinstalled-server-arm64+raspi.img.xz http://cdimage.ubuntu.com/ubuntu-server/daily-preinstalled/current/groovy-preinstalled-server-arm64+raspi.img.xz`

#### Unpack the image

`$ gunzip groovy-preinstalled-server-arm64+raspi.img.xz`

#### Mount the image to the default mac mount point 

 `$ hdiutil mount  ./groovy-preinstalled-server-arm64+raspi.img
$ hdiutil mount  ./groovy-preinstalled-server-arm64+raspi.img
 /dev/disk4          	FDisk_partition_scheme
 /dev/disk4s1        	Windows_FAT_32                 	/Volumes/system-boot
 /dev/disk4s2        	Linux`

#### Modify the config on the disk image

#### Unmount the disk
`$ hdiutil unmount /Volumes/system-boot`

#### Write the image to the sd card.