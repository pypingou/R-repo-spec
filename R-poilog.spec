%global packname  poilog
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.4
Release:          1%{?dist}
Summary:          Poisson lognormal and bivariate Poisson lognormal distribution

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Functions for obtaining the density, random deviates and maximum
likelihood estimates of the Poisson lognormal distribution and the
bivariate Poisson lognormal distribution.

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
%doc %{rlibdir}/poilog/DESCRIPTION
%doc %{rlibdir}/poilog/doc
%doc %{rlibdir}/poilog/html
%{rlibdir}/poilog/R
%{rlibdir}/poilog/INDEX
%{rlibdir}/poilog/help
%{rlibdir}/poilog/libs
%{rlibdir}/poilog/NAMESPACE
%{rlibdir}/poilog/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4-1
- initial package for Fedora