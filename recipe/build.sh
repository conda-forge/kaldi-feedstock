#! /usr/bin/env bash

pushd tools

make cub openfst portaudio -k ${CPU_COUNT}

popd

pushd src

./configure --shared --mathlib=OPENBLAS --openblas-root=${PREFIX} --static-fst=yes --use-cuda=no
make -j ${CPU_COUNT}

# Move binaries
find . -type f -executable -regex '.*bin/.*' -exec cp {} ${PREFIX}/bin \;

popd
