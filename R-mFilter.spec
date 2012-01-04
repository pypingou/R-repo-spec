%global packname  mFilter
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Miscellaneous time series filters

Group:            Applications/Engineering 
License:          GPL version 2 or newer
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
The package implements several time series filters useful for smoothing
and extracting trend and cyclical components of a time series. The
routines are commonly used in economics and finance, however they should
also be interest to other areas. Currently, Christiano-Fitzgerald,
Baxter-King, Hodrick-Prescott, Butterworth, and trigonometric regression
filters are included in the package.

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
%doc %{rlibdir}/mFilter/DESCRIPTION
%doc %{rlibdir}/mFilter/html
%{rlibdir}/mFilter/Meta
%{rlibdir}/mFilter/INDEX
%{rlibdir}/mFilter/NAMESPACE
%{rlibdir}/mFilter/help
%{rlibdir}/mFilter/data
%{rlibdir}/mFilter/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.3-1
- initial package for Fedora