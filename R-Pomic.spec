%global packname  Pomic
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Pattern Oriented Modelling Information Criterion

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
This package propose calculations of an information criterion to check the
quality of simulations results of ABM/IBM or other non-linear rule-based
models. The POMDEV measure is based on the KL divergence and likelihood
theory. It basically indicates the deviance of simulation results from
field observations. Once POMDEV scores and metropolis-hasting sampling on
different model versions are effectuated, POMIC scores can be calculated.
This method is still under development and further work are needed for the
incorporation of multiple patterns assessment.

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
%doc %{rlibdir}/Pomic/CITATION
%doc %{rlibdir}/Pomic/NEWS
%doc %{rlibdir}/Pomic/DESCRIPTION
%doc %{rlibdir}/Pomic/html
%{rlibdir}/Pomic/R
%{rlibdir}/Pomic/demo
%{rlibdir}/Pomic/NAMESPACE
%{rlibdir}/Pomic/INDEX
%{rlibdir}/Pomic/help
%{rlibdir}/Pomic/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora