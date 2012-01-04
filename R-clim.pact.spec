%global packname  clim.pact
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.3.10
Release:          1%{?dist}
Summary:          Climate analysis and empirical-statistical downscaling (ESD) package for monthly and daily data.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.3-10.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-ncdf R-akima 


BuildRequires:    R-devel tex(latex) R-ncdf R-akima



%description
The package contains R functions for retrieving data, making climate
analysis and downscaling of monthly mean and daily mean global climate
scenarios. (Windows-users may need to obtain the 'ncdf' package from URL
'http://www.stats.ox.ac.uk/pub/RWin/' to get clim.pact to work). The
package is also described in the book 'Empirical-Statistical Downscaling

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.3.10-1
- initial package for Fedora