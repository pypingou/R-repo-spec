%global packname  TxDb.Dmelanogaster.UCSC.dm3.ensGene
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.6.2
Release:          1%{?dist}
Summary:          Annotation package for the Dmelanogaster_UCSC_dm3_ensGene_TxDb object

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/data/annotation/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/annotation/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-GenomicFeatures 

BuildRequires:    R-devel tex(latex) R-GenomicFeatures 

%description
Contains the Dmelanogaster_UCSC_dm3_ensGene_TxDb object annotation
database as generated from UCSC

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
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.6.2-1
- initial package for Fedora