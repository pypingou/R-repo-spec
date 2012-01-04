%global packname  ppls
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.05
Release:          1%{?dist}
Summary:          Penalized Partial Least Squares

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-splines R-MASS 

BuildRequires:    R-devel tex(latex) R-splines R-MASS 

%description
This package contains linear and nonlinear regression methods based on
Partial Least Squares and Penalization Techniques. Model parameters are
selected via cross-validation, and confidence intervals ans tests for the
regression coefficients can be conducted via jackknifing.

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
%doc %{rlibdir}/ppls/html
%doc %{rlibdir}/ppls/DESCRIPTION
%{rlibdir}/ppls/help
%{rlibdir}/ppls/INDEX
%{rlibdir}/ppls/Meta
%{rlibdir}/ppls/NAMESPACE
%{rlibdir}/ppls/R
%{rlibdir}/ppls/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.05-1
- initial package for Fedora