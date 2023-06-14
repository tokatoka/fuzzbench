#!/usr/bin/python3
import subprocess

    
fuzzers = [
    "build-libafl_lto-openssl_x509",
    "build-libafl_lto-php_php-fuzz-parser_0dbedb",
    "build-libafl_lto-re2_fuzzer",
    "build-libafl_lto-sqlite3_ossfuzz",
    "build-libafl_lto-stb_stbi_read_fuzzer",
    "build-libafl_lto-vorbis_decode_fuzzer",
    "build-libafl_lto-woff2_convert_woff2ttf_fuzzer",
    "build-libafl_lto-zlib_zlib_uncompress_fuzzer",
]

for fuzzer in fuzzers:
    try:
        subprocess.run(["make", fuzzer])
    except:
        pass
