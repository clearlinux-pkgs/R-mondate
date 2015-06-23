#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-mondate
Version  : 0.10.01.02
Release  : 3
URL      : http://cran.r-project.org/src/contrib/mondate_0.10.01.02.tar.gz
Source0  : http://cran.r-project.org/src/contrib/mondate_0.10.01.02.tar.gz
Summary  : Keep track of dates in terms of months
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : clr-R-helpers

%description
No detailed description available

%prep
%setup -q -c -n mondate

%build

%install
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -ffunction-sections -fno-semantic-interposition -freorder-functions "
export CXXFLAGS="$CXXFLAGS -O3 -flto -ffunction-sections -fno-semantic-interposition -freorder-functions "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library mondate
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library mondate


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/mondate/DESCRIPTION
/usr/lib64/R/library/mondate/INDEX
/usr/lib64/R/library/mondate/Meta/Rd.rds
/usr/lib64/R/library/mondate/Meta/hsearch.rds
/usr/lib64/R/library/mondate/Meta/links.rds
/usr/lib64/R/library/mondate/Meta/nsInfo.rds
/usr/lib64/R/library/mondate/Meta/package.rds
/usr/lib64/R/library/mondate/NAMESPACE
/usr/lib64/R/library/mondate/NEWS
/usr/lib64/R/library/mondate/R/mondate
/usr/lib64/R/library/mondate/R/mondate.rdb
/usr/lib64/R/library/mondate/R/mondate.rdx
/usr/lib64/R/library/mondate/help/AnIndex
/usr/lib64/R/library/mondate/help/aliases.rds
/usr/lib64/R/library/mondate/help/mondate.rdb
/usr/lib64/R/library/mondate/help/mondate.rdx
/usr/lib64/R/library/mondate/help/paths.rds
/usr/lib64/R/library/mondate/html/00Index.html
/usr/lib64/R/library/mondate/html/R.css
