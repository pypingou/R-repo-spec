%global packname  GeneSelector
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.4.0
Release:          1%{?dist}
Summary:          Stability and Aggregation of ranked gene lists

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-stats R-Biobase 
Requires:         R-multtest R-siggenes R-samr R-limma 

BuildRequires:    R-devel tex(latex) R-methods R-stats R-Biobase
BuildRequires:    R-multtest R-siggenes R-samr R-limma 


%description
The term 'GeneSelector' refers to a filter selecting those genes which are
consistently identified as differentially expressed using various
statistical procedures. 'Selected' genes are those present at the top of
the list in various ranking methods (currently 14). In addition, the
stability of the findings can be taken into account in the final ranking
by examining perturbed versions of the original data set, e.g. by leaving
samples, swapping class labels, generating bootstrap replicates or adding
noise. Given multiple ranked lists, one can use aggregation methods in
order to find a synthesis.

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.4.0-1
- initial package for Fedora