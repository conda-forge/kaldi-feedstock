#! /usr/bin/env bash

mkdir build

pushd build


cmake -GNinja -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_LIBDIR=${PREFIX}/lib -DCMAKE_INSTALL_PREFIX=${PREFIX}  -DKALDI_BUILD_TEST=OFF  -DMATHLIB=OpenBLAS -DOVERRIDE_KALDI_VERSION=${PKG_VERSION} ..

cmake --build . --target install --config Release -- -j ${CPU_COUNT}

#  Clean up libfst.so style files to prevent compatibility issues with openfst package, Kaldi will be linked to libfst.so.16 or libfst.16.dylib

rm -rf ${PREFIX}/lib/fst
rm -rf ${PREFIX}/include/fst

rm ${PREFIX}/lib/libfst${SHLIB_EXT}
rm ${PREFIX}/lib/libfstscript${SHLIB_EXT}
rm ${PREFIX}/lib/libfstcompact${SHLIB_EXT}
rm ${PREFIX}/lib/libfstconst${SHLIB_EXT}
rm ${PREFIX}/lib/libfstfar${SHLIB_EXT}
rm ${PREFIX}/lib/libfstfarscript${SHLIB_EXT}
rm ${PREFIX}/lib/libfstlinearscript${SHLIB_EXT}
rm ${PREFIX}/lib/libfstlookahead${SHLIB_EXT}
rm ${PREFIX}/lib/libfstmpdtscript${SHLIB_EXT}
rm ${PREFIX}/lib/libfstngram${SHLIB_EXT}
rm ${PREFIX}/lib/libngram_fst${SHLIB_EXT}
rm ${PREFIX}/lib/libfstpdtscript${SHLIB_EXT}
rm ${PREFIX}/lib/libfstspecial${SHLIB_EXT}

popd
