#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-mondate
Version  : 0.10.01.02
Release  : 36
URL      : http://cran.r-project.org/src/contrib/mondate_0.10.01.02.tar.gz
Source0  : http://cran.r-project.org/src/contrib/mondate_0.10.01.02.tar.gz
Summary  : Keep track of dates in terms of months
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-zoo
BuildRequires : R-zoo
BuildRequires : clr-R-helpers

%description
Model dates as at close of business.
  Perform date arithmetic in units of "months" and "years" (multiples of months).
  Allow "infinite" dates to model "ultimate" time spans.

%prep
%setup -q -c -n mondate

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1502409845

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1502409845
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mondate
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mondate
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library mondate
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/mondate/DESCRIPTION
/usr/lib64/R/library/mondate/INDEX
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
