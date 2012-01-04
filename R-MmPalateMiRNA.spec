%global packname  MmPalateMiRNA
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          Murine Palate miRNA Expression Analysis

Group:            Applications/Engineering 
License:          LGPL-3
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-Biobase R-xtable R-limma R-statmod R-lattice R-vsn 
Requires:         R-limma R-lattice R-Biobase 

BuildRequires:    R-devel tex(latex) R-methods R-Biobase R-xtable R-limma R-statmod R-lattice R-vsn
BuildRequires:    R-limma R-lattice R-Biobase 


%description
R package compendium for the analysis of murine palate miRNA two-color
expression data.

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.0-1
- initial package for Fedora