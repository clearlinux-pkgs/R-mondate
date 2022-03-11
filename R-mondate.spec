#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-mondate
Version  : 0.10.02
Release  : 74
URL      : https://cran.r-project.org/src/contrib/mondate_0.10.02.tar.gz
Source0  : https://cran.r-project.org/src/contrib/mondate_0.10.02.tar.gz
Summary  : Keep Track of Dates in Terms of Months
Group    : Development/Tools
License  : MPL-2.0
BuildRequires : buildreq-R

%description
# mondate
mondate is an R package that keeps track of dates in units of elapsed fractional months.
mondate is motivated by Damien Laker's 2008 paper
"Time Calculations for Annualizing Returns: the Need for Standardization"
in *The Journal of Performance Measurement*.

%prep
%setup -q -c -n mondate
cd %{_builddir}/mondate

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641063284

%install
export SOURCE_DATE_EPOCH=1641063284
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mondate
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mondate
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mondate
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc mondate || :


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
