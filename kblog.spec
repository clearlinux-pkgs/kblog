#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kblog
Version  : 18.08.0
Release  : 2
URL      : https://download.kde.org/stable/applications/18.08.0/src/kblog-18.08.0.tar.xz
Source0  : https://download.kde.org/stable/applications/18.08.0/src/kblog-18.08.0.tar.xz
Source99 : https://download.kde.org/stable/applications/18.08.0/src/kblog-18.08.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: kblog-lib
Requires: kblog-license
Requires: kblog-locales
Requires: kblog-data
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
Requires: kblog-lib
Requires: kblog-data
Provides: kblog-devel

%description dev
dev components for the kblog package.


%package lib
Summary: lib components for the kblog package.
Group: Libraries
Requires: kblog-data
Requires: kblog-license

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
%setup -q -n kblog-18.08.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1535426308
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1535426308
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/kblog
cp COPYING.LIB %{buildroot}/usr/share/doc/kblog/COPYING.LIB
pushd clr-build
%make_install
popd
%find_lang libkblog5

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/xdg/kblog.categories
/usr/share/xdg/kblog.renamecategories

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
/usr/lib64/libKF5Blog.so.5.9.0

%files license
%defattr(-,root,root,-)
/usr/share/doc/kblog/COPYING.LIB

%files locales -f libkblog5.lang
%defattr(-,root,root,-)

