%global packname  eisa
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6.0
Release:          1%{?dist}
Summary:          Expression data analysis via the Iterative Signature Algorithm

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-isa2 R-Biobase R-AnnotationDbi R-Category R-genefilter R-DBI 

BuildRequires:    R-devel tex(latex) R-methods R-isa2 R-Biobase R-AnnotationDbi R-Category R-genefilter R-DBI 

%description
The Iterative Signature Algorithm (ISA) is a biclustering method; it finds
correlated blocks (transcription modules) in gene expression (or other
tabular) data. The ISA is capable of finding overlapping modules and it is
resilient to noise. This package provides a convenient interface to the
ISA, using standard BioConductor data structures; and also contains
various visualization tools that can be used with other biclustering

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