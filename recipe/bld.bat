
mkdir build

cd build

cmake -GNinja  -DOVERRIDE_KALDI_VERSION=%PKG_VERSION% -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_LIBDIR=lib -DCMAKE_INSTALL_PREFIX=%LIBRARY_PREFIX%  -DKALDI_BUILD_TEST=OFF  -DMATHLIB=OpenBLAS ..
if errorlevel 1 exit 1

cmake --build . --target install --config Release -- -j %CPU_COUNT%
if errorlevel 1 exit 1