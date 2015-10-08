Name:           ros-indigo-perception-oru
Version:        1.0.29
Release:        0%{?dist}
Summary:        ROS perception_oru package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/perception_oru
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-ndt-feature-reg
Requires:       ros-indigo-ndt-fuser
Requires:       ros-indigo-ndt-map
Requires:       ros-indigo-ndt-map-builder
Requires:       ros-indigo-ndt-mcl
Requires:       ros-indigo-ndt-registration
Requires:       ros-indigo-ndt-rviz-visualisation
Requires:       ros-indigo-ndt-visualisation
Requires:       ros-indigo-sdf-tracker
BuildRequires:  ros-indigo-catkin

%description
Perception packages from the MRO lab at AASS, Orebro University

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
* Thu Oct 08 2015 Jari Saarinen <jari.p.saarinen@gmail.com> - 1.0.29-0
- Autogenerated by Bloom

