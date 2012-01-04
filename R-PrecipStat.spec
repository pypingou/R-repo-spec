%global packname  PrecipStat
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.00
Release:          1%{?dist}
Summary:          Precipitation Statistics

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The package contains data for the qqplotter package. These data contain 14
percentiles p in [0.50, 0.55, ... 0.95] and [0.96,0.97, ... 0.99] for the
24hr precipitation for all days with amounts greater than 1mm/day.

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
%doc %{rlibdir}/PrecipStat/html
%doc %{rlibdir}/PrecipStat/DESCRIPTION
%{rlibdir}/PrecipStat/data
%{rlibdir}/PrecipStat/NAMESPACE
%{rlibdir}/PrecipStat/Meta
%{rlibdir}/PrecipStat/R
%{rlibdir}/PrecipStat/INDEX
%{rlibdir}/PrecipStat/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.00-1
- initial package for Fedora