%global packname  gageData
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.3
Release:          1%{?dist}
Summary:          Auxillary data for gage package

Group:            Applications/Engineering 
License:          GPL (>=2.0)
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This is a supportive data package for the software package, gage. However,
the data supplied here are also useful for gene set or pathway analysis or
microarray data analysis in general. In this package, we provide two demo
microarray dataset: GSE16873 (a breast cancer dataset from GEO) and BMP6
(originally published as an demo dataset for GAGE, also registered as
GSE13604 in GEO). This package also includes commonly used gene set data
based on KEGG pathways and GO terms for major research species, including
human, mouse, rat and budding yeast. Mapping data between common gene IDs
for budding yeast are also included.

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
%doc %{rlibdir}/gageData/DESCRIPTION
%doc %{rlibdir}/gageData/html
%{rlibdir}/gageData/NAMESPACE
%{rlibdir}/gageData/help
%{rlibdir}/gageData/data
%{rlibdir}/gageData/Meta
%{rlibdir}/gageData/INDEX

%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.3-1
- initial package for Fedora