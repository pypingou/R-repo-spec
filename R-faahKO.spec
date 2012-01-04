%global packname  faahKO
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.8
Release:          1%{?dist}
Summary:          Saghatelian et al. (2004) FAAH knockout LC/MS data

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-xcms 


BuildRequires:    R-devel tex(latex) R-xcms



%description
Positive ionization mode data in NetCDF file format. Centroided subset
from 200-600 m/z and 2500-4500 seconds. Data originally reported in
"Assignment of Endogenous Substrates to Enzymes by Global Metabolite
Profiling" Biochemistry; 2004; 43(45). Also includes detected peaks in an

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.8-1
- initial package for Fedora