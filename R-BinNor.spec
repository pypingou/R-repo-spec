%global packname  BinNor
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Simultaneous generation of multivariate binary and normal variates.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-mvtnorm R-corpcor R-psych R-Matrix 

BuildRequires:    R-devel tex(latex) R-mvtnorm R-corpcor R-psych R-Matrix 

%description
Generating multiple binary and normal variables simultaneously given
marginal characteristics and association structure based on the
methodology proposed by Demirtas and Doganay (2012).

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
%doc %{rlibdir}/BinNor/html
%doc %{rlibdir}/BinNor/DESCRIPTION
%{rlibdir}/BinNor/R
%{rlibdir}/BinNor/Meta
%{rlibdir}/BinNor/help
%{rlibdir}/BinNor/INDEX
%{rlibdir}/BinNor/NAMESPACE

%changelog
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora