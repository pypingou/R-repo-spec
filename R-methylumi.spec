%global packname  methylumi
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.0.1
Release:          1%{?dist}
Summary:          Handle Illumina methylation data

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-methods 

BuildRequires:    R-devel tex(latex) R-Biobase R-methods 

%description
This package provides classes for holding and manipulating Illumina
methylation data.  Based on eSet, it can contain MIAME information, sample
information, feature information, and multiple matrices of data.  An
"intelligent" import function, methylumiR can read the Illumina text files
and create a MethyLumiSet. methylumIDAT can directly read raw IDAT files
from HumanMethylation27 and HumanMethylation450 microarrays. 
Normalization, background correction, and quality control features for
GoldenGate, Infinium, and Infinium HD arrays are also included.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.1-1
- initial package for Fedora