%global packname  clusterSim
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.40.6
Release:          1%{?dist}
Summary:          Searching for optimal clustering procedure for a data set

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.40-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-ade4 R-cluster R-R2HTML R-e1071 R-rgl R-MASS R-mlbench 


BuildRequires:    R-devel tex(latex) R-ade4 R-cluster R-R2HTML R-e1071 R-rgl R-MASS R-mlbench



%description
GDM Distance, Sokal-Michener Distance, Bray-Curtis Distance,
Calinski-Harabasz Index, G2 Index, G3 Index, Silhouette Index,
Krzanowski-Lai Index, Hartigan Index, Gap Index, DB Index, Data
Normalization, HINoV method, Replication analysis for cluster validation,
Clustering with several algorithms, distances, Symbolic interval
distances, Plot functions, Random cluster generation, Linear ordering
methods, Comparing partitions, Spectral clustering.

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
%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.40.6-1
- initial package for Fedora