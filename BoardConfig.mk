#
# Copyright (C) 2025 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from xiaomi sm8550-common
include device/xiaomi/sm8550-common/BoardConfigCommon.mk

# Inherit from the proprietary version
include vendor/xiaomi/nuwa/BoardConfigVendor.mk

DEVICE_PATH := device/xiaomi/nuwa

# Kernel
BOOT_KERNEL_MODULES += \
	fts_touch_spi.ko

BOARD_VENDOR_KERNEL_MODULES_LOAD += \
	cs35l41_dlkm.ko \
	goodix_fod.ko \
	fts_touch_spi.ko

# Display
TARGET_SCREEN_DENSITY := 560

# Properties
TARGET_ODM_PROP += $(DEVICE_PATH)/properties/odm.prop