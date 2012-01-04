%global packname  EcoHydRology
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3.8
Release:          1%{?dist}
Summary:          A community modeling foundation for Eco-Hydrology.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-operators R-topmodel R-DEoptim 

BuildRequires:    R-devel tex(latex) R-operators R-topmodel R-DEoptim 

%description
This package provides a flexible foundation for scientists, engineers, and
policy makers to base teaching exercises as well as for more applied use
to model complex eco-hydrological interactions.

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.8-1
- initial package for Fedora