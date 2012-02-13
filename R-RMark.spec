%global packname  RMark
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.1.0
Release:          1%{dist}
Summary:          R Code for MARK Analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-plotrix R-snowfall 
Requires:         R-msm R-nlme 

BuildRequires:    R-devel tex(latex) R-plotrix R-snowfall
BuildRequires:    R-msm R-nlme 


%description
This package provides an interface to the software package MARK developed
by Gary White. MARK is freely available at
(http://www.phidot.org/software/mark/download/) but is not open source.

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
%doc %{rlibdir}/RMark/DESCRIPTION
%doc %{rlibdir}/RMark/html
%{rlibdir}/RMark/parameters.txt
%{rlibdir}/RMark/MarkModels.pdf
%{rlibdir}/RMark/models.txt
%{rlibdir}/RMark/extdata
%{rlibdir}/RMark/NAMESPACE
%{rlibdir}/RMark/data
%{rlibdir}/RMark/README.txt
%{rlibdir}/RMark/R
%{rlibdir}/RMark/Meta
%{rlibdir}/RMark/help
%{rlibdir}/RMark/INDEX

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 2.1.0-1
- Update to version 2.1.0

* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.9-1
- initial package for Fedora