%global packname  Rsubread
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.2
Release:          1%{?dist}
Summary:          Rsubread: a super fast, sensitive and accurate read aligner for mapping next-generation sequencing reads

Group:            Applications/Engineering 
License:          LGPL-3
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package performs read mapping, exon junction detection and other
tasks for next-generation sequencing data. The read mapping function
implements a novel mapping paradigm, which is entirely different from the
"seed-and-extent" paradigm. It can be used to map both short reads and
long reads (>200bp) and reads of variable lengths. It also provides
functions to summarize read counts to genes or exons and gives detection p
values for each gene in the RNA-seq data.

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
%doc %{rlibdir}/Rsubread/NEWS
%doc %{rlibdir}/Rsubread/html
%doc %{rlibdir}/Rsubread/CITATION
%doc %{rlibdir}/Rsubread/DESCRIPTION
%doc %{rlibdir}/Rsubread/doc
%{rlibdir}/Rsubread/Meta
%{rlibdir}/Rsubread/help
%{rlibdir}/Rsubread/libs
%{rlibdir}/Rsubread/INDEX
%{rlibdir}/Rsubread/R
%{rlibdir}/Rsubread/annot
%{rlibdir}/Rsubread/NAMESPACE
%{rlibdir}/Rsubread/extdata

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.2-1
- initial package for Fedora