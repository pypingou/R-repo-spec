%global packname  apComplex
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.20.0
Release:          1%{?dist}
Summary:          Estimate protein complex membership using AP-MS protein data

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-graph R-RBGL 
Requires:         R-Rgraphviz R-stats R-org.Sc.sgd.db 

BuildRequires:    R-devel tex(latex) R-graph R-RBGL
BuildRequires:    R-Rgraphviz R-stats R-org.Sc.sgd.db 


%description
Functions to estimate a bipartite graph of protein complex membership
using AP-MS data.

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.20.0-1
- initial package for Fedora