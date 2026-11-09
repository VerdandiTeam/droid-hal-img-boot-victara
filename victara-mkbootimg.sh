#!/bin/sh
set -e

INITRD=$1
OUT=$2

CMDLINE='console=tty0 systemd.show_status=false msm.allow_vram_carveout=1 msm.vram=128m mem_sleep_default=s2idle'
DTB=qcom-msm8974pro-motorola-victara.dtb

cat /boot/zImage /boot/$DTB > zImage-dtb

python3 mkbootimg.py --kernel zImage-dtb --ramdisk "$INITRD" --base 0x00000000 --kernel_offset 0x00008000 \
    --ramdisk_offset 0x02000000 --second_offset 0x00f00000 --tags_offset 0x00000100 --pagesize 2048 \
    --header_version 0 --cmdline "$CMDLINE" --output "$OUT"

if [ "$OUT" = hybris-boot.img ]; then
    cp "$INITRD" initrd.img

    cat > extlinux.conf <<EXT
default sailfish

label sailfish
    linux /sailfish/zImage
    fdt /sailfish/$DTB
    initrd /sailfish/initrd.img
    append $CMDLINE
EXT
fi
