%global packname  affyio
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.22.0
Release:          1%{?dist}
Summary:          Tools for parsing Affymetrix data files

Group:            Applications/Engineering 
License:          LGPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 
Requires:         R-zlibbioc 

BuildRequires:    R-devel tex(latex) R-methods
BuildRequires:    R-zlibbioc 


%description
Routines for parsing Affymetrix data files based upon file format
information. Primary focus is on accessing the CEL and CDF file formats.

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
%doc %{rlibdir}/affyio/DESCRIPTION
%doc %{rlibdir}/affyio/html
%{rlibdir}/affyio/LICENSE
%{rlibdir}/affyio/INDEX
%{rlibdir}/affyio/help
%{rlibdir}/affyio/Meta
%{rlibdir}/affyio/libs
%{rlibdir}/affyio/NAMESPACE
%{rlibdir}/affyio/R

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.22.0-1
- initial package for Fedora