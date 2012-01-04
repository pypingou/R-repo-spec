%global packname  girafe
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6.0
Release:          1%{?dist}
Summary:          Genome Intervals and Read Alignments for Functional Exploration

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-IRanges R-Rsamtools R-ShortRead R-intervals R-genomeIntervals R-grid 

BuildRequires:    R-devel tex(latex) R-methods R-IRanges R-Rsamtools R-ShortRead R-intervals R-genomeIntervals R-grid 

%description
The package 'girafe' deals with the genome-level representation of aligned
reads from next-generation sequencing data. It contains an object class
for enabling a detailed description of genome intervals with aligned reads
and functions for comparing, visualising, exporting and working with such
intervals and the aligned reads. As such, the package interacts with and
provides a link between the packages ShortRead, IRanges and

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.0-1
- initial package for Fedora