%global packname  clusterGeneration
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.7
Release:          1%{?dist}
Summary:          random cluster generation (with specified degree of separation)

Group:            Applications/Engineering 
License:          GPL version 2 or newer
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS 

BuildRequires:    R-devel tex(latex) R-MASS 

%description
The package contains functions for generating random clusters, generating
random covariance/correlation matrices, calculating a separation index
(data and population version) for pairs of clusters or cluster
distributions, and 1-D and 2-D projection plots to visualize clusters. The
package also contains a function to generate random clusters based on
factorial designs with factors such as degree of separation, number of
clusters, number of variables, number of noisy variables.

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
%doc %{rlibdir}/clusterGeneration/DESCRIPTION
%doc %{rlibdir}/clusterGeneration/html
%{rlibdir}/clusterGeneration/NAMESPACE
%{rlibdir}/clusterGeneration/help
%{rlibdir}/clusterGeneration/R
%{rlibdir}/clusterGeneration/INDEX
%{rlibdir}/clusterGeneration/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.7-1
- initial package for Fedora