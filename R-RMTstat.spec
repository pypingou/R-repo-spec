%global packname  RMTstat
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          Distributions, Statistics and Tests derived from Random Matrix Theory

Group:            Applications/Engineering 
License:          BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Functions for working with the Tracy-Widom laws and other distributions
related to the eigenvalues of large Wishart matrices. . The tables for
computing the Tracy-Widom densities and distribution functions were
computed by Momar Dieng's MATLAB package "RMLab", which is available on
his homepage at http://math.arizona.edu/~momar/research.htm . This package
is part of a collaboration between Iain Johnstone, Zongming Ma, Patrick
Perry, and Morteza Shahram.  It will soon be replaced by a package with
more accuracy and built-in support for relevant statistical tests.

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
%doc %{rlibdir}/RMTstat/html
%doc %{rlibdir}/RMTstat/CITATION
%doc %{rlibdir}/RMTstat/DESCRIPTION
%{rlibdir}/RMTstat/LICENSE
%{rlibdir}/RMTstat/help
%{rlibdir}/RMTstat/NAMESPACE
%{rlibdir}/RMTstat/Meta
%{rlibdir}/RMTstat/R
%{rlibdir}/RMTstat/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2-1
- initial package for Fedora