#!/usr/bin/python3
import subprocess

    
fuzzers = [
    "build-libafl_analysis_no_lto-openssl_x509",
    "build-libafl_analysis_no_lto-php_php-fuzz-parser_0dbedb",
    "build-libafl_analysis_no_lto-re2_fuzzer",
    "build-libafl_analysis_no_lto-sqlite3_ossfuzz",
    "build-libafl_analysis_no_lto-stb_stbi_read_fuzzer",
    "build-libafl_analysis_no_lto-vorbis_decode_fuzzer",
    "build-libafl_analysis_no_lto-woff2_convert_woff2ttf_fuzzer",
    "build-libafl_analysis_no_lto-zlib_zlib_uncompress_fuzzer",
]

for fuzzer in fuzzers:
    try:
        subprocess.run(["make", fuzzer])
    except:
        pass
