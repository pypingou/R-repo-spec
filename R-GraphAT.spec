%global packname  GraphAT
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.26.0
Release:          1%{?dist}
Summary:          Graph Theoretic Association Tests

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-graph R-methods 
Requires:         R-graph R-MCMCpack R-methods R-stats 

BuildRequires:    R-devel tex(latex) R-graph R-methods
BuildRequires:    R-graph R-MCMCpack R-methods R-stats 


%description
Functions and data used in Balasubramanian, et al. (2004)

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
%doc %{rlibdir}/GraphAT/DESCRIPTION
%doc %{rlibdir}/GraphAT/html
%{rlibdir}/GraphAT/Meta
%{rlibdir}/GraphAT/INDEX
%{rlibdir}/GraphAT/NAMESPACE
%{rlibdir}/GraphAT/help
%{rlibdir}/GraphAT/data
%{rlibdir}/GraphAT/R

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.26.0-1
- initial package for Fedora