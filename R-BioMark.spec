%global packname  BioMark
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3.3
Release:          1%{?dist}
Summary:          Find biomarkers in two-class discrimination problems

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS R-pls R-st 


BuildRequires:    R-devel tex(latex) R-MASS R-pls R-st



%description
The package implements PCLDA, PLSDA, and several t-tests to find those
variables that allow for adequate discrimination between two classes.
Apart from the usual approaches based on the size of model coefficients, a
set of functions is provided that assess the stability of the potential
biomarkers under crossvalidation.

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.3-1
- initial package for Fedora