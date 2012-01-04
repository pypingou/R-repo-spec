%global packname  DAGGER
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.4
Release:          1%{?dist}
Summary:          Consensus genetic maps

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Rglpk R-quadprog R-Matrix 

BuildRequires:    R-devel tex(latex) R-Rglpk R-quadprog R-Matrix 

%description
Integrates the information from multiple linkage maps to create a
consensus directed graph, which is then linearized to produce a consensus

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
%doc %{rlibdir}/DAGGER/DESCRIPTION
%doc %{rlibdir}/DAGGER/html
%{rlibdir}/DAGGER/INDEX
%{rlibdir}/DAGGER/NAMESPACE
%{rlibdir}/DAGGER/R
%{rlibdir}/DAGGER/Meta
%{rlibdir}/DAGGER/help

%changelog
* Fri Nov 25 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4-1
- initial package for Fedora