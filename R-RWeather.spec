%global packname  RWeather
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3
Release:          1%{?dist}
Summary:          R wrapper around the Yahoo! Weather, Google Weather and NOAA APIs

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-XML 


BuildRequires:    R-devel tex(latex) R-XML



%description
This package provides programmatic access to Google Weather, Yahoo!
Weather and NOAA APIs

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
%doc %{rlibdir}/RWeather/html
%doc %{rlibdir}/RWeather/DESCRIPTION
%{rlibdir}/RWeather/help
%{rlibdir}/RWeather/Meta
%{rlibdir}/RWeather/R
%{rlibdir}/RWeather/INDEX
%{rlibdir}/RWeather/NAMESPACE

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3-1
- initial package for Fedora