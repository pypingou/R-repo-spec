%global packname  MortalitySmooth
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.0
Release:          1%{?dist}
Summary:          Smoothing and forecasting Poisson counts with P-splines

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-svcm 

BuildRequires:    R-devel tex(latex) R-svcm 

%description
Smoothing one- and two-dimensional Poisson counts with P-splines
specifically tailored to mortality data. Extra-Poisson variation can be
accounted as well as forecasting. Collection of mortality data and a
specific function for selecting those data by country, sex, age and years.

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
%doc %{rlibdir}/MortalitySmooth/html
%doc %{rlibdir}/MortalitySmooth/DESCRIPTION
%{rlibdir}/MortalitySmooth/Meta
%{rlibdir}/MortalitySmooth/INDEX
%{rlibdir}/MortalitySmooth/R
%{rlibdir}/MortalitySmooth/help
%{rlibdir}/MortalitySmooth/data

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0-1
- initial package for Fedora