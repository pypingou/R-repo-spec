%global packname  rconifers
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.5
Release:          1%{?dist}
Summary:          R interface to the CONIFERS forest growth model

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-utils 

BuildRequires:    R-devel tex(latex) R-utils 

%description
This package contains functions for simulating future forest conditions
using the CONIFERS growth model.

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
%doc %{rlibdir}/rconifers/DESCRIPTION
%doc %{rlibdir}/rconifers/CITATION
%doc %{rlibdir}/rconifers/html
%{rlibdir}/rconifers/help
%{rlibdir}/rconifers/INDEX
%{rlibdir}/rconifers/Meta
%{rlibdir}/rconifers/data
%{rlibdir}/rconifers/R
%{rlibdir}/rconifers/libs
%{rlibdir}/rconifers/NAMESPACE
RPM build errors:

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.5-1
- initial package for Fedora