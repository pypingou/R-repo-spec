%global packname  RNetCDF
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.5.2.2
Release:          1%{?dist}
Summary:          R Interface to NetCDF Datasets

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.5.2-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package provides an interface to Unidata's NetCDF library functions
(version 3) and furthermore access to Unidata's UDUNITS calendar
conversions. The routines and the documentation follow the NetCDF and
UDUNITS C interface, so the corresponding manuals can be consulted for
more detailed information.

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5.2.2-1
- initial package for Fedora