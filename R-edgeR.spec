%global packname  edgeR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.4.1
Release:          1%{?dist}
Summary:          Empirical analysis of digital gene expression data in R

Group:            Applications/Engineering 
License:          LGPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 
Requires:         R-limma 

BuildRequires:    R-devel tex(latex) R-methods
BuildRequires:    R-limma 


%description
Differential expression analysis of RNA-seq and digital gene expression
profiles with biological replication.  Uses empirical Bayes estimation and
exact tests based on the negative binomial distribution.  Also useful for
differential signal analysis with other types of genome-scale count data.

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
%doc %{rlibdir}/edgeR/NEWS
%doc %{rlibdir}/edgeR/html
%doc %{rlibdir}/edgeR/CITATION
%doc %{rlibdir}/edgeR/DESCRIPTION
%doc %{rlibdir}/edgeR/doc
%{rlibdir}/edgeR/help
%{rlibdir}/edgeR/INDEX
%{rlibdir}/edgeR/Meta
%{rlibdir}/edgeR/NAMESPACE
%{rlibdir}/edgeR/R
%{rlibdir}/edgeR/data

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.4.1-1
- initial package for Fedora