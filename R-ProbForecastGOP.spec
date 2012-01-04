%global packname  ProbForecastGOP
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3.2
Release:          1%{?dist}
Summary:          Probabilistic weather forecast using the GOP method

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-RandomFields R-fields 

BuildRequires:    R-devel tex(latex) R-RandomFields R-fields 

%description
The ProbForecastGOP package contains a main function, called
ProbForecastGOP and other functions, to produce probabilistic weather
forecasts of weather fields using the Geostatistical Output Perturbation
(GOP) method of Gel, Raftery, and Gneiting (JASA, 2004).

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.2-1
- initial package for Fedora