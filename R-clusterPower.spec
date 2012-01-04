%global packname  clusterPower
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          Power calculations for cluster-randomized crossover trials

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lme4 


BuildRequires:    R-devel tex(latex) R-lme4



%description
This package enables researchers to calculate power for cluster-randomized
crossover trials by employing a simulation-based approach.  A particular
study design is specified, with fixed sample sizes for all clusters and an
assumed treatment effect, and the empirical power for that study design is
calculated by simulating hypothetical datasets.

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
%doc %{rlibdir}/clusterPower/html
%doc %{rlibdir}/clusterPower/DESCRIPTION
%{rlibdir}/clusterPower/NAMESPACE
%{rlibdir}/clusterPower/help
%{rlibdir}/clusterPower/Meta
%{rlibdir}/clusterPower/INDEX
%{rlibdir}/clusterPower/R

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1-1
- initial package for Fedora