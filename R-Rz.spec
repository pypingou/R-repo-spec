%global packname  Rz
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.1
Release:          1%{?dist}
Summary:          GUI Tool for Data Management like SPSS or Stata

Group:            Applications/Engineering 
License:          BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-memisc R-methods 
Requires:         R-RGtk2 

BuildRequires:    R-devel tex(latex) R-memisc R-methods
BuildRequires:    R-RGtk2 


%description
R is very powerfull but not enough for social science becouse of lack in
some functionality for managing survey data SPSS or Stata provides. Memisc
package supplements those, variable labels, value labels, definable
missing values and so on, but to efficiently work these functions need
graphical interface to overlook data. This package provides such graphical
interface similar to SPSS's Variable View and data managing system using
memisc package as backend.

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.1-1
- initial package for Fedora