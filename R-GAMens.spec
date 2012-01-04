%global packname  GAMens
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Applies GAMbag, GAMrsm and GAMens ensemble classifiers for binary classification

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-splines R-akima R-gam 

BuildRequires:    R-devel tex(latex) R-splines R-akima R-gam 

%description
This package implements the GAMbag, GAMrsm and GAMens ensemble classifiers
for binary classification (De Bock et al., 2010). The ensembles implement
Bagging (Breiman, 1996), the Random Subspace Method (Ho, 1998), or both,
and use Hastie and Tibshirani's (1990) generalized additive models (GAMs)
as base classifiers. Once an ensemble classifier has been trained, it can
be used for predictions on new data. A function for cross validation is
also included.

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
%doc %{rlibdir}/GAMens/html
%doc %{rlibdir}/GAMens/CITATION
%doc %{rlibdir}/GAMens/DESCRIPTION
%{rlibdir}/GAMens/INDEX
%{rlibdir}/GAMens/Meta
%{rlibdir}/GAMens/help
%{rlibdir}/GAMens/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.1-1
- initial package for Fedora