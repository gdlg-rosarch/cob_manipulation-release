# Script generated with Bloom
pkgdesc="ROS - cob_lookat_action"
url='http://ros.org/wiki/cob_manipulation/'

pkgname='ros-kinetic-cob-lookat-action'
pkgver='0.7.1_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('boost'
'ros-kinetic-actionlib'
'ros-kinetic-actionlib-msgs'
'ros-kinetic-catkin'
'ros-kinetic-control-msgs'
'ros-kinetic-geometry-msgs'
'ros-kinetic-kdl-conversions'
'ros-kinetic-kdl-parser'
'ros-kinetic-message-generation'
'ros-kinetic-orocos-kdl'
'ros-kinetic-roscpp'
'ros-kinetic-tf'
'ros-kinetic-tf-conversions'
'ros-kinetic-trajectory-msgs'
)

depends=('boost'
'ros-kinetic-actionlib'
'ros-kinetic-actionlib-msgs'
'ros-kinetic-control-msgs'
'ros-kinetic-geometry-msgs'
'ros-kinetic-kdl-conversions'
'ros-kinetic-kdl-parser'
'ros-kinetic-message-runtime'
'ros-kinetic-orocos-kdl'
'ros-kinetic-roscpp'
'ros-kinetic-rospy'
'ros-kinetic-tf'
'ros-kinetic-tf-conversions'
'ros-kinetic-trajectory-msgs'
)

conflicts=()
replaces=()

_dir=cob_lookat_action
source=()
md5sums=()

prepare() {
    cp -R $startdir/cob_lookat_action $srcdir/cob_lookat_action
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

