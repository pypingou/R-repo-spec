%global packname  CCMtools
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Clustering through "Correlation Clustering Model" (CCM) and cluster analysis tools.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-mclust R-class R-tree R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-mclust R-class R-tree R-mvtnorm 

%description
This package proposes a clustering method called "Correlation Clustering
Model" (CCM) based on mixture of canonical correlation analysis (CCA). It
also provides some tools for cluster analysis.

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
%doc %{rlibdir}/CCMtools/DESCRIPTION
%doc %{rlibdir}/CCMtools/html
%{rlibdir}/CCMtools/Meta
%{rlibdir}/CCMtools/INDEX
%{rlibdir}/CCMtools/R
%{rlibdir}/CCMtools/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora