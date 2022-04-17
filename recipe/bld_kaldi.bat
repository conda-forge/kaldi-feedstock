setlocal EnableDelayedExpansion

mkdir build
cd build

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

cmake -GNinja ^
    -DCMAKE_BUILD_TYPE=Release ^
    -DCONDA_ROOT="%LIBRARY_PREFIX%" ^
    -DCMAKE_INSTALL_PREFIX="%LIBRARY_PREFIX%" ^
    -DKALDI_VERSION="%PKG_VERSION%" ^
    -DBUILD_SHARED_LIBS=OFF ^
    -DKALDI_BUILD_TEST=OFF ^
    ..
if %ERRORLEVEL% neq 0 exit 1

cmake --build . --verbose --config Release -- -v -j %CPU_COUNT%
if %ERRORLEVEL% neq 0 exit 1

cmake --install . --component kaldi --verbose --config Release
if %ERRORLEVEL% neq 0 exit 1