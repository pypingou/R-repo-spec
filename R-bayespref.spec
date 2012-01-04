%global packname  bayespref
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Hierarchical Bayesian analysis of ecological count data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-coda R-lattice R-MASS R-MCMCpack R-RColorBrewer 

BuildRequires:    R-devel tex(latex) R-coda R-lattice R-MASS R-MCMCpack R-RColorBrewer 

%description
This program implements a hierarchical Bayesian analysis of count data,
such as preference experiments. It provides population-level and
individual-level preference parameter estimates obtained via MCMC. It also
allows for model comparison using Deviance Information Criterion.

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
%doc %{rlibdir}/bayespref/DESCRIPTION
%doc %{rlibdir}/bayespref/html
%{rlibdir}/bayespref/Meta
%{rlibdir}/bayespref/help
%{rlibdir}/bayespref/data
%{rlibdir}/bayespref/INDEX
%{rlibdir}/bayespref/R

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora