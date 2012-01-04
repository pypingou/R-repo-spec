%global packname  gage
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.4.0
Release:          1%{?dist}
Summary:          Generally Applicable Gene-set Enrichment for Pathway Analysis

Group:            Applications/Engineering 
License:          GPL (>=2.0)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-graph R-multtest 

BuildRequires:    R-devel tex(latex) R-graph R-multtest 

%description
GAGE is a published method for gene set or pathway analysis. GAGE is
generally applicable independent of microarray data attributes including
sample sizes, experimental designs, microarray platforms, and other types
of heterogeneity, and consistently achieves superior performance over
other frequently used methods. In gage package, we provide functions for
basic GAGE analysis, result processing and presentation. We have also
built pipeline routines for of multiple GAGE analyses in a batch,
comparison between parallel analyses, and combined analysis of
heterogeneous data from different sources/studies. In addition, we provide
demo microarray data and commonly used gene set data based on KEGG
pathways and GO terms. These funtions and data are also useful for gene
set analysis using other methods.

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.4.0-1
- initial package for Fedora