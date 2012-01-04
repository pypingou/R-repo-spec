%global packname  prabclus
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.2.2
Release:          1%{?dist}
Summary:          Functions for clustering of presence-absence, abundance and multilocus genetic data

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.2-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS R-mclust 

BuildRequires:    R-devel tex(latex) R-MASS R-mclust 

%description
Distance-based parametric bootstrap tests for clustering with spatial
neighborhood information. Some distance measures, Clustering of
presence-absence, abundance and multilocus genetical data for species
delimitation, nearest neighbor based noise detection. Try package?prabclus
for on overview. Note that the use of the package mclust (called by
function prabclust) is protected by a special license, see
http://www.stat.washington.edu/mclust/license.txt, particularly point 6.

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
%doc %{rlibdir}/prabclus/html
%doc %{rlibdir}/prabclus/DESCRIPTION
%{rlibdir}/prabclus/R
%{rlibdir}/prabclus/help
%{rlibdir}/prabclus/data
%{rlibdir}/prabclus/Meta
%{rlibdir}/prabclus/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.2.2-1
- initial package for Fedora