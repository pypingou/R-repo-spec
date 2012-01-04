%global packname  scrime
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.8
Release:          1%{?dist}
Summary:          Analysis of High-Dimensional Categorical Data such as SNP Data

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Tools for the analysis of high-dimensional data developed/implemented at
the group "Statistical Complexity Reduction In Molecular Epidemiology"
(SCRIME). Main focus is on SNP data. But most of the functions can also be
applied to other types of categorical data.

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
%doc %{rlibdir}/scrime/DESCRIPTION
%doc %{rlibdir}/scrime/html
%{rlibdir}/scrime/NAMESPACE
%{rlibdir}/scrime/CHANGES
%{rlibdir}/scrime/help
%{rlibdir}/scrime/R
%{rlibdir}/scrime/INDEX
%{rlibdir}/scrime/Meta

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.8-1
- initial package for Fedora