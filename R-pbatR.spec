%global packname  pbatR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.2.3
Release:          1%{?dist}
Summary:          P2BAT

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.2-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-survival R-rootSolve 

BuildRequires:    R-devel tex(latex) R-survival R-rootSolve 

%description
This package provides data analysis via the pbat program, and an
alternative internal implementation of the power calculations via
simulation only.  For analysis, this package provides a frontend to the
PBAT software, automatically reading in the output from the pbat program
and displaying the corresponding figure when appropriate (i.e.
PBAT-logrank). It includes support for multiple processes and clusters.
For analysis, users must download PBAT (developed by Christoph Lange) and
accept it's license, available on the PBAT webpage. Both the data analysis
and power calculations have command line and graphical interfaces using

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
%doc %{rlibdir}/pbatR/html
%doc %{rlibdir}/pbatR/DESCRIPTION
%{rlibdir}/pbatR/NAMESPACE
%{rlibdir}/pbatR/R
%{rlibdir}/pbatR/INDEX
%{rlibdir}/pbatR/help
%{rlibdir}/pbatR/libs
RPM build errors:
%{rlibdir}/pbatR/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.2.3-1
- initial package for Fedora