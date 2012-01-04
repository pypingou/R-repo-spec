%global packname  polspline
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.5
Release:          1%{?dist}
Summary:          Polynomial spline routines

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Routines for the polynomial spline fitting routines hazard regression,
hazard estimation with flexible tails, logspline, lspec, polyclass, and
polymars, by C. Kooperberg and co-authors

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
%doc %{rlibdir}/polspline/html
%doc %{rlibdir}/polspline/DESCRIPTION
%{rlibdir}/polspline/NAMESPACE
%{rlibdir}/polspline/R
%{rlibdir}/polspline/libs
%{rlibdir}/polspline/INDEX
%{rlibdir}/polspline/Meta
%{rlibdir}/polspline/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.5-1
- initial package for Fedora