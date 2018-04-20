# Script generated with Bloom
pkgdesc="ROS - An action interface to MoveIt!'s pick-and-place for Care-O-bot"
url='http://ros.org/wiki/cob_manipulation/'

pkgname='ros-kinetic-cob-pick-place-action'
pkgver='0.7.1_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('ros-kinetic-actionlib'
'ros-kinetic-actionlib-msgs'
'ros-kinetic-catkin'
'ros-kinetic-cob-grasp-generation'
'ros-kinetic-cob-moveit-interface'
'ros-kinetic-geometric-shapes'
'ros-kinetic-geometry-msgs'
'ros-kinetic-message-generation'
'ros-kinetic-moveit-msgs'
'ros-kinetic-moveit-ros-move-group'
'ros-kinetic-moveit-ros-planning-interface'
'ros-kinetic-roscpp'
'ros-kinetic-std-msgs'
'ros-kinetic-tf'
)

depends=('ros-kinetic-actionlib'
'ros-kinetic-actionlib-msgs'
'ros-kinetic-cob-grasp-generation'
'ros-kinetic-cob-moveit-interface'
'ros-kinetic-geometric-shapes'
'ros-kinetic-geometry-msgs'
'ros-kinetic-message-runtime'
'ros-kinetic-moveit-msgs'
'ros-kinetic-moveit-ros-move-group'
'ros-kinetic-moveit-ros-planning-interface'
'ros-kinetic-roscpp'
'ros-kinetic-rospy'
'ros-kinetic-std-msgs'
'ros-kinetic-tf'
)

conflicts=()
replaces=()

_dir=cob_pick_place_action
source=()
md5sums=()

prepare() {
    cp -R $startdir/cob_pick_place_action $srcdir/cob_pick_place_action
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

