%global packname  flexclust
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3.2
Release:          1%{?dist}
Summary:          Flexible Cluster Algorithms

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.3-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-graphics R-grid R-lattice R-modeltools 

BuildRequires:    R-devel tex(latex) R-graphics R-grid R-lattice R-modeltools 

%description
The main function kcca implements a general framework for k-centroids
cluster analysis supporting arbitrary distance measures and centroid
computation. Further cluster methods include hard competitive learning,
neural gas, and QT clustering. There are numerous visualization methods
for cluster results (neighborhood graphs, convex cluster hulls, barcharts
of centroids, ...), and bootstrap methods for the analysis of cluster

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.2-1
- initial package for Fedora