%global packname  globaltest
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          5.8.1
Release:          1%{?dist}
Summary:          Testing groups of covariates/features for association with a response variable, with applications to gene set testing

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 
Requires:         R-Biobase R-survival R-AnnotationDbi R-annotate R-multtest R-graphics 

BuildRequires:    R-devel tex(latex) R-methods
BuildRequires:    R-Biobase R-survival R-AnnotationDbi R-annotate R-multtest R-graphics 


%description
The global test tests groups of covariates (or features) for association
with a response variable. This package implements the test with diagnostic
plots and multiple testing utilities, along with several functions to
facilitate the use of this test for gene set testing of GO and KEGG terms.

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 5.8.1-1
- initial package for Fedora