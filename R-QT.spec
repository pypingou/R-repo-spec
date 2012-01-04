%global packname  QT
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          QT Knowledge Management System

Group:            Applications/Engineering 
License:          LGPL (>= 2.1)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Hmisc R-lattice R-SASxport R-grid 


BuildRequires:    R-devel tex(latex) R-Hmisc R-lattice R-SASxport R-grid



%description
This package performs QT-RR, QTc-time, and concentration-QTc analyses.

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
%doc %{rlibdir}/QT/html
%doc %{rlibdir}/QT/DESCRIPTION
%{rlibdir}/QT/Meta
%{rlibdir}/QT/INDEX
%{rlibdir}/QT/data
%{rlibdir}/QT/extdata
%{rlibdir}/QT/NAMESPACE
%{rlibdir}/QT/R
%{rlibdir}/QT/help

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3-1
- initial package for Fedora