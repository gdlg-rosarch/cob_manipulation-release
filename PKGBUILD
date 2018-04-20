# Script generated with Bloom
pkgdesc="ROS - This package provides nodes for calculating the minimal distance to robot links, obstacles and octomap using MoveIt!'s PlanningSceneMonitor"


pkgname='ros-kinetic-cob-obstacle-distance-moveit'
pkgver='0.7.1_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('boost'
'fcl'
'pkg-config'
'ros-kinetic-catkin'
'ros-kinetic-cob-control-msgs'
'ros-kinetic-cob-srvs'
'ros-kinetic-eigen-conversions'
'ros-kinetic-geometric-shapes'
'ros-kinetic-geometry-msgs'
'ros-kinetic-moveit-core'
'ros-kinetic-moveit-msgs'
'ros-kinetic-moveit-ros-perception'
'ros-kinetic-moveit-ros-planning-interface'
'ros-kinetic-roscpp'
'ros-kinetic-tf'
'ros-kinetic-tf-conversions'
)

depends=('boost'
'fcl'
'pkg-config'
'ros-kinetic-cob-control-msgs'
'ros-kinetic-cob-srvs'
'ros-kinetic-eigen-conversions'
'ros-kinetic-geometric-shapes'
'ros-kinetic-geometry-msgs'
'ros-kinetic-moveit-core'
'ros-kinetic-moveit-msgs'
'ros-kinetic-moveit-ros-perception'
'ros-kinetic-moveit-ros-planning-interface'
'ros-kinetic-roscpp'
'ros-kinetic-rospy'
'ros-kinetic-tf'
'ros-kinetic-tf-conversions'
)

conflicts=()
replaces=()

_dir=cob_obstacle_distance_moveit
source=()
md5sums=()

prepare() {
    cp -R $startdir/cob_obstacle_distance_moveit $srcdir/cob_obstacle_distance_moveit
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

