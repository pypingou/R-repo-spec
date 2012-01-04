%global packname  ProData
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.5
Release:          1%{?dist}
Summary:          SELDI-TOF data of Breast cancer samples

Group:            Applications/Engineering 
License:          GPL
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Biobase 

BuildRequires:    R-devel tex(latex) R-Biobase 

%description
A data package of SELDI-TOF protein mass spectrometry data of 167 breast
cancer and normal samples.

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
%doc %{rlibdir}/ProData/DESCRIPTION
%doc %{rlibdir}/ProData/html
%{rlibdir}/ProData/NAMESPACE
%{rlibdir}/ProData/INDEX
%{rlibdir}/ProData/help
%{rlibdir}/ProData/data
%{rlibdir}/ProData/Meta
%{rlibdir}/ProData/f45c

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.5-1
- initial package for Fedora