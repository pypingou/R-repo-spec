%global packname  distrTEst
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.3.1
Release:          1%{?dist}
Summary:          Estimation and Testing classes based on package distr

Group:            Applications/Engineering 
License:          LGPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-graphics R-setRNG R-distr R-distrSim R-startupmsg 

BuildRequires:    R-devel tex(latex) R-methods R-graphics R-setRNG R-distr R-distrSim R-startupmsg 

%description
Evaluation (S4-)classes based on package distr for evaluating procedures
(estimators/tests) at data/simulation in a unified way.

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
%doc %{rlibdir}/distrTEst/DESCRIPTION
%doc %{rlibdir}/distrTEst/html
%doc %{rlibdir}/distrTEst/CITATION
%doc %{rlibdir}/distrTEst/NEWS
%{rlibdir}/distrTEst/demo
%{rlibdir}/distrTEst/R
%{rlibdir}/distrTEst/TOBEDONE
%{rlibdir}/distrTEst/help
%{rlibdir}/distrTEst/Meta
%{rlibdir}/distrTEst/NAMESPACE
%{rlibdir}/distrTEst/INDEX

%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.3.1-1
- initial package for Fedora