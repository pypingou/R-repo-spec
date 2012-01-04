%global packname  elasticnet
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.5
Release:          1%{?dist}
Summary:          Elastic-Net for Sparse Estimation and Sparse PCA

Group:            Applications/Engineering 
License:          GPL (>=2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lars 

BuildRequires:    R-devel tex(latex) R-lars 

%description
This package provides functions for fitting the entire solution path of
the Elastic-Net and also provides functions for estimating sparse
Principal Components. The Lasso solution paths can be computed by the same
function. First version: 2005-10.

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
%doc %{rlibdir}/elasticnet/html
%doc %{rlibdir}/elasticnet/DESCRIPTION
%{rlibdir}/elasticnet/Meta
%{rlibdir}/elasticnet/INDEX
%{rlibdir}/elasticnet/help
%{rlibdir}/elasticnet/data
%{rlibdir}/elasticnet/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.5-1
- initial package for Fedora