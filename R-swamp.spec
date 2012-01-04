%global packname  swamp
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Analysis and visualization of high-dimensional data in respect to sample annotations.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-impute R-amap R-gplots 


BuildRequires:    R-devel tex(latex) R-impute R-amap R-gplots



%description
The package contains functions to connect the structure of the data with
the information on the samples. Three types of associations are covered:
1. linear model of principal components. 2. hierarchical clustering
analysis. 3. distribution of features-sample annotation associations.
Additionally, the inter-relation between sample annotations can be
analyzed. Simple methods are provided for the correction of batch effects
and removal of principal components.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora