%global packname  prodlim
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.9
Release:          1%{dist}
Summary:          Product Limit Estimation

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-KernSmooth R-survival 

BuildRequires:    R-devel tex(latex) R-stats R-KernSmooth R-survival 

%description
Fast and user friendly nonparametric estimation in censored survival
(event history) analysis.

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
%doc %{rlibdir}/prodlim/DESCRIPTION
%doc %{rlibdir}/prodlim/html
%{rlibdir}/prodlim/help
%{rlibdir}/prodlim/data
%{rlibdir}/prodlim/Meta
%{rlibdir}/prodlim/INDEX
%{rlibdir}/prodlim/R
%{rlibdir}/prodlim/libs
%{rlibdir}/prodlim/NAMESPACE

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.9-1
- Update to version 1.2.9

* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.1-1
- initial package for Fedora