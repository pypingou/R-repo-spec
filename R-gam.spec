%global packname  gam
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.04.1
Release:          1%{?dist}
Summary:          Generalized Additive Models

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-splines 

BuildRequires:    R-devel tex(latex) R-stats R-splines 

%description
Functions for fitting and working with generalized additive models, as
described in chapter 7 of "Statistical Models in S" (Chambers and Hastie
(eds), 1991), and "Generalized Additive Models" (Hastie and Tibshirani,

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
%doc %{rlibdir}/gam/DESCRIPTION
%doc %{rlibdir}/gam/html
%{rlibdir}/gam/libs
%{rlibdir}/gam/data
%{rlibdir}/gam/Meta
%{rlibdir}/gam/NAMESPACE
%{rlibdir}/gam/INDEX
%{rlibdir}/gam/R
%{rlibdir}/gam/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.04.1-1
- initial package for Fedora