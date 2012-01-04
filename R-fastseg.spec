%global packname  fastseg
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          fastseg - a fast segmentation algorithm

Group:            Applications/Engineering 
License:          LGPL (>= 2.0)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-GenomicRanges 
Requires:         R-graphics R-stats R-IRanges 

BuildRequires:    R-devel tex(latex) R-GenomicRanges
BuildRequires:    R-graphics R-stats R-IRanges 


%description
fastseg implements a very fast and efficient segmentation algorithm. It
has similar functionality as DNACopy (Olshen and Venkatraman 2004), but is
considerably faster and more flexible. fastseg can segment data stemming
from DNA microarrays and data stemming from next generation sequencing for
example to detect copy number segments. Further it can segment data
stemming from RNA microarrays like tiling arrays to identify transcripts.
Most generally, it can segment data given as a matrix or as a vector.
Various data formats can be used as input to fastseg like expression set
objects for microarrays or GRanges for sequencing data. The segmentation
criterion of fastseg is based on a statistical tests in a Bayesian
framework, namely the cyber t-test (Baldi 2001). The speed-up stems from
the facts, that sampling is not necessary in for fastseg and that a
dynamic programming approach is used for calculation of the segments'
first and higher order moments.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora