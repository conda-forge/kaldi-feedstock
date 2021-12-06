#! /usr/bin/env bash

mkdir build

pushd build


cmake -GNinja ${CMAKE_ARGS} -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON -DCMAKE_BUILD_TYPE=Release \
              -DCONDA_ROOT="${PREFIX}" \
              -DCMAKE_INSTALL_PREFIX="${PREFIX}"   -DKALDI_BUILD_TEST=OFF \
              -DOVERRIDE_KALDI_VERSION="${PKG_VERSION}" ..


cmake --build . --verbose --config Release -- -v -j ${CPU_COUNT}

cmake --install . --component kaldi --verbose --config Release


popd
