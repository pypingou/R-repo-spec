%global packname  distrSim
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.3.1
Release:          1%{?dist}
Summary:          Simulation classes based on package distr

Group:            Applications/Engineering 
License:          LGPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-graphics R-setRNG R-distr R-startupmsg 

BuildRequires:    R-devel tex(latex) R-methods R-graphics R-setRNG R-distr R-startupmsg 

%description
Simulation (S4-)classes based on package distr

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
%doc %{rlibdir}/distrSim/DESCRIPTION
%doc %{rlibdir}/distrSim/CITATION
%doc %{rlibdir}/distrSim/NEWS
%doc %{rlibdir}/distrSim/html
%{rlibdir}/distrSim/Meta
%{rlibdir}/distrSim/demo
%{rlibdir}/distrSim/R
%{rlibdir}/distrSim/MASKING
%{rlibdir}/distrSim/INDEX
%{rlibdir}/distrSim/NAMESPACE
%{rlibdir}/distrSim/help
%{rlibdir}/distrSim/TOBEDONE

%changelog
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.3.1-1
- initial package for Fedora