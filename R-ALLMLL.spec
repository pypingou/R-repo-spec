%global packname  ALLMLL
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.11
Release:          1%{?dist}
Summary:          A subset of arrays from a large acute lymphoblastic leukemia (ALL) study

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-affy 

BuildRequires:    R-devel tex(latex) R-affy 

%description
This package provides probe-level data for 20 HGU133A and 20 HGU133B
arrays which are a subset of arrays from a large ALL study. The data is
for the MLL arrays. This data was published in Mary E. Ross, Xiaodong
Zhou, Guangchun Song, Sheila A. Shurtleff, Kevin Girtman, W. Kent
Williams, Hsi-Che Liu, Rami Mahfouz, Susana C. Raimondi, Noel Lenny, Anami
Patel, and James R. Downing (2003) Classification of pediatric acute
lymphoblastic leukemia by gene expression profiling Blood 102: 2951-2959

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.11-1
- initial package for Fedora