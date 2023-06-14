#!/usr/bin/python3
import subprocess

    
fuzzers = [
    "build-libafl_lto-bloaty_fuzz_target",
    "build-libafl_lto-harfbuzz_hb-shape-fuzzer",
    "build-libafl_lto-libjpeg-turbo_libjpeg_turbo_fuzzer",
    "build-libafl_lto-libpcap_fuzz_both",
    "build-libafl_lto-systemd_fuzz-link-parser",
    "build-libafl_lto-proj4_proj_crs_to_crs_fuzzer",
    "build-libafl_lto-openthread_ot-ip6-send-fuzzer",
    "build-libafl_lto-mbedtls_fuzz_dtlsclient",
]

for fuzzer in fuzzers:
    try:
        subprocess.run(["make", fuzzer])
    except:
        pass
