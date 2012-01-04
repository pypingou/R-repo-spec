%global packname  Modalclust
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          Hierarchical Modal Clustering

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-mvtnorm R-zoo R-class 

BuildRequires:    R-devel tex(latex) R-mvtnorm R-zoo R-class 

%description
Perfroms Modal Clustering (MAC) including Hierarchical Modal Clustering
(HMAC) along with their parallel implementation (PHMAC) over several
processors.  These model-based non-parametric clustering techniques can
extract clusters in very high dimensions with arbitrary density shapes. By
default clustering is performed over several resolutions and the results
are summarized as a hierarchical tree. Associated plot functions are also
provided. There is a package vignette that provides many examples.

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
%doc %{rlibdir}/Modalclust/html
%doc %{rlibdir}/Modalclust/DESCRIPTION
%doc %{rlibdir}/Modalclust/doc
%{rlibdir}/Modalclust/Meta
%{rlibdir}/Modalclust/NAMESPACE
%{rlibdir}/Modalclust/demo
%{rlibdir}/Modalclust/data
%{rlibdir}/Modalclust/R
%{rlibdir}/Modalclust/INDEX
%{rlibdir}/Modalclust/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2-1
- initial package for Fedora