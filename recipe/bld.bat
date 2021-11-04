setlocal EnableDelayedExpansion

mkdir build

cd build

cmake -GNinja  -DOVERRIDE_KALDI_VERSION="%PKG_VERSION%" -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_LIBDIR="%PREFIX%\Library\lib" ^
                -DCONDA_ROOT="%BUILD_PREFIX%\Library" ^
                 -DCMAKE_INSTALL_BINDIR="%PREFIX%\Library\bin" ^
                -DCMAKE_INSTALL_PREFIX="%LIBRARY_PREFIX%" -DCMAKE_PREFIX_PATH:PATH="%LIBRARY_PREFIX%"  ^
                -DKALDI_BUILD_TEST=OFF  -DMATHLIB=MKL ..

cmake --build . --verbose --config Release -- -v -j %CPU_COUNT%

cmake --install . --component conda_kaldi --verbose --config Release