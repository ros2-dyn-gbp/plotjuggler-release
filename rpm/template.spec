%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-plotjuggler
Version:        3.0.5
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS plotjuggler package

License:        LGPLv3
URL:            https://github.com/facontidavide/PlotJuggler
Source0:        %{name}-%{version}.tar.gz

Requires:       binutils-devel
Requires:       boost-devel
Requires:       boost-python3-devel
Requires:       cppzmq-devel
Requires:       qt5-qtbase-devel
Requires:       qt5-qtsvg-devel
Requires:       qt5-qtwebsockets
Requires:       qt5-qtx11extras-devel
Requires:       ros-noetic-roslib
BuildRequires:  binutils-devel
BuildRequires:  boost-devel
BuildRequires:  boost-python3-devel
BuildRequires:  cppzmq-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtwebsockets
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-roslib
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
PlotJuggler: juggle with data

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Thu Dec 10 2020 Davide Faconti <davide.faconti@gmail.com> - 3.0.5-1
- Autogenerated by Bloom

* Fri Dec 04 2020 Davide Faconti <davide.faconti@gmail.com> - 3.0.4-1
- Autogenerated by Bloom

* Sun Nov 29 2020 Davide Faconti <davide.faconti@gmail.com> - 3.0.3-1
- Autogenerated by Bloom

* Sat Nov 28 2020 Davide Faconti <davide.faconti@gmail.com> - 3.0.2-1
- Autogenerated by Bloom

* Fri Aug 14 2020 Davide Faconti <davide.faconti@gmail.com> - 2.8.4-1
- Autogenerated by Bloom

* Sat Jul 11 2020 Davide Faconti <davide.faconti@gmail.com> - 2.8.3-1
- Autogenerated by Bloom

* Tue Jul 07 2020 Davide Faconti <davide.faconti@gmail.com> - 2.8.2-1
- Autogenerated by Bloom
