%global packname  CHNOSZ
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.7
Release:          1%{?dist}
Summary:          Chemical Thermodynamics and Activity Diagrams

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-utils 

BuildRequires:    R-devel tex(latex) R-utils 

%description
This package includes functions and data sets to support chemical
thermodynamic modeling in biochemistry and low-temperature geochemistry.
The features include calculation of the standard molal thermodynamic
properties and chemical affinities of reactions involving minerals and/or
biomolecules; a database of thermodynamic properties of aqueous,
crystalline and gaseous species; amino acid group additivity for the
standard molal thermodynamic properties of neutral and ionized proteins;
use of the revised Helgeson-Kirkham-Flowers equations of state for aqueous
species; construction of equilibrium activity diagrams as a function of
temperature, pressure, and chemical activities or fugacities of basis

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.7-1
- initial package for Fedora