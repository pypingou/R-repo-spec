%global packname  lumiHumanIDMapping
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.10.0
Release:          1%{?dist}
Summary:          Illumina Identifier mapping for Human

Group:            Applications/Engineering 
License:          The Artistic License, Version 2.0
URL:              http://bioconductor.org/packages/release/data/annotation/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/annotation/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lumi R-methods R-AnnotationDbi 

BuildRequires:    R-devel tex(latex) R-lumi R-methods R-AnnotationDbi 

%description
This package includes mappings information between different types of
Illumina IDs of Illumina Human chips and nuIDs. It also includes mappings
of all nuIDs included in Illumina Human chips to RefSeq IDs with mapping
qualities information.

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
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.10.0-1
- initial package for Fedora