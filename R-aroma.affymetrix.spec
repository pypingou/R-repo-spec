%global packname  aroma.affymetrix
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.3.0
Release:          1%{?dist}
Summary:          Analysis of large Affymetrix microarray data sets

Group:            Applications/Engineering 
License:          LGPL (>= 2.1)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-R.utils R-R.filesets R-aroma.core R-aroma.light R-aroma.apd R-R.rsp R-affxparser 

BuildRequires:    R-devel tex(latex) R-R.utils R-R.filesets R-aroma.core R-aroma.light R-aroma.apd R-R.rsp R-affxparser 

%description
This package implements classes for files and sets of files for various
Affymetrix file formats, e.g. AffymetrixCdfFile, AffymetrixCelFile, and
AffymetrixCelSet.  These are designed to be memory efficient but still
being fast.  The idea is to keep all data on file and only read data into
memory when needed.  Clever caching mechanisms are used to minimize the
overhead of data IO.  All of the above is hidden in the package API and
for the developer (and the end user), the data is queried as if it lives
in memory.  With this design it is only the diskspace that limits the
number of arrays that can be analyzed.  To install, do:
source("http://www.aroma-project.org/hbLite.R");

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.3.0-1
- initial package for Fedora