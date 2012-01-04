%global packname  fpc
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.0.3
Release:          1%{?dist}
Summary:          Flexible procedures for clustering

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.0-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS R-cluster R-mclust R-flexmix 


BuildRequires:    R-devel tex(latex) R-MASS R-cluster R-mclust R-flexmix



%description
Various methods for clustering and cluster validation. Fixed point
clustering. Linear regression clustering. Clustering by merging Gaussian
mixture components. Symmetric and asymmetric discriminant projections for
visualisation of the separation of groupings. Cluster validation
statistics for distance based clustering including corrected Rand index.
Clusterwise cluster stability assessment. Methods for estimation of the
number of clusters: Calinski-Harabasz, Tibshirani and Walther's prediction
strength. Gaussian/multinomial mixture fitting for mixed
continuous/categorical variables. Veriablewise statistics for cluster
interpretation. DBSCAN clustering. Interface functions for many clustering
methods implemented in R, including estimating the number of clusters with
kmeans, pam and clara. Modality diagnosis for Gaussian mixtures. Note that
the use of the package mclust (called by function prabclust) is protected
by a special license, see
http://www.stat.washington.edu/mclust/license.txt. For an overview see

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
%doc %{rlibdir}/fpc/html
%doc %{rlibdir}/fpc/DESCRIPTION
%{rlibdir}/fpc/R
%{rlibdir}/fpc/Meta
%{rlibdir}/fpc/data
%{rlibdir}/fpc/INDEX
%{rlibdir}/fpc/help
%{rlibdir}/fpc/NAMESPACE

%changelog
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.3-1
- initial package for Fedora