%global packname  ShortRead
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.12.2
Release:          1%{?dist}
Summary:          Classes and methods for high-throughput short-read sequencing data.

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-IRanges R-GenomicRanges R-Biostrings R-lattice R-Rsamtools R-latticeExtra 

BuildRequires:    R-devel tex(latex) R-methods R-IRanges R-GenomicRanges R-Biostrings R-lattice R-Rsamtools R-latticeExtra 

%description
Base classes, functions, and methods for representation of
high-throughput, short-read sequencing data.

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
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.12.2-1
- initial package for Fedora