# Script generated with Bloom
pkgdesc="ROS - MoveIt launch files"


pkgname='ros-kinetic-cob-moveit-bringup'
pkgver='0.7.1_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-cob-hardware-config'
'ros-kinetic-cob-moveit-config'
'ros-kinetic-joint-state-publisher'
'ros-kinetic-moveit-planners-ompl'
'ros-kinetic-moveit-plugins'
'ros-kinetic-moveit-ros-move-group'
'ros-kinetic-moveit-ros-perception'
'ros-kinetic-moveit-ros-visualization'
'ros-kinetic-moveit-setup-assistant'
'ros-kinetic-robot-state-publisher'
'ros-kinetic-tf'
)

conflicts=()
replaces=()

_dir=cob_moveit_bringup
source=()
md5sums=()

prepare() {
    cp -R $startdir/cob_moveit_bringup $srcdir/cob_moveit_bringup
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

