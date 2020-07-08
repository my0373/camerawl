# Purpose
Camerawl is a project to automate the download, backup, naming of digital photos. The name comes from the Bristolian word for Camera.

## The problem
As with all software projects, this project is designed to solve a specific problem. Photographers spend too much time organising and backing up images. Often images are renamed, reindexed and stored, and backed up on multiple drives, directories, devices and cloud platforms. Often these files are modified and stored in finished formats. Metadata about the images needs to be kept.

For many of us, we have the skills to create automated workflows using proprietory tools such as Adobe Bridge, and tools such as rsync and automation scripts, however it would be awesome if there was a way to create a device that could manage this for us.

We live in an era of cheap, low power hardware (Raspberry Pi's), powerful open source software and open standards for communicating with devices, network file systems and cloud providers.

This project aims to create a device that makes life easier for photographers.

## The problems to be solved
### Device provisioning
1) What hardware do we require ? 
* USB hub ?
* Raspberry PI 4B 8GB ?
* Memory card ? What size ?
* Network connectivity ?

2) How do we define and provision an OS (Linux) onto a Raspberry PI ?
* which linux distro will we use ?
* Create a custom image on an SD card ?
* Can we network boot ?
* What devices will we support ?


3) How do we configure the OS ?
* How will we keep it patched and up to date ?
* How will we simplify the configuration of the OS ? 
    * Is cockpit an option ?
    * Do we write a custom portal ?
    * Phone app ?

4) External media
* How do we detect when new media has been physically inserted ?
* Can we trigger when an external disk is inserted ?
* What do we trigger when an external disk is inserted ?
* How do we safely remove external media ? 
    * Physical button ?
    * Web portal ?
    * Phone app ?