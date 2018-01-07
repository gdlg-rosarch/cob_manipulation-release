Name:           ros-indigo-cob-grasp-generation
Version:        0.6.6
Release:        1%{?dist}
Summary:        ROS cob_grasp_generation package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://ros.org/wiki/cob_manipulation/
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib
Requires:       ros-indigo-actionlib-msgs
Requires:       ros-indigo-cob-description
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-moveit-msgs
Requires:       ros-indigo-robot-state-publisher
Requires:       ros-indigo-roslib
Requires:       ros-indigo-rospy
Requires:       ros-indigo-rviz
Requires:       ros-indigo-schunk-description
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-tf
Requires:       ros-indigo-tf2-ros
Requires:       ros-indigo-trajectory-msgs
Requires:       ros-indigo-visualization-msgs
Requires:       ros-indigo-xacro
Requires:       scipy
BuildRequires:  ros-indigo-actionlib-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-moveit-msgs

%description
Grasp generation for Care-O-bot based on OpenRAVE

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun Jan 07 2018 Felix Messmer <fxm@ipa.fhg.de> - 0.6.6-1
- Autogenerated by Bloom

* Sun Jan 07 2018 Felix Messmer <fxm@ipa.fhg.de> - 0.6.6-0
- Autogenerated by Bloom

* Mon Jul 31 2017 Felix Messmer <fxm@ipa.fhg.de> - 0.6.5-1
- Autogenerated by Bloom

* Mon Jul 31 2017 Felix Messmer <fxm@ipa.fhg.de> - 0.6.5-0
- Autogenerated by Bloom

* Fri Apr 01 2016 Felix Messmer <fxm@ipa.fhg.de> - 0.6.4-0
- Autogenerated by Bloom

* Mon Aug 31 2015 Felix Messmer <fxm@ipa.fhg.de> - 0.6.3-0
- Autogenerated by Bloom

* Sat Aug 29 2015 Felix Messmer <fxm@ipa.fhg.de> - 0.6.2-0
- Autogenerated by Bloom

* Wed Jun 17 2015 Felix Messmer <fxm@ipa.fhg.de> - 0.6.1-0
- Autogenerated by Bloom

