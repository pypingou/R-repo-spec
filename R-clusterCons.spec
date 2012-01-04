%global packname  clusterCons
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Calculate the consensus clustering result from re-sampled clustering experiments with the option of using multiple algorithms and parameter

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-cluster R-lattice R-RColorBrewer R-grid R-apcluster 

BuildRequires:    R-devel tex(latex) R-methods R-cluster R-lattice R-RColorBrewer R-grid R-apcluster 

%description
clusterCons is a package containing functions that generate robustness
measures for clusters and cluster membership based on generating consensus
matrices from bootstrapped clustering experiments in which a random
proportion of rows of the data set are used in each individual clustering.
This allows the user to prioritise clusters and the members of clusters
based on their consistency in this regime. The functions allow the user to
select several algorithms to use in the re-sampling scheme and with any of
the parameters that the algorithm would normally take.

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
%doc %{rlibdir}/clusterCons/CITATION
%doc %{rlibdir}/clusterCons/DESCRIPTION
%doc %{rlibdir}/clusterCons/html
%{rlibdir}/clusterCons/INDEX
%{rlibdir}/clusterCons/help
%{rlibdir}/clusterCons/data
%{rlibdir}/clusterCons/Meta
%{rlibdir}/clusterCons/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora