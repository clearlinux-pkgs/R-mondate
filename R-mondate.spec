#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v4
# autospec commit: 213bb01
#
Name     : R-mondate
Version  : 1.0
Release  : 83
URL      : https://cran.r-project.org/src/contrib/mondate_1.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/mondate_1.0.tar.gz
Summary  : Keep Track of Dates in Terms of Months
Group    : Development/Tools
License  : MPL-2.0
Requires: R-mondate-license = %{version}-%{release}
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# mondate
mondate is an R package that keeps track of dates in units of elapsed fractional months.
mondate is motivated by Damien Laker's 2008 paper
"Time Calculations for Annualizing Returns: the Need for Standardization"
in *The Journal of Performance Measurement*.

%package license
Summary: license components for the R-mondate package.
Group: Default

%description license
license components for the R-mondate package.


%prep
%setup -q -n mondate
pushd ..
cp -a mondate buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1707322129

%install
export SOURCE_DATE_EPOCH=1707322129
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-mondate
cp %{_builddir}/mondate/LICENSE %{buildroot}/usr/share/package-licenses/R-mondate/81ef2049acec205180dfaa781e2d6257e1901e95 || :
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-va/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/mondate/DESCRIPTION
/usr/lib64/R/library/mondate/INDEX
/usr/lib64/R/library/mondate/LICENSE
/usr/lib64/R/library/mondate/Meta/Rd.rds
/usr/lib64/R/library/mondate/Meta/features.rds
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
/usr/lib64/R/library/mondate/readme.rmd

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-mondate/81ef2049acec205180dfaa781e2d6257e1901e95
