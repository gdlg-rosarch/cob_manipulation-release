Name:           ros-indigo-cob-kinematics
Version:        0.6.3
Release:        0%{?dist}
Summary:        ROS cob_kinematics package

Group:          Development/Libraries
License:        LGPL
URL:            http://ros.org/wiki/cob_manipulation/
Source0:        %{name}-%{version}.tar.gz

Requires:       lapack-devel
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-moveit-core
Requires:       ros-indigo-moveit-msgs
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-tf-conversions
Requires:       ros-indigo-urdf
BuildRequires:  lapack-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-moveit-core
BuildRequires:  ros-indigo-moveit-msgs
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-tf-conversions
BuildRequires:  ros-indigo-urdf

%description
IK solvers and utilities for Care-O-bot

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
* Mon Aug 31 2015 Mathias Luedtke <mdl@ipa.fhg.de> - 0.6.3-0
- Autogenerated by Bloom

* Sat Aug 29 2015 Mathias Luedtke <mdl@ipa.fhg.de> - 0.6.2-0
- Autogenerated by Bloom

* Wed Jun 17 2015 Mathias Luedtke <mdl@ipa.fhg.de> - 0.6.1-0
- Autogenerated by Bloom

* Thu Sep 18 2014 Mathias Luedtke <mdl@ipa.fhg.de> - 0.6.0-0
- Autogenerated by Bloom

* Thu Aug 28 2014 Mathias Luedtke <mdl@ipa.fhg.de> - 0.5.2-0
- Autogenerated by Bloom

