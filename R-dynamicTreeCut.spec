%global packname  dynamicTreeCut
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.21
Release:          1%{?dist}
Summary:          Methods for detection of clusters in hierarchical clustering dendrograms.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
Contains methods for detection of clusters in hierarchical clustering

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
%doc %{rlibdir}/dynamicTreeCut/DESCRIPTION
%doc %{rlibdir}/dynamicTreeCut/html
%{rlibdir}/dynamicTreeCut/R
%{rlibdir}/dynamicTreeCut/INDEX
%{rlibdir}/dynamicTreeCut/Meta
%{rlibdir}/dynamicTreeCut/NAMESPACE
%{rlibdir}/dynamicTreeCut/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.21-1
- initial package for Fedora