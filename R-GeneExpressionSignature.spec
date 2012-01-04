%global packname  GeneExpressionSignature
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Gene Expression Signature based Similarity Metric

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase 

BuildRequires:    R-devel tex(latex) R-Biobase 

%description
This package gives the implementations of the gene expression signature
and its distance to each. Gene expression signature is represented as a
list of genes whose expression is correlated with a biological state of
interest. And its distance is defined using a nonparametric, rank-based
pattern-matching strategy based on the Kolmogorov-Smirnov statistic. Gene
expression signature and its distance can be used to detect similarities
among the signatures of drugs, diseases, and biological states of

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora