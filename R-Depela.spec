%global packname  Depela
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0
Release:          1%{?dist}
Summary:          Depela

Group:            Applications/Engineering 
License:          GPL (version 2 or later)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats R-stats4 R-copula 

BuildRequires:    R-devel tex(latex) R-stats R-stats4 R-copula 

%description
Implement semiparametric estimation of copula model, and deal with
structural break problems in copula modelling.

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
%doc %{rlibdir}/Depela/DESCRIPTION
%doc %{rlibdir}/Depela/html
%{rlibdir}/Depela/INDEX
%{rlibdir}/Depela/NAMESPACE
%{rlibdir}/Depela/help
%{rlibdir}/Depela/R
%{rlibdir}/Depela/Meta

%changelog
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0-1
- initial package for Fedora