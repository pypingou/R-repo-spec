%global packname  RHT
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Regularized Hotelling's T-square Test for Pathway (Gene Set) Analysis

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package offers functions to perform regularized Hotelling's T-square
test for pathway or gene set analysis. The package is tailored for but not
limited to proteomics data, in which sample sizes are often small, a large
proportion of the data are missing and/or correlations may be present.

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
%doc %{rlibdir}/RHT/html
%doc %{rlibdir}/RHT/DESCRIPTION
%{rlibdir}/RHT/INDEX
%{rlibdir}/RHT/Meta
%{rlibdir}/RHT/R
%{rlibdir}/RHT/NAMESPACE
%{rlibdir}/RHT/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora