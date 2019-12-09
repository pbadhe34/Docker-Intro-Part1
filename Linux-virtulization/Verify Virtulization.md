     
Install cpu-checker

$ sudo apt-get update
$ sudo apt-get install cpu-checker

Then check:

$ kvm-ok

If the CPU is enabled, you should see something like:

INFO: /dev/kvm exists
KVM acceleration can be used

Otherwise, you might see something like:

INFO: /dev/kvm does not exist
HINT:   sudo modprobe kvm_intel
INFO: Your CPU supports KVM extensions
INFO: KVM (vmx) is disabled by your BIOS
HINT: Enter your BIOS setup and enable Virtualization Technology (VT),
      and then hard poweroff/poweron your system
KVM acceleration can NOT be used

Hardware Virtulization
Enabling virtualization extensions in BIOS

    Reboot the computer and open the system's BIOS menu. 
    This can usually be done by pressing the delete/F12 key, the F1 key or Alt and F4 keys depending on the system.
    Select Restore Defaults or Restore Optimized Defaults, and then select Save & Exit.
    Power off the machine and disconnect the power supply.

1.Power on the machine and open the BIOS (as per Step 1).
2.Open the Processor submenu The processor settings menu may be hidden in the Chipset, Advanced CPU Configuration or Northbridge.
3.Enable Intel Virtualization Technology (also known as Intel VT) or AMD-V depending on the brand of the processor. 
4.The virtualization extensions may be labeled Virtualization Extensions, Vanderpool or various other names depending on the OEM and system BIOS.
5.Enable Intel VTd or AMD IOMMU, if the options are available. Intel VTd and AMD IOMMU are used for PCI passthrough.
Select Save & Exit. 

*******************************

  Run lscpu commnad from terminal
  Check the Virtualization option in the output.
******************************************

Verify Intel or AMD 64 bit CPU
 grep -w -o lm /proc/cpuinfo | uniq
 Returns lm that means  AMD or Intel CPU


lm – If you see lm flag means you’ve 64 bit Intel or AMD cpu.
**************************************

    vmx – Intel VT-x, virtualization support enabled in BIOS.
    svm – AMD SVM,virtualization enabled in BIOS.
  Run cat /proc/cpuinfo | grep vmx  : for Intel processor

  OR
 
   Run cat /proc/cpuinfo | grep svm : for AMD CPU

  If the command outputs, the virtualization extensions are now enabled. 
  If there is no output your system may not have the virtualization extensions or the correct BIOS setting enabled. 

to check if your hardware supports virtualization

Verify Intel VT CPU virtualization extensions on a Linux
grep --color vmx /proc/cpuinfo
  On AMD machine
   ***********************


  Check the BIOS settings


Check your BIOS settings

  lscpu
$ egrep -wo 'vmx|ept|vpid|npt|tpr_shadow|flexpriority|vnmi|lm|aes' /proc/cpuinfo | sort | uniq
$ egrep -o '(vmx|svm)' /proc/cpuinfo | sort | uniq


