%global packname  mcsm
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Functions for Monte Carlo Methods with R

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats R-MASS R-coda 


BuildRequires:    R-devel tex(latex) R-stats R-MASS R-coda



%description
mcsm contains a collection of functions that allows the reenactment of the
R programs used in the book EnteR Monte Carlo Methods without further
programming. Programs being available as well, they can be modified by the
user to conduct one's own simulations.

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
%doc %{rlibdir}/mcsm/html
%doc %{rlibdir}/mcsm/DESCRIPTION
%{rlibdir}/mcsm/help
%{rlibdir}/mcsm/data
%{rlibdir}/mcsm/demo
%{rlibdir}/mcsm/NAMESPACE
%{rlibdir}/mcsm/Meta
%{rlibdir}/mcsm/INDEX
%{rlibdir}/mcsm/R

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora