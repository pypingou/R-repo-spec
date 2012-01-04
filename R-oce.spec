%global packname  oce
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.8.2
Release:          1%{?dist}
Summary:          Analysis of Oceanographic data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.8-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-utils R-methods 

BuildRequires:    R-devel tex(latex) R-utils R-methods 

%description
Supports the analysis of Oceanographic data, including ADP measurements,
CTD measurements, sectional data, sea-level time series, coastline files,
etc. Provides functions for calculating seawater properties such as
potential temperature and density, as well as derived properties such as
buoyancy frequency and dynamic height.

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
%doc %{rlibdir}/oce/DESCRIPTION
%doc %{rlibdir}/oce/doc
%doc %{rlibdir}/oce/html
%doc %{rlibdir}/oce/NEWS
%{rlibdir}/oce/help
%{rlibdir}/oce/R
%{rlibdir}/oce/data
%{rlibdir}/oce/INDEX
%{rlibdir}/oce/NAMESPACE
%{rlibdir}/oce/demo
%{rlibdir}/oce/extdata
%{rlibdir}/oce/libs
RPM build errors:
%{rlibdir}/oce/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.2-1
- initial package for Fedora