%global packname  mosaics
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          MOSAiCS (MOdel-based one and two Sample Analysis and Inference for ChIP-Seq)

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-graphics 
Requires:         R-MASS R-splines R-lattice R-IRanges 

BuildRequires:    R-devel tex(latex) R-methods R-graphics
BuildRequires:    R-MASS R-splines R-lattice R-IRanges 


%description
This package provides functions for fitting MOSAiCS, a statistical
framework to analyze one-sample or two-sample ChIP-seq data.

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
%doc %{rlibdir}/mosaics/html
%doc %{rlibdir}/mosaics/doc
%doc %{rlibdir}/mosaics/DESCRIPTION
%{rlibdir}/mosaics/help
%{rlibdir}/mosaics/Meta
%{rlibdir}/mosaics/R
%{rlibdir}/mosaics/INDEX
%{rlibdir}/mosaics/NAMESPACE

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.0-1
- initial package for Fedora