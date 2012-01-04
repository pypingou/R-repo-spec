%global packname  RTCA
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6.0
Release:          1%{?dist}
Summary:          Open-source toolkit to analyse data from xCELLigence System (RTCA) by Roche

Group:            Applications/Engineering 
License:          LGPL-3
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-stats R-graphics R-Biobase R-RColorBrewer R-gtools 

BuildRequires:    R-devel tex(latex) R-methods R-stats R-graphics R-Biobase R-RColorBrewer R-gtools 

%description
Import, analyze and visualize data from Roche(R) xCELLigence RTCA systems.
The package imports real-time cell electrical impedance data into R. As an
alternative to commercial software shipped along the system, the
Bioconductor package RTCA provides several unique transformation
(normalization) strategies and various visualization tools.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.0-1
- initial package for Fedora