%global packname  rnaSeqMap
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.8.0
Release:          1%{?dist}
Summary:          rnaSeq secondary analyses

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-xmapcore R-Biobase R-Rsamtools 

BuildRequires:    R-devel tex(latex) R-methods R-xmapcore R-Biobase R-Rsamtools 

%description
Provides means of analysis for RNAseq data, used together with genomic
annotation. Requires a set of BAM files on the input or alternatively, an
xmapcore database in MySQL as a back-end, which is also a storage for
sequencing reads. Front-end analyses include transformations of the
coverage function, splicing analysis, finding irreducible regions with the
two-sliding-windows algorithm and genomic region visualizations.

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
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.8.0-1
- initial package for Fedora