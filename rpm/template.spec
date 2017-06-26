Name:           ros-kinetic-plotjuggler
Version:        1.1.1
Release:        0%{?dist}
Summary:        ROS plotjuggler package

Group:          Development/Libraries
License:        LGPLv3
URL:            https://github.com/facontidavide/PlotJuggler
Source0:        %{name}-%{version}.tar.gz

Requires:       binutils-devel
Requires:       qt5-qtbase-devel
Requires:       qt5-qtsvg-devel
Requires:       ros-kinetic-ros-type-introspection
Requires:       ros-kinetic-rosbag
Requires:       ros-kinetic-rosbag-storage
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-roscpp-serialization
Requires:       ros-kinetic-rostime
Requires:       ros-kinetic-topic-tools
BuildRequires:  binutils-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-ros-type-introspection
BuildRequires:  ros-kinetic-rosbag
BuildRequires:  ros-kinetic-rosbag-storage
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-roscpp-serialization
BuildRequires:  ros-kinetic-rostime
BuildRequires:  ros-kinetic-topic-tools

%description
PlotJuggler: juggle with data

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Mon Jun 26 2017 Davide Faconti <davide.faconti@gmail.com> - 1.1.1-0
- Autogenerated by Bloom

* Tue Jun 20 2017 Davide Faconti <davide.faconti@gmail.com> - 1.1.0-0
- Autogenerated by Bloom

* Tue Jun 20 2017 Davide Faconti <davide.faconti@gmail.com> - 1.0.8-0
- Autogenerated by Bloom

* Fri May 12 2017 Davide Faconti <davide.faconti@gmail.com> - 1.0.7-0
- Autogenerated by Bloom

* Fri May 12 2017 Davide Faconti <davide.faconti@gmail.com> - 1.0.6-0
- Autogenerated by Bloom

* Sun May 07 2017 Davide Faconti <davide.faconti@gmail.com> - 1.0.5-0
- Autogenerated by Bloom

* Sun Apr 30 2017 Davide Faconti <davide.faconti@gmail.com> - 1.0.4-0
- Autogenerated by Bloom

* Fri Apr 28 2017 Davide Faconti <davide.faconti@gmail.com> - 1.0.3-0
- Autogenerated by Bloom

* Wed Apr 26 2017 Davide Faconti <davide.faconti@gmail.com> - 1.0.2-0
- Autogenerated by Bloom

* Mon Apr 24 2017 Davide Faconti <davide.faconti@gmail.com> - 1.0.1-0
- Autogenerated by Bloom

* Sat Apr 22 2017 Davide Faconti <davide.faconti@gmail.com> - 1.0.0-0
- Autogenerated by Bloom

* Fri Apr 21 2017 Davide Faconti <davide.faconti@gmail.com> - 0.18.0-0
- Autogenerated by Bloom

* Sun Apr 02 2017 Davide Faconti <davide.faconti@gmail.com> - 0.17.0-0
- Autogenerated by Bloom

* Wed Mar 22 2017 Davide Faconti <davide.faconti@gmail.com> - 0.15.3-0
- Autogenerated by Bloom

* Wed Mar 22 2017 Davide Faconti <davide.faconti@gmail.com> - 0.15.2-0
- Autogenerated by Bloom

* Mon Mar 20 2017 Davide Faconti <davide.faconti@gmail.com> - 0.15.1-0
- Autogenerated by Bloom

* Sat Mar 18 2017 Davide Faconti <davide.faconti@gmail.com> - 0.15.0-1
- Autogenerated by Bloom

* Fri Mar 17 2017 Davide Faconti <davide.faconti@gmail.com> - 0.15.0-0
- Autogenerated by Bloom

* Fri Mar 17 2017 Davide Faconti <davide.faconti@gmail.com> - 0.14.2-0
- Autogenerated by Bloom

* Wed Mar 15 2017 Davide Faconti <davide.faconti@gmail.com> - 0.14.1-0
- Autogenerated by Bloom

* Sun Mar 12 2017 Davide Faconti <davide.faconti@gmail.com> - 0.13.0-0
- Autogenerated by Bloom

* Mon Mar 06 2017 Davide Faconti <davide.faconti@gmail.com> - 0.12.1-0
- Autogenerated by Bloom

* Tue Feb 14 2017 Davide Faconti <davide.faconti@gmail.com> - 0.10.2-0
- Autogenerated by Bloom

* Tue Feb 14 2017 Davide Faconti <davide.faconti@gmail.com> - 0.10.1-0
- Autogenerated by Bloom

* Sun Feb 12 2017 Davide Faconti <davide.faconti@gmail.com> - 0.10.0-0
- Autogenerated by Bloom

* Thu Feb 09 2017 Davide Faconti <davide.faconti@gmail.com> - 0.9.1-0
- Autogenerated by Bloom

* Tue Feb 07 2017 Davide Faconti <davide.faconti@gmail.com> - 0.9.0-2
- Autogenerated by Bloom

* Tue Feb 07 2017 Davide Faconti <davide.faconti@gmail.com> - 0.9.0-1
- Autogenerated by Bloom

* Tue Feb 07 2017 Davide Faconti <davide.faconti@gmail.com> - 0.9.0-0
- Autogenerated by Bloom

* Tue Jan 24 2017 Davide Faconti <davide.faconti@gmail.com> - 0.8.1-0
- Autogenerated by Bloom

