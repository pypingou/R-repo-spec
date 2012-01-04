%global packname  modelfree
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Model-free estimation of a psychometric function

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-PolynomF R-SparseM R-stats R-utils R-base 

BuildRequires:    R-devel tex(latex) R-PolynomF R-SparseM R-stats R-utils R-base 

%description
Local linear estimation of psychometric functions. Provides functions for
nonparametric estimation of a psychometric function and for estimation of
a derived threshold and slope, and their standard deviations and
confidence intervals

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
%doc %{rlibdir}/modelfree/html
%doc %{rlibdir}/modelfree/DESCRIPTION
%{rlibdir}/modelfree/R
%{rlibdir}/modelfree/help
%{rlibdir}/modelfree/NAMESPACE
%{rlibdir}/modelfree/INDEX
%{rlibdir}/modelfree/Meta
%{rlibdir}/modelfree/data

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora