%global packname  marelac
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.1
Release:          1%{?dist}
Summary:          Tools for Aquatic Sciences

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-shape R-seacarb 

BuildRequires:    R-devel tex(latex) R-shape R-seacarb 

%description
Datasets, constants, conversion factors, utilities for MArine, Riverine,
Estuarine, LAcustrine and Coastal science. The package contains among
others: (1) chemical and physical constants and datasets, e.g. atomic
weights, gas constants, the earths bathymetry; (2) conversion factors
(e.g. gram to mol to liter, barometric units, temperature, salinity); (3)
physical functions, e.g. to estimate concentrations of conservative
substances, gas transfer and diffusion coefficients, the Coriolis force
and gravity; (4) thermophysical properties of the seawater, as from the
UNESCO polynomial or from the more recent derivation based on a Gibbs

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.1-1
- initial package for Fedora