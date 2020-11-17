# ubuntu-configuration
## Repo for the configuration of Ubuntu after minimal installation

This repo is useful for configuration of ubuntu and installation of useful packages for my work.
The configuration will be composed by:
- Installation of git
- Installation of gnome-tweaks
- Installation of miniconda and python libraries
- Mount external volumes

## Installation of git
To install git use:
```
sudo apt install git
```

## Installation of gnome-tweaks
To install gnome-tweaks use:
```
apt install gnome-tweaks
```

## Installation of miniconda and python libraries

To install miniconda first we have to clone this repository:
```
git clone https://github.com/riccardoscheda/ubuntu-configuration
```
 
Then we have to run bash files:
```
cd ubuntu-configuration
bash install-conda.sh
```

During installation press Enter and yes when asked.
Then we can install python libraries and also Spyder:

```
bash pylibraries.sh
```

Now we have ubuntu configurated.

## Mount external volumes

To mount external volumes (ntfs) we have modify the file /etc/fstab. So, first we have to create the mount point:

```
mkdir /media/dati 
```
Then, we have to take the information of the volume we want to mount.
First, use fdisk command to list of all partitions:

```
sudo fdisk -l
```
The output will be something like that:
```
Device         Start       End   Sectors  Size Type
/dev/sda1       2048    534527    532480  260M EFI System
/dev/sda2     534528    567295     32768   16M Microsoft reserved
/dev/sda3     567296 188228801 187661506 89,5G Microsoft basic data
/dev/sda5  189360128 860399615 671039488  320G Microsoft basic data
/dev/sda6  860399616 982095871 121696256   58G Linux filesystem
/dev/sda7  982095872 999192575  17096704  8,2G Microsoft basic data

```
In my case i want to mount the 320G partition, so `/dev/sda5`.

Next use the blkid command to get the UUID of partitions. The uuid is necessary to add the partitions to the fstab file. 
```
sudo blkid
```
Output:
```
/dev/sda1: LABEL="SYSTEM" UUID="BA26-B19F" TYPE="vfat" PARTLABEL="EFI system partition" PARTUUID="6e0d1331-1454-430f-92dc-e639cbf5fa51"
/dev/sda2: PARTLABEL="Microsoft reserved partition" PARTUUID="d20ffaf7-65b0-4477-9e3c-e2e488e7faa3"
/dev/sda3: LABEL="OS" UUID="01D37E334FCB9410" TYPE="ntfs" PARTLABEL="Basic data partition" PARTUUID="3f7d7249-4e5c-4aa9-8ef7-74745099451c"
/dev/sda5: LABEL="DATI" UUID="01D37E31970BDA30" TYPE="ntfs" PARTLABEL="Basic data partition" PARTUUID="4fd9ebf0-7e33-01d3-f8f5-eca719bfe900"
/dev/sda6: UUID="442cd4b2-28fe-4fb1-bed3-b214bd964bb7" TYPE="ext4" PARTUUID="547712b7-2cde-423d-a997-42f8965e12a9"
/dev/sda7: UUID="f6355da4-8ef1-4e2f-84e5-3a64f11082a1" TYPE="swap" PARTLABEL="Basic data partition" PARTUUID="0001297f-2ba0-6034-33fe-db3bfe520200"

```
So I need the UUID `01D37E31970BDA30`. Now we have to add this partition in file fstab:
```
sudo gedit /etc/fstab
```
and insert 
```
############### PARTIZIONE DATI #################
UUID=01D37E31970BDA30	/media/dati	ntfs	errors=remount-ro	0	1	
```

Then reboot
