# Script generated with Bloom
pkgdesc="ROS - The collision monitor uses the planning scene monitor to read the state of the robot and check it for collision with itselt or the environment. It addition a ground plane is added in any case. Can be used as a stand-aloan node or a move_group capability."
url='http://wiki.ros.org/cob_collision_monitor'

pkgname='ros-kinetic-cob-collision-monitor'
pkgver='0.7.1_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-moveit-ros-move-group'
'ros-kinetic-moveit-ros-planning'
'ros-kinetic-pluginlib'
'ros-kinetic-std-msgs'
'ros-kinetic-tf'
)

depends=('ros-kinetic-cob-moveit-config'
'ros-kinetic-moveit-ros-move-group'
'ros-kinetic-moveit-ros-planning'
'ros-kinetic-pluginlib'
'ros-kinetic-std-msgs'
'ros-kinetic-tf'
)

conflicts=()
replaces=()

_dir=cob_collision_monitor
source=()
md5sums=()

prepare() {
    cp -R $startdir/cob_collision_monitor $srcdir/cob_collision_monitor
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

