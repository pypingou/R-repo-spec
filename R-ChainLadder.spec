%global packname  ChainLadder
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.5.1
Release:          1%{?dist}
Summary:          Mack, Bootstrap, Munich, Multivariate-chain-ladder, Clark methods and generalized linear models for insurance claims reserving

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1.5-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Hmisc R-lattice R-Matrix R-methods R-stats R-systemfit R-MASS R-RUnit R-actuar R-statmod R-utils 

BuildRequires:    R-devel tex(latex) R-Hmisc R-lattice R-Matrix R-methods R-stats R-systemfit R-MASS R-RUnit R-actuar R-statmod R-utils 

%description
The package provides Mack-, Munich-, Bootstrap, and
Multivariate-chain-ladder methods, as well as the LDF Curve Fitting
methods of Dave Clark and GLM-based reserving models. These methods are
typically used in insurance claims reserving.

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
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.5.1-1
- initial package for Fedora