setlocal EnableDelayedExpansion

mkdir build
cd build

set "LIBRARY_PREFIX=%LIBRARY_PREFIX:\=/%"
echo "%LIBRARY_PREFIX%"

if "%cuda_compiler_version%"=="None" (
    set USE_CUDA=0
) else (
    set USE_CUDA=1
    REM no cf-builds for NCCL on windows yet
    REM set NCCL_ROOT_DIR=%LIBRARY_PREFIX%
    REM set NCCL_INCLUDE_DIR=%LIBRARY_INC%
    set USE_SYSTEM_NCCL=0
    set USE_STATIC_NCCL=0
    set USE_STATIC_CUDNN=0
    set "CUDA_HOME=%CUDA_HOME:\=/%"
    echo "%CUDA_HOME%"
    set CUDA_TOOLKIT_ROOT_DIR=%CUDA_HOME%
    set MAGMA_HOME=%LIBRARY_PREFIX%
)

if "%cuda_compiler_version:~0,2%"=="12" (
    REM header-only on windows as of CUDA 12, see
    REM https://github.com/conda-forge/cuda-nvtx-feedstock/issues/4
    set "CMAKE_EXTRA=-DNvToolExt_INCLUDE_DIR=%LIBRARY_INC%/nvtx3"
)

cmake -GNinja ^
    -DCMAKE_BUILD_TYPE=Release ^
    -DCONDA_ROOT="%LIBRARY_PREFIX%" ^
    -DCMAKE_INSTALL_PREFIX="%LIBRARY_PREFIX%" ^
    -DKALDI_VERSION="%PKG_VERSION%" ^
    -DBUILD_SHARED_LIBS=ON ^
    -DKALDI_BUILD_TEST=OFF ^
    !CMAKE_EXTRA! ^
    ..
if %ERRORLEVEL% neq 0 exit 1

cmake --build . --verbose --config Release -- -v -j %CPU_COUNT%
if %ERRORLEVEL% neq 0 exit 1

cmake --install . --component kaldi --verbose --config Release
if %ERRORLEVEL% neq 0 exit 1
