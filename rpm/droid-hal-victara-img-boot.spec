%define device victara

%define native_build 1
%define disable_tools 1

%define mkbootimg_cmd sh victara-mkbootimg.sh %{initrd}

%define root_part_label userdata

%define display_brightness_path /sys/class/backlight/fd922800.dsi.0/brightness
%define display_brightness 100

%define lvm_root_size 5000

%global __spec_install_post \
install -D -m 644 /boot/zImage $RPM_BUILD_ROOT/boot/sailfish/zImage\
install -D -m 644 /boot/qcom-msm8974pro-motorola-victara.dtb $RPM_BUILD_ROOT/boot/sailfish/qcom-msm8974pro-motorola-victara.dtb\
install -D -m 644 initrd.img $RPM_BUILD_ROOT/boot/sailfish/initrd.img\
install -D -m 644 extlinux.conf $RPM_BUILD_ROOT/boot/extlinux/extlinux.conf\
install -D -m 644 lk2nd.img $RPM_BUILD_ROOT/boot/lk2nd.img\
%{?__spec_install_post}

BuildRequires:  python3-base

%include initrd/droid-hal-device-img-boot.inc

%package -n droid-hal-%{device}-extlinux
Summary:    lk2nd extlinux boot files for %{device}
Requires:   droid-hal-%{device}-img-boot = %{version}-%{release}

%description -n droid-hal-%{device}-extlinux
%{summary}

%pre -n droid-hal-%{device}-extlinux
if [ $1 -gt 1 ] && ! grep -q ' /boot ' /proc/mounts; then
    echo "/boot (customize) is not mounted, refusing to update the boot files"
    exit 1
fi

%files -n droid-hal-%{device}-extlinux
%defattr(644,root,root,-)
/boot/sailfish/zImage
/boot/sailfish/qcom-msm8974pro-motorola-victara.dtb
/boot/sailfish/initrd.img
/boot/extlinux/extlinux.conf
/boot/lk2nd.img
