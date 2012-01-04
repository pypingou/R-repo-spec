%global packname  hopach
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.14.0
Release:          1%{?dist}
Summary:          Hierarchical Ordered Partitioning and Collapsing Hybrid (HOPACH)

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-cluster R-Biobase R-methods 

BuildRequires:    R-devel tex(latex) R-cluster R-Biobase R-methods 

%description
The HOPACH clustering algorithm builds a hierarchical tree of clusters by
recursively partitioning a data set, while ordering and possibly
collapsing clusters at each level. The algorithm uses the Mean/Median
Split Silhouette (MSS) criteria to identify the level of the tree with
maximally homogeneous clusters. It also runs the tree down to produce a
final ordered list of the elements. The non-parametric bootstrap allows
one to estimate the probability that each element belongs to each cluster
(fuzzy clustering).

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.14.0-1
- initial package for Fedora