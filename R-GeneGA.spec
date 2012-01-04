%global packname  GeneGA
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.0
Release:          1%{?dist}
Summary:          Design gene based on both mRNA secondary structure and codon usage bias using Genetic algorithm

Group:            Applications/Engineering 
License:          GPL version 2
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-GeneRfold R-seqinr R-hash R-methods 


BuildRequires:    R-devel tex(latex) R-GeneRfold R-seqinr R-hash R-methods



%description
R based Genetic algorithm for gene expression optimization by considering
both mRNA secondary structure and codon usage bias, GeneGA includes the
information of highly expressed genes of almost 200 genomes.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.0-1
- initial package for Fedora