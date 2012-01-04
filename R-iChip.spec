%global packname  iChip
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.8.0
Release:          1%{?dist}
Summary:          Bayesian Modeling of ChIP-chip Data Through Hidden Ising Models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-limma 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-limma 


%description
This package uses hidden Ising models to identify enriched genomic regions
in ChIP-chip data.  It can be used to analyze the data from multiple
platforms (e.g., Affymetrix, Agilent, and NimbleGen), and the data with
single to multiple replicates.

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
%doc %{rlibdir}/iChip/html
%doc %{rlibdir}/iChip/DESCRIPTION
%doc %{rlibdir}/iChip/doc
%{rlibdir}/iChip/NAMESPACE
%{rlibdir}/iChip/R
%{rlibdir}/iChip/data
%{rlibdir}/iChip/INDEX
%{rlibdir}/iChip/Meta
%{rlibdir}/iChip/demo
%{rlibdir}/iChip/help
%{rlibdir}/iChip/libs

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.8.0-1
- initial package for Fedora