%global packname  miRNApath
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.14.0
Release:          1%{?dist}
Summary:          miRNApath: Pathway Enrichment for miRNA Expression Data

Group:            Applications/Engineering 
License:          LGPL-2.1
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
This package provides pathway enrichment techniques for miRNA expression
data. Specifically, the set of methods handles the many-to-many
relationship between miRNAs and the multiple genes they are predicted to
target (and thus affect.)  It also handles the gene-to-pathway
relationships separately. Both steps are designed to preserve the additive
effects of miRNAs on genes, many miRNAs affecting one gene, one miRNA
affecting multiple genes, or many miRNAs affecting many genes.

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
%doc %{rlibdir}/miRNApath/CITATION
%doc %{rlibdir}/miRNApath/html
%doc %{rlibdir}/miRNApath/NEWS
%doc %{rlibdir}/miRNApath/DESCRIPTION
%doc %{rlibdir}/miRNApath/doc
%{rlibdir}/miRNApath/NAMESPACE
%{rlibdir}/miRNApath/help
%{rlibdir}/miRNApath/Meta
%{rlibdir}/miRNApath/samples
%{rlibdir}/miRNApath/data
%{rlibdir}/miRNApath/R
%{rlibdir}/miRNApath/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.14.0-1
- initial package for Fedora