%global packname  ppiData
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.16
Release:          1%{?dist}
Summary:          A package that contains the bait to prey directed graphs for protein-protein interactions.

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-graph 

BuildRequires:    R-devel tex(latex) R-graph 

%description
This package contains the directed graphs for protein interaction data as
derived from Y2H and APMS as well as the code used to obtain the y2h data
from IntAct Repository.

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
%doc %{rlibdir}/ppiData/DESCRIPTION
%doc %{rlibdir}/ppiData/html
%doc %{rlibdir}/ppiData/doc
%{rlibdir}/ppiData/R
%{rlibdir}/ppiData/NAMESPACE
%{rlibdir}/ppiData/INDEX
%{rlibdir}/ppiData/help
%{rlibdir}/ppiData/data
%{rlibdir}/ppiData/Scripts
%{rlibdir}/ppiData/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.16-1
- initial package for Fedora