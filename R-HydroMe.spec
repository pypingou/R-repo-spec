%global packname  HydroMe
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Estimation of Soil Hydraulic Parameters from Experimental Data

Group:            Applications/Engineering 
License:          GPL version 2 or newer
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-nlme 

BuildRequires:    R-devel tex(latex) R-nlme 

%description
This package estimates the parameters in infiltration and water retention
models by curve-fitting method. The models considered are those that are
commonly used in soil science.

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
%doc %{rlibdir}/HydroMe/DESCRIPTION
%doc %{rlibdir}/HydroMe/html
%{rlibdir}/HydroMe/INDEX
%{rlibdir}/HydroMe/R
%{rlibdir}/HydroMe/data
%{rlibdir}/HydroMe/NAMESPACE
%{rlibdir}/HydroMe/Meta
%{rlibdir}/HydroMe/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora