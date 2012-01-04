%global packname  davidTiling
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.14
Release:          1%{?dist}
Summary:          Data and analysis scripts for David, Huber et al. yeast tiling array paper

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-tilingArray R-GO.db 

BuildRequires:    R-devel tex(latex) R-Biobase R-tilingArray R-GO.db 

%description
This package contains the data for the paper by L. David et al. in PNAS
2006 (PMID 16569694): 8 CEL files of Affymetrix genechips, an
ExpressionSet object with the raw feature data, a probe annotation data
structure for the chip and the yeast genome annotation (GFF file) that was
used. In addition, some custom-written analysis functions are provided, as
well as R scripts in the scripts directory.

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
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.14-1
- initial package for Fedora