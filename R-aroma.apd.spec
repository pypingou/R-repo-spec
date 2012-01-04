%global packname  aroma.apd
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          A probe-level data file format used by aroma.affymetrix [DEPRECATED]

Group:            Applications/Engineering 
License:          LGPL (>= 2.1)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-R.methodsS3 R-R.utils R-R.huge 

BuildRequires:    R-devel tex(latex) R-R.methodsS3 R-R.utils R-R.huge 

%description
THIS PACKAGE HAS BEEN DEPRECATED. (The (in-house) APD file format was
initially developed to store Affymetrix probe-level data, e.g. normalized
CEL intensites.  Chip types can be added to APD file and similar to
methods in the affxparser package, this package provides methods to read
APDs organized by units (probesets).  In addition, the probe elements can
be arranged optimally such that the elements are guaranteed to be read in
order when, for instance, data is read unit by unit.  This speed up the
read substantially.  This package is supporting the aroma.affymetrix
package and not intended to be used elsewhere.)

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
%doc %{rlibdir}/aroma.apd/DESCRIPTION
%doc %{rlibdir}/aroma.apd/html
%doc %{rlibdir}/aroma.apd/NEWS
%{rlibdir}/aroma.apd/help
%{rlibdir}/aroma.apd/NAMESPACE
%{rlibdir}/aroma.apd/R
%{rlibdir}/aroma.apd/INDEX
%{rlibdir}/aroma.apd/Meta

%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.0-1
- initial package for Fedora