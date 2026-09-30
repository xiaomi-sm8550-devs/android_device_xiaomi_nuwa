#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

import extract_utils.tools


from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_vendorcompat,
    lib_fixups_user_type,
    libs_proto_3_9_1,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/xiaomi/sm8550-common',
    'hardware/qcom-caf/sm8550',
    'hardware/xiaomi',
    'vendor/qcom/opensource/commonsys-intf/display',
    'vendor/xiaomi/sm8550-common',
]

lib_fixups: lib_fixups_user_type = {
    libs_proto_3_9_1: lib_fixup_vendorcompat,
}

blob_fixups: blob_fixups_user_type = {
    'odm/lib64/com.qti.feature2.gs.sm8550.so': blob_fixup()
        .sig_replace('3f d1 00 71', '3f d5 00 71')
        .sig_replace('10 14 c0 f2', '90 14 c0 f2')
        .sig_replace('10 02 e0 f2', '10 06 e0 f2'),
    'odm/lib64/com.qti.feature2.rt.so': blob_fixup()
        .sig_replace('d1 12 40 b9', 'f1 82 40 b9'),
    (
        'odm/etc/camera/enhance_motiontuning.xml',
        'odm/etc/camera/night_motiontuning.xml',
        'odm/etc/camera/motiontuning.xml'
    ): blob_fixup()
        .regex_replace('xml=version', 'xml version'),
    (
        'odm/lib64/libcamxcommonutils.so',
        'odm/lib64/hw/com.qti.chi.override.so',
        'odm/lib64/libchifeature2.so',
        'odm/lib64/libmialgoengine.so'
    ): blob_fixup()
        .add_needed('libprocessgroup_shim.so'),
    (
        'odm/lib64/libMiPhotoFilter.so',
        'odm/lib64/libTrueSight.so',
    ): blob_fixup()
        .clear_symbol_version('AHardwareBuffer_allocate')
        .clear_symbol_version('AHardwareBuffer_describe')
        .clear_symbol_version('AHardwareBuffer_lockPlanes')
        .clear_symbol_version('AHardwareBuffer_release')
        .clear_symbol_version('AHardwareBuffer_unlock')
        .clear_symbol_version('AHardwareBuffer_isSupported'),
    'odm/lib64/libTrueSight.so': blob_fixup()
        .clear_symbol_version('AHardwareBuffer_lock'),
    'odm/lib64/libmorpho_ubwc.so': blob_fixup()
        .clear_symbol_version('AHardwareBuffer_describe'),
    'odm/lib64/hw/camera.xiaomi.so': blob_fixup()
        .add_needed('libprocessgroup_shim.so')
        .replace_needed('libui.so', 'libui-v34.so'),
    (
        'odm/bin/hw/vendor.qti.camera.provider-service_64',
        'odm/lib64/camx.provider-impl.so',
        'odm/lib64/camera/plugins/com.xiaomi.plugin.mialgosnsc.so',
        'odm/lib64/com.qti.feature2.anchorsync.so'
    ): blob_fixup().replace_needed('libtinyxml2.so', 'libtinyxml2-v34.so'),
    'vendor/lib64/libsnpe_config.so': blob_fixup()
        .add_needed('liblog.so'),
}

module = ExtractUtilsModule(
    'nuwa',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    check_elf=True,
    add_firmware_proprietary_file=True,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'sm8550-common', module.vendor
    )
    utils.run()
