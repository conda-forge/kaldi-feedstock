setlocal EnableDelayedExpansion

mkdir build

cd build

cmake -GNinja  -DOVERRIDE_KALDI_VERSION="%PKG_VERSION%" -DCMAKE_BUILD_TYPE=Release ^
                -DCONDA_ROOT="%LIBRARY_PREFIX%" ^
                -DCMAKE_INSTALL_PREFIX="%LIBRARY_PREFIX%"  ^
                -DKALDI_BUILD_TEST=OFF ..

cmake --build . --verbose --config Release -- -v -j %CPU_COUNT%

cmake --install . --component conda_kaldi --verbose --config Release