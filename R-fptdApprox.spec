%global packname  fptdApprox
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Approximation of first-passage-time densities for diffusion processes.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package contains several functions for an efficient approximation of
first-passage-time densities for diffusion processes based on the
First-Passage-Time Location (FPTL) function.

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
%doc %{rlibdir}/fptdApprox/html
%doc %{rlibdir}/fptdApprox/DESCRIPTION
%{rlibdir}/fptdApprox/NAMESPACE
%{rlibdir}/fptdApprox/R
%{rlibdir}/fptdApprox/Meta
%{rlibdir}/fptdApprox/demo
%{rlibdir}/fptdApprox/INDEX
%{rlibdir}/fptdApprox/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora