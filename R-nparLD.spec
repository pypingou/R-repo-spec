%global packname  nparLD
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          Nonparametric Analysis of Longitudinal Data in Factorial Experiments

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS 

BuildRequires:    R-devel tex(latex) R-MASS 

%description
The package "nparLD" is designed to perform nonparametric analysis of
longitudinal data in factorial experiments. Longitudinal data are those
which are collected from the same subjects over time, and they frequently
arise in biological sciences. Nonparametric methods do not require
assumptions on distributions of parameters, and are applicable to a
variety of data types (continuous, discrete, purely ordinal, and
dichotomous). Such methods are also robust with respect to outliers and
for small sample sizes.

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
%doc %{rlibdir}/nparLD/html
%doc %{rlibdir}/nparLD/DESCRIPTION
%{rlibdir}/nparLD/help
%{rlibdir}/nparLD/INDEX
%{rlibdir}/nparLD/NAMESPACE
%{rlibdir}/nparLD/Meta
%{rlibdir}/nparLD/data
%{rlibdir}/nparLD/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3-1
- initial package for Fedora