%global packname  affyPLM
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.30.0
Release:          1%{?dist}
Summary:          Methods for fitting probe-level models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-affy R-Biobase R-gcrma R-stats R-preprocessCore 
Requires:         R-zlibbioc R-methods 

BuildRequires:    R-devel tex(latex) R-affy R-Biobase R-gcrma R-stats R-preprocessCore
BuildRequires:    R-zlibbioc R-methods 


%description
A package that extends and improves the functionality of the base affy
package. Routines that make heavy use of compiled code for speed. Central
focus is on implementation of methods for fitting probe-level models and
tools using these models. PLM based quality assessment tools.

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.30.0-1
- initial package for Fedora