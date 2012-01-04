%global packname  glmmBUGS
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.9
Release:          1%{?dist}
Summary:          Generalised Linear Mixed Models and Spatial Models with WinBUGS, BRugs, or OpenBUGS

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS R-abind R-spdep 


BuildRequires:    R-devel tex(latex) R-MASS R-abind R-spdep



%description
Write bugs model files for hierarchical and spatial models, arranges
unbalanced data in ragged arrays, and creates starting values.

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.9-1
- initial package for Fedora