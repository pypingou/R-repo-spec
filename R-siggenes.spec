%global packname  siggenes
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.28.0
Release:          1%{?dist}
Summary:          Multiple testing using SAM and Efron's empirical Bayes approaches

Group:            Applications/Engineering 
License:          LGPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-multtest R-Biobase R-splines 


BuildRequires:    R-devel tex(latex) R-methods R-multtest R-Biobase R-splines



%description
Identification of differentially expressed genes and estimation of the
False Discovery Rate (FDR) using both the Significance Analysis of
Microarrays (SAM) and the Empirical Bayes Analyses of Microarrays (EBAM).

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
%doc %{rlibdir}/siggenes/html
%doc %{rlibdir}/siggenes/doc
%doc %{rlibdir}/siggenes/DESCRIPTION
%{rlibdir}/siggenes/Meta
%{rlibdir}/siggenes/INDEX
%{rlibdir}/siggenes/R
%{rlibdir}/siggenes/NAMESPACE
%{rlibdir}/siggenes/help

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.28.0-1
- initial package for Fedora