#
# Copyright (C) 2025 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from xiaomi sm8550-common
$(call inherit-product, device/xiaomi/sm8550-common/common.mk)

# Inherit from the proprietary version
$(call inherit-product, vendor/xiaomi/nuwa/nuwa-vendor.mk)

# DSP Volume Synchronizer
PRODUCT_PACKAGES += \
    DSPVolumeSynchronizer
    
# IFAAService
PRODUCT_PACKAGES += \
    IFAAService

# Init
PRODUCT_COPY_FILES += \
    $(LOCAL_PATH)/init/init.nuwa.rc:$(TARGET_COPY_OUT_VENDOR)/etc/init/init.nuwa.rc \

# Euicc
PRODUCT_PACKAGES += \
    XiaomiEuicc

# Overlay
PRODUCT_PACKAGES += \
    SettingsProviderResNuwa \
    ApertureOverlayNuwa \
    FrameworkResOverlayNuwa \
    SettingsOverlayNuwa \
    SystemUIOverlayNuwa \
    WifiResNuwa

# Sensors
PRODUCT_PACKAGES += \
    sensors.xiaomi.v2

PRODUCT_COPY_FILES += \
    $(LOCAL_PATH)/hals.conf:$(TARGET_COPY_OUT_ODM)/etc/sensors/hals.conf

# PowerShare
PRODUCT_PACKAGES += \
    vendor.lineage.powershare@1.0-service.default

# Soong namespaces
PRODUCT_SOONG_NAMESPACES += \
    $(LOCAL_PATH)
