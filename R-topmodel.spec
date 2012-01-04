%global packname  topmodel
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.7.2.2
Release:          1%{?dist}
Summary:          Implementation of the hydrological model TOPMODEL in R

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.7.2-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Set of hydrological functions including an R implementation of the
hydrological model TOPMODEL, which is based on the 1995 FORTRAN version by
Keith Beven. From version 0.7.0, the package is put into maintenance mode.
New functions for hydrological analysis are now developed as part of the
RHydro package. RHydro can be found on R-forge and is built on a set of
dedicated S4 classes.

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
%doc %{rlibdir}/topmodel/DESCRIPTION
%doc %{rlibdir}/topmodel/html
%{rlibdir}/topmodel/INDEX
%{rlibdir}/topmodel/R
%{rlibdir}/topmodel/NAMESPACE
%{rlibdir}/topmodel/data
%{rlibdir}/topmodel/Meta
%{rlibdir}/topmodel/help
%{rlibdir}/topmodel/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7.2.2-1
- initial package for Fedora