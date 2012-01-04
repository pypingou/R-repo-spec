%global packname  gtx
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.3
Release:          1%{?dist}
Summary:          Genetics ToolboX

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Assorted tools for genetic association analyses.  The focus is on
implementing (either exactly or approximately) regression analyses using
summary statistics instead of using subject-specific data.  So far,
functions exist to support multi-SNP risk score analyses, and multi-SNP
conditional regression analyses, using summary statistics.  There are
helper functions for reading and manipulating subject-specific genotype
data, which provide a platform for calculating the summary statistics, or
for using R to conduct other analyses not supported by specific GWAS
analysis tools.

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
%doc %{rlibdir}/gtx/DESCRIPTION
%doc %{rlibdir}/gtx/html
%{rlibdir}/gtx/Meta
%{rlibdir}/gtx/NAMESPACE
%{rlibdir}/gtx/R
%{rlibdir}/gtx/help
%{rlibdir}/gtx/data
%{rlibdir}/gtx/INDEX

%changelog
* Sat Dec 03 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.3-1
- initial package for Fedora