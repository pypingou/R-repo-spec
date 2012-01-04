%global packname  FRB
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.7
Release:          1%{?dist}
Summary:          Fast and Robust Bootstrap

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-corpcor R-rrcov 

BuildRequires:    R-devel tex(latex) R-corpcor R-rrcov 

%description
This package performs robust inference based on applying Fast and Robust
Bootstrap on robust estimators. Available methods are multivariate
regression, PCA and Hotelling tests.

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
%doc %{rlibdir}/FRB/html
%doc %{rlibdir}/FRB/DESCRIPTION
%{rlibdir}/FRB/help
%{rlibdir}/FRB/INDEX
%{rlibdir}/FRB/Meta
%{rlibdir}/FRB/data
%{rlibdir}/FRB/R
%{rlibdir}/FRB/NAMESPACE

%changelog
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.7-1
- initial package for Fedora