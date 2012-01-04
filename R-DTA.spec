%global packname  DTA
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Dynamic Transcriptome Analysis

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-LSD 
Requires:         R-scatterplot3d 

BuildRequires:    R-devel tex(latex) R-LSD
BuildRequires:    R-scatterplot3d 


%description
Dynamic Transcriptome Analysis (DTA) can monitor the cellular response to
perturbations with higher sensitivity and temporal resolution than
standard transcriptomics. The package implements the underlying kinetic
modeling approach capable of the precise determination of synthesis- and
decay rates from individual microarray or RNAseq measurements.

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
%doc %{rlibdir}/DTA/DESCRIPTION
%doc %{rlibdir}/DTA/doc
%doc %{rlibdir}/DTA/html
%{rlibdir}/DTA/NAMESPACE
%{rlibdir}/DTA/INDEX
%{rlibdir}/DTA/Meta
%{rlibdir}/DTA/help
%{rlibdir}/DTA/R
%{rlibdir}/DTA/data

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora