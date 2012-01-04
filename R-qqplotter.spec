%global packname  qqplotter
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.11
Release:          1%{?dist}
Summary:          Quantile-quantile analysis of 24-hr precipitation using a frame work based on the exponential distribution

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-ncdf R-fields R-clim.pact R-akima R-LatticeKrig R-PrecipStat 


BuildRequires:    R-devel tex(latex) R-ncdf R-fields R-clim.pact R-akima R-LatticeKrig R-PrecipStat



%description
The package provides a quick analysis of quantiles of wet-day 24-hr
accumulated precipitation records, demonstrating that the quantiles to a
great degree can be predicted from the wet-day mean. The package analyses
both observations and results from RCMs.

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.11-1
- initial package for Fedora