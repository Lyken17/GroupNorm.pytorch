import os
import glob

import torch
from torch.utils.ffi import create_extension


this_file = os.path.dirname(__file__)

# sources = ['src/new_lib.c']
# headers = ['src/new_lib.h']

all_sources = glob.glob("src/**/*.c", recursive=True)
all_headers = glob.glob("src/**/*.h")

cu_sources = glob.glob("src/**/*_cuda.c")
cu_headers = glob.glob("src/**/*_cuda.h")

sources = list(set(all_sources) - set(cu_sources))
headers = list(set(all_headers) - set(cu_headers))

defines = []

with_cuda = False

if torch.cuda.is_available():
    print('Including CUDA code.')
    # sources += ['src/new_lib_cuda.c']
    sources += cu_sources
    # headers += ['src/new_lib_cuda.h']
    headers += cu_headers
    defines += [('WITH_CUDA', None)]
    with_cuda = True

ffi = create_extension(
    '_ext.new_lib',
    headers=headers,
    sources=sources,
    define_macros=defines,
    relative_to=__file__,
    with_cuda=with_cuda,
    extra_compile_args=["-std=c99"]
)

if __name__ == '__main__':
    ffi.build()
