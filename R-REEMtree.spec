%global packname  REEMtree
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.90.3
Release:          1%{?dist}
Summary:          Regression Trees with Random Effects for Longitudinal (Panel) Data

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-nlme R-rpart R-methods 

BuildRequires:    R-devel tex(latex) R-nlme R-rpart R-methods 

%description
This package estimates regression trees with random effects as a way to
use data mining techniques to describe longitudinal or panel data.

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
%doc %{rlibdir}/REEMtree/html
%doc %{rlibdir}/REEMtree/DESCRIPTION
%doc %{rlibdir}/REEMtree/CITATION
%{rlibdir}/REEMtree/help
%{rlibdir}/REEMtree/INDEX
%{rlibdir}/REEMtree/Meta
%{rlibdir}/REEMtree/data
%{rlibdir}/REEMtree/R
%{rlibdir}/REEMtree/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.90.3-1
- initial package for Fedora