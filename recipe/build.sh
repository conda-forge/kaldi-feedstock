#! /usr/bin/env bash

mkdir build

pushd build


cmake -GNinja -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_LIBDIR=${PREFIX}/lib \
              -DCONDA_ROOT="${BUILD_PREFIX}" \
              -DCMAKE_INSTALL_PREFIX=${PREFIX} -DCMAKE_INSTALL_BINDIR=${PREFIX}/bin  -DKALDI_BUILD_TEST=OFF  -DMATHLIB=OpenBLAS \
              -DOVERRIDE_KALDI_VERSION=${PKG_VERSION} ..


cmake --build . --verbose --config Release -- -v -j ${CPU_COUNT}

cmake --install . --component conda_kaldi --verbose --config Release


popd
