%global packname  VanillaICE
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.16.1
Release:          1%{?dist}
Summary:          A Hidden Markov Model for high throughput genotyping arrays

Group:            Applications/Engineering 
License:          LGPL-2
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-IRanges R-oligoClasses R-methods R-stats 
Requires:         R-SNPchip R-stats R-Biobase R-lattice R-utils R-IRanges R-grid 

BuildRequires:    R-devel tex(latex) R-IRanges R-oligoClasses R-methods R-stats
BuildRequires:    R-SNPchip R-stats R-Biobase R-lattice R-utils R-IRanges R-grid 


%description
Hidden Markov Models for characterizing chromosomal alterations in high
throughput SNP arrays

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
* Mon Dec 12 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.16.1-1
- initial package for Fedora