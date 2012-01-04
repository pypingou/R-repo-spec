%global packname  intamap
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.3.11
Release:          1%{?dist}
Summary:          procedures for automated interpolation

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.3-11.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-sp R-gstat R-rgdal R-akima R-automap R-mvtnorm R-MASS R-evd R-lattice 

BuildRequires:    R-devel tex(latex) R-sp R-gstat R-rgdal R-akima R-automap R-mvtnorm R-MASS R-evd R-lattice 

%description
A package that provides classes and methods for automated spatial

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.11-1
- initial package for Fedora