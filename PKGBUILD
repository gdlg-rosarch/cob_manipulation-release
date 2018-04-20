# Script generated with Bloom
pkgdesc="ROS - The cob_manipulation stack includes packages that provide manipulation capabilities for Care-O-bot."
url='http://ros.org/wiki/cob_manipulation/'

pkgname='ros-kinetic-cob-manipulation'
pkgver='0.7.1_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-cob-collision-monitor'
'ros-kinetic-cob-grasp-generation'
'ros-kinetic-cob-lookat-action'
'ros-kinetic-cob-moveit-bringup'
'ros-kinetic-cob-moveit-interface'
'ros-kinetic-cob-obstacle-distance-moveit'
'ros-kinetic-cob-pick-place-action'
)

conflicts=()
replaces=()

_dir=cob_manipulation
source=()
md5sums=()

prepare() {
    cp -R $startdir/cob_manipulation $srcdir/cob_manipulation
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

