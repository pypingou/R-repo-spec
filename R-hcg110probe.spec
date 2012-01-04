%global packname  hcg110probe
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.9.0
Release:          1%{?dist}
Summary:          Probe sequence data for microarrays of type hcg110

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/data/annotation/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/annotation/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-AnnotationDbi 


BuildRequires:    R-devel tex(latex) R-AnnotationDbi



%description
This package was automatically created by package AnnotationDbi version
1.15.34. The probe sequence data was obtained from
http://www.affymetrix.com. The file name was HC-G110\_probe\_tab.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.9.0-1
- initial package for Fedora