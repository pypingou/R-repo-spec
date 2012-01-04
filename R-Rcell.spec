%global packname  Rcell
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.6
Release:          1%{?dist}
Summary:          Microscopy Based Citometry Data Analysis Package

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-reshape R-plyr R-ggplot2 R-Hmisc 

BuildRequires:    R-devel tex(latex) R-stats R-reshape R-plyr R-ggplot2 R-Hmisc 

%description
Provides functions to load, filter and visualize microscopy based
citometry data

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.6-1
- initial package for Fedora