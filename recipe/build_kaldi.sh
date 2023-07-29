#! /usr/bin/env bash


export CFLAGS="$(echo $CFLAGS | sed 's/-fvisibility-inlines-hidden//g')"
export CXXFLAGS="$(echo $CXXFLAGS | sed 's/-fvisibility-inlines-hidden//g')"
export LDFLAGS="$(echo $LDFLAGS | sed 's/-Wl,--as-needed//g')"
export LDFLAGS="$(echo $LDFLAGS | sed 's/-Wl,-dead_strip_dylibs//g')"
export LDFLAGS_LD="$(echo $LDFLAGS_LD | sed 's/-dead_strip_dylibs//g')"
export CXXFLAGS="$CXXFLAGS -Wno-deprecated-declarations"
export CFLAGS="$CFLAGS -Wno-deprecated-declarations"

if [[ "$target_platform" == "osx-64" ]]; then
  export CXXFLAGS="$CXXFLAGS -DTARGET_OS_OSX=1"
  export CFLAGS="$CFLAGS -DTARGET_OS_OSX=1"
fi

export CMAKE_GENERATOR=Ninja
export CMAKE_SYSROOT=$CONDA_BUILD_SYSROOT
export CMAKE_LIBRARY_PATH=$PREFIX/lib:$PREFIX/include:$CMAKE_LIBRARY_PATH
export CMAKE_INCLUDE_PATH=$PREFIX/include:CMAKE_INCLUDE_PATH
export CMAKE_PREFIX_PATH=$PREFIX

for ARG in $CMAKE_ARGS; do
  if [[ "$ARG" == "-DCMAKE_"* ]]; then
    cmake_arg=$(echo $ARG | cut -d= -f1)
    cmake_arg=$(echo $cmake_arg| cut -dD -f2-)
    cmake_val=$(echo $ARG | cut -d= -f2-)
    printf -v $cmake_arg "$cmake_val"
    export ${cmake_arg}
  fi
done
export USE_NINJA=ON

CXXFLAGS="${CXXFLAGS} -D_LIBCPP_DISABLE_AVAILABILITY"

if [[ "$CONDA_BUILD_CROSS_COMPILATION" == 1 ]]; then
    export COMPILER_WORKS_EXITCODE=0
    export COMPILER_WORKS_EXITCODE__TRYRUN_OUTPUT=""
fi

if [[ "$OSTYPE" == "darwin"* ]]; then
    # Produce macOS builds with torch.distributed support.
    # This is enabled by default on Linux, but disabled by default on macOS,
    # because it requires an non-bundled compile-time dependency (libuv
    # through gloo). This dependency is made available through meta.yaml, so
    # we can override the default and set USE_DISTRIBUTED=1.
    export USE_DISTRIBUTED=1

    if [[ "$target_platform" == "osx-arm64" ]]; then
        export USE_MKLDNN=0
        # There is a problem with pkg-config
        # See https://github.com/conda-forge/pkg-config-feedstock/issues/38
        export USE_DISTRIBUTED=0
    fi
fi

if [[ ${cuda_compiler_version} != "None" ]]; then
    export USE_CUDA=1
    export NCCL_ROOT_DIR=$PREFIX
    export NCCL_INCLUDE_DIR=$PREFIX/include
    export USE_SYSTEM_NCCL=1
    export USE_STATIC_NCCL=0
    export USE_STATIC_CUDNN=0
    export CUDA_TOOLKIT_ROOT_DIR=$CUDA_HOME
    export MAGMA_HOME="${PREFIX}"
else
    export USE_CUDA=0
fi

export CMAKE_BUILD_TYPE=Release
export BUILD_SHARED_LIBS=ON
export CMAKE_BUILD_WITH_INSTALL_RPATH=ON
export CMAKE_INSTALL_LIBDIR=lib
export CMAKE_CXX_STANDARD=17

mkdir build

pushd build

if [[ "${target_platform}" == "linux-64" ]] && [[ "${cuda_compiler_version}" =~ 12.* ]]; then
    # Cuda 12.0 places files in the targets/platform directory structure rather than in PREFIX/lib and PREFIX/include
    CMAKE_ARGS="${CMAKE_ARGS} -DCUDA_TOOLKIT_ROOT_DIR=${PREFIX}/targets/x86_64-linux"
fi

cmake ${CMAKE_ARGS} \
    -DCMAKE_INSTALL_PREFIX="${PREFIX}" \
    -DCONDA_ROOT="${PREFIX}" \
    -DBUILD_SHARED_LIBS=ON \
    -DKALDI_BUILD_TEST=OFF \
    -DKALDI_VERSION="${PKG_VERSION}" \
    ..


cmake --build . --verbose --config Release -- -v -j ${CPU_COUNT}

cmake --install . --component kaldi --verbose --config Release


popd
