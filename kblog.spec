#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kblog
Version  : 19.08.3
Release  : 14
URL      : https://download.kde.org/stable/applications/19.08.3/src/kblog-19.08.3.tar.xz
Source0  : https://download.kde.org/stable/applications/19.08.3/src/kblog-19.08.3.tar.xz
Source1 : https://download.kde.org/stable/applications/19.08.3/src/kblog-19.08.3.tar.xz.sig
Summary  : A blogging library for KDE
Group    : Development/Tools
License  : LGPL-2.1
Requires: kblog-data = %{version}-%{release}
Requires: kblog-lib = %{version}-%{release}
Requires: kblog-license = %{version}-%{release}
Requires: kblog-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kcalcore-dev
BuildRequires : kxmlrpcclient-dev
BuildRequires : syndication-dev

%description
# KBlog #
KBlog provides client-side support for web application remote blogging APIs.

%package data
Summary: data components for the kblog package.
Group: Data

%description data
data components for the kblog package.


%package dev
Summary: dev components for the kblog package.
Group: Development
Requires: kblog-lib = %{version}-%{release}
Requires: kblog-data = %{version}-%{release}
Provides: kblog-devel = %{version}-%{release}
Requires: kblog = %{version}-%{release}
Requires: kblog = %{version}-%{release}

%description dev
dev components for the kblog package.


%package lib
Summary: lib components for the kblog package.
Group: Libraries
Requires: kblog-data = %{version}-%{release}
Requires: kblog-license = %{version}-%{release}

%description lib
lib components for the kblog package.


%package license
Summary: license components for the kblog package.
Group: Default

%description license
license components for the kblog package.


%package locales
Summary: locales components for the kblog package.
Group: Default

%description locales
locales components for the kblog package.


%prep
%setup -q -n kblog-19.08.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1573524911
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1573524911
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kblog
cp %{_builddir}/kblog-19.08.3/COPYING.LIB %{buildroot}/usr/share/package-licenses/kblog/9a1929f4700d2407c70b507b3b2aaf6226a9543c
pushd clr-build
%make_install
popd
%find_lang libkblog5

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/kblog.categories
/usr/share/qlogging-categories5/kblog.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KBlog/KBlog/Blog
/usr/include/KF5/KBlog/KBlog/BlogComment
/usr/include/KF5/KBlog/KBlog/BlogMedia
/usr/include/KF5/KBlog/KBlog/BlogPost
/usr/include/KF5/KBlog/KBlog/Blogger1
/usr/include/KF5/KBlog/KBlog/GData
/usr/include/KF5/KBlog/KBlog/MetaWeblog
/usr/include/KF5/KBlog/KBlog/MovableType
/usr/include/KF5/KBlog/KBlog/WordpressBuggy
/usr/include/KF5/KBlog/kblog/Blog
/usr/include/KF5/KBlog/kblog/BlogComment
/usr/include/KF5/KBlog/kblog/BlogMedia
/usr/include/KF5/KBlog/kblog/BlogPost
/usr/include/KF5/KBlog/kblog/Blogger1
/usr/include/KF5/KBlog/kblog/GData
/usr/include/KF5/KBlog/kblog/MetaWeblog
/usr/include/KF5/KBlog/kblog/MovableType
/usr/include/KF5/KBlog/kblog/WordpressBuggy
/usr/include/KF5/KBlog/kblog/blog.h
/usr/include/KF5/KBlog/kblog/blogcomment.h
/usr/include/KF5/KBlog/kblog/blogger1.h
/usr/include/KF5/KBlog/kblog/blogmedia.h
/usr/include/KF5/KBlog/kblog/blogpost.h
/usr/include/KF5/KBlog/kblog/gdata.h
/usr/include/KF5/KBlog/kblog/kblog_export.h
/usr/include/KF5/KBlog/kblog/metaweblog.h
/usr/include/KF5/KBlog/kblog/movabletype.h
/usr/include/KF5/KBlog/kblog/wordpressbuggy.h
/usr/include/KF5/kblog_version.h
/usr/lib64/cmake/KF5Blog/KF5BlogConfig.cmake
/usr/lib64/cmake/KF5Blog/KF5BlogConfigVersion.cmake
/usr/lib64/cmake/KF5Blog/KF5BlogTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Blog/KF5BlogTargets.cmake
/usr/lib64/libKF5Blog.so
/usr/lib64/qt5/mkspecs/modules/qt_KBlog.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Blog.so.5
/usr/lib64/libKF5Blog.so.5.12.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kblog/9a1929f4700d2407c70b507b3b2aaf6226a9543c

%files locales -f libkblog5.lang
%defattr(-,root,root,-)

