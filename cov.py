#!/usr/bin/python3
import subprocess

    
fuzzers = [
    "build-libafl_lto-curl_curl_fuzzer_http",
    "build-libafl_lto-freetype2_ftfuzzer",
    "build-libafl_lto-jsoncpp_jsoncpp_fuzzer",
    "build-libafl_lto-lcms_cms_transform_fuzzer",
    "build-libafl_lto-libpng_libpng_read_fuzzer",
    "build-libafl_lto-libxml2_xml",
    "build-libafl_lto-libxslt_xpath",
    "build-libafl_lto-openh264_decoder_fuzzer",
]

for fuzzer in fuzzers:
    try:
        subprocess.run(["make", fuzzer])
    except:
        pass
