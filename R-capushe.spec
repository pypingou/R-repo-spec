%global packname  capushe
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.8
Release:          1%{?dist}
Summary:          Capushe, data-driven slope estimation and dimension jump

Group:            Applications/Engineering 
License:          GPL (>= 2.0)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-graphics R-MASS 

BuildRequires:    R-devel tex(latex) R-methods R-graphics R-MASS 

%description
This package is devoted to the calibration of penalized criteria for model
selection. The calibration methods available in this package are based on
the slope heuristics.

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
%doc %{rlibdir}/capushe/html
%doc %{rlibdir}/capushe/DESCRIPTION
%{rlibdir}/capushe/help
%{rlibdir}/capushe/Meta
%{rlibdir}/capushe/R
%{rlibdir}/capushe/data
%{rlibdir}/capushe/INDEX
%{rlibdir}/capushe/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8-1
- initial package for Fedora