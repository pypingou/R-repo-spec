%global packname  gclus
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          Clustering Graphics

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-cluster 

BuildRequires:    R-devel tex(latex) R-cluster 

%description
Orders panels in scatterplot matrices and parallel coordinate displays by
some merit index. Package contains various indices of merit, ordering
functions, and enhanced versions of pairs and parcoord which color panels
according to their merit level.

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
%doc %{rlibdir}/gclus/html
%doc %{rlibdir}/gclus/DESCRIPTION
%{rlibdir}/gclus/Meta
%{rlibdir}/gclus/INDEX
%{rlibdir}/gclus/data
%{rlibdir}/gclus/NAMESPACE
%{rlibdir}/gclus/R
%{rlibdir}/gclus/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3-1
- initial package for Fedora