%global packname  iSeq
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6.0
Release:          1%{?dist}
Summary:          Bayesian Hierarchical Modeling of ChIP-seq Data Through Hidden Ising Models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package uses Bayesian hidden Ising models to identify IP-enriched
genomic regions from ChIP-seq data. It can be used to analyze ChIP-seq
data with or without controls.

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
%doc %{rlibdir}/iSeq/doc
%doc %{rlibdir}/iSeq/html
%doc %{rlibdir}/iSeq/DESCRIPTION
%{rlibdir}/iSeq/data
%{rlibdir}/iSeq/NAMESPACE
%{rlibdir}/iSeq/help
%{rlibdir}/iSeq/Meta
%{rlibdir}/iSeq/demo
%{rlibdir}/iSeq/R
%{rlibdir}/iSeq/libs
%{rlibdir}/iSeq/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.0-1
- initial package for Fedora