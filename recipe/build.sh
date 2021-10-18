#! /usr/bin/env bash

mkdir build

pushd build


cmake -GNinja -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_LIBDIR=${PREFIX}/lib -DCMAKE_INSTALL_PREFIX=${PREFIX}  -DKALDI_BUILD_TEST=OFF  -DMATHLIB=OpenBLAS -DBLAS_LIBRARIES=${PREFIX}/lib/libopenblas${SHLIB_EXT} -DLAPACK_LIBRARIES=${PREFIX}/lib/libopenblas${SHLIB_EXT} ..

cmake --build . --target install --config Release -- -j ${CPU_COUNT}

popd
