%global packname  hbmem
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          Hierarchical Bayesian Analysis of Recognition Memory

Group:            Applications/Engineering 
License:          LGPL (>= 2.0)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
Contains functions for fitting hierarchical versions of EVSD, UVSD, DPSD,
and our gamma signal detection model to recognition memory
confidence-ratings data.

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
%doc %{rlibdir}/hbmem/html
%doc %{rlibdir}/hbmem/DESCRIPTION
%{rlibdir}/hbmem/NAMESPACE
%{rlibdir}/hbmem/INDEX
%{rlibdir}/hbmem/help
%{rlibdir}/hbmem/Meta
%{rlibdir}/hbmem/data
%{rlibdir}/hbmem/R
%{rlibdir}/hbmem/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2-1
- initial package for Fedora