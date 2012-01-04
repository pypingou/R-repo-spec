%global packname  OSACC
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Ordered Subset Analysis for Case-Control Studies

Group:            Applications/Engineering 
License:          LGPL (>= 2.0)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Genetic heterogeneity can reduce the power for complex disease gene
mapping since only a fraction of the cases in the collected dataset may
carry a specific disease susceptibility allele. The Ordered Subset
Analysis for Case-Control data (OSACC) program was designed to evaluate
evidence for association in the presence of genetic heterogeneity. For a
more detailed description of the method and results of an extensive
simulation study based on different models of genetic heterogeneity.
Please see Qin et. al.(2010), Ordered Subset Analysis for Case-Control
Studies, Genetic Epidemiology 34(5), 407-417.

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
%doc %{rlibdir}/OSACC/html
%doc %{rlibdir}/OSACC/CITATION
%doc %{rlibdir}/OSACC/DESCRIPTION
%{rlibdir}/OSACC/INDEX
%{rlibdir}/OSACC/help
%{rlibdir}/OSACC/NAMESPACE
%{rlibdir}/OSACC/R
%{rlibdir}/OSACC/Meta
%{rlibdir}/OSACC/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora