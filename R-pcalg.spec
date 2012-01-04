%global packname  pcalg
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.4
Release:          1%{?dist}
Summary:          Estimation of CPDAG/PAG and causal inference using the IDA algorithm

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-abind R-corpcor R-sfsmisc 
Requires:         R-graph R-RBGL R-ggm R-robustbase R-graphics R-vcd 

BuildRequires:    R-devel tex(latex) R-methods R-abind R-corpcor R-sfsmisc
BuildRequires:    R-graph R-RBGL R-ggm R-robustbase R-graphics R-vcd 


%description
Standard and robust estimation of the equivalence class of a Directed
Acyclic Graph (DAG) via the PC-Algorithm. The equivalence class is
represented by its (unique) Completete Partially Directed Acyclic Graph
(CPDAG). Furthermore, a PAG instead of a CPDAG can be estimated if latent
variables and/or selection variables are assumed to be present. FCI and
RFCI are available for estimating PAGs. Functions for causal inference
using the IDA algorithm (based on do-calculus of Judea Pearl) are provided
for CPDAGs.

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.4-1
- initial package for Fedora