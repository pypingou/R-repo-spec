%global packname  M3
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          Reading M3 files

Group:            Applications/Engineering 
License:          Unlimited
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-ncdf4 R-rgdal R-maps 


BuildRequires:    R-devel tex(latex) R-ncdf4 R-rgdal R-maps



%description
This package contains functions to read in and manipulate air quality
model output from Models3-formatted files.  This format is used by the
Community Multiscale Air Quaility (CMAQ) model.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1-1
- initial package for Fedora