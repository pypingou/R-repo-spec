%global packname  RunuranGUI
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          A GUI for the UNU.RAN random variate generators

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-Runuran R-rvgtest R-gWidgets R-gWidgetsRGtk2 R-cairoDevice 


BuildRequires:    R-devel tex(latex) R-methods R-Runuran R-rvgtest R-gWidgets R-gWidgetsRGtk2 R-cairoDevice



%description
This package provides a GUI (Graphical User Interface) for the UNU.RAN
random variate generators. Thus it allows to build non-uniform random
number generators interactively for quite arbitrary distributions. In
addition, R code for the required calls from package Runuran can be
displayed and stored for later use. Some basic analysis like
goodness-of-fit tests can be performed.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1-1
- initial package for Fedora