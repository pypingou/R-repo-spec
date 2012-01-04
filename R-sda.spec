%global packname  sda
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          Shrinkage Discriminant Analysis and CAT Score Variable Selection

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lattice R-entropy R-corpcor R-fdrtool 

BuildRequires:    R-devel tex(latex) R-lattice R-entropy R-corpcor R-fdrtool 

%description
This package provides an efficient framework for high-dimensional linear
and diagonal discriminant analysis with variable selection. The classifier
is trained using James-Stein-type shrinkage estimators and predictor
variables are ranked using CAT scores (correlation-adjusted t-scores).
Variable selection error is controlled using false non-discovery rates or
higher criticism scores.

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
%doc %{rlibdir}/sda/NEWS
%doc %{rlibdir}/sda/html
%doc %{rlibdir}/sda/DESCRIPTION
%{rlibdir}/sda/R
%{rlibdir}/sda/data
%{rlibdir}/sda/INDEX
%{rlibdir}/sda/LICENSE
%{rlibdir}/sda/Meta
%{rlibdir}/sda/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.0-1
- initial package for Fedora