# Building and using the operating system image for Camerawl.
## What OS are we using ?
After looking at a number of Operating Systems, it's been decided that Ubuntu will be the best choice. This gives us the benefit of support for PI 1,2,3,4 and 4b images. It gives us some benefits of revieving regular patches, as well as a way to easily obtain new packages without having to re-invent the wheel.

At the time of writing, I have a number of RPI 4B's. All of my testing is based around 64bit version of Ubuntu for Rasberry PI.

The OS images i'm using can be found here.
http://cdimage.ubuntu.com/ubuntu-server/daily-preinstalled/current/HEADER.html

## Are we tweaking the images ?
Yes, so once the images are downloaded, they are unpacked

`$ gunzip groovy-preinstalled-server-arm64+raspi.img.xz`
