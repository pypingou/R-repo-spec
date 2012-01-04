%global packname  RCASPAR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          A package for survival time prediction based on a piecewise baseline hazard Cox regression model.

Group:            Applications/Engineering 
License:          GPL (>=3)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
The package is the R-version of the C-based software \bold{CASPAR}
(Kaderali,2006:
\url{http://bioinformatics.oxfordjournals.org/content/22/12/1495}). It is
meant to help predict survival times in the presence of high-dimensional
explanatory covariates. The model is a piecewise baseline hazard Cox
regression model with an Lq-norm based prior that selects for the most
important regression coefficients, and in turn the most relevant
covariates for survival analysis. It was primarily tried on gene
expression and aCGH data, but can be used on any other type of
high-dimensional data and in disciplines other than biology and medicine.
biocViews: aCGH, GeneExpression, Genetics, Proteomics, Visualization

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
%doc %{rlibdir}/RCASPAR/doc
%doc %{rlibdir}/RCASPAR/html
%doc %{rlibdir}/RCASPAR/DESCRIPTION
%{rlibdir}/RCASPAR/Meta
%{rlibdir}/RCASPAR/data
%{rlibdir}/RCASPAR/R
%{rlibdir}/RCASPAR/NAMESPACE
%{rlibdir}/RCASPAR/INDEX
RPM build errors:
%{rlibdir}/RCASPAR/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora