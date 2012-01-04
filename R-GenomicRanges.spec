%global packname  GenomicRanges
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6.4
Release:          1%{?dist}
Summary:          Representation and manipulation of genomic intervals

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-IRanges 
Requires:         R-methods R-IRanges 

BuildRequires:    R-devel tex(latex) R-methods R-IRanges
BuildRequires:    R-methods R-IRanges 


%description
The ability to efficiently store genomic annotations and alignments is
playing a central role when it comes to analyze high-throughput sequencing
data (a.k.a. NGS data). The package defines general purpose containers for
storing genomic intervals as well as more specialized containers for
storing alignments against a reference genome.

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
%doc %{rlibdir}/GenomicRanges/doc
%doc %{rlibdir}/GenomicRanges/html
%doc %{rlibdir}/GenomicRanges/DESCRIPTION
%doc %{rlibdir}/GenomicRanges/NEWS
%{rlibdir}/GenomicRanges/R
%{rlibdir}/GenomicRanges/NAMESPACE
%{rlibdir}/GenomicRanges/INDEX
RPM build errors:
%{rlibdir}/GenomicRanges/Meta
%{rlibdir}/GenomicRanges/scripts
%{rlibdir}/GenomicRanges/unitTests
%{rlibdir}/GenomicRanges/help
%{rlibdir}/GenomicRanges/extdata
%{rlibdir}/GenomicRanges/libs

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.4-1
- initial package for Fedora