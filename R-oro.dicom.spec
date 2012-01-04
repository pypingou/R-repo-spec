%global packname  oro.dicom
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          Rigorous - DICOM Input / Output

Group:            Applications/Engineering 
License:          BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-utils 

BuildRequires:    R-devel tex(latex) R-utils 

%description
Data input/output functions for data that conform to the Digital Imaging
and Communications in Medicine (DICOM) standard, part of the Rigorous
Analytics bundle.

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
%doc %{rlibdir}/oro.dicom/CITATION
%doc %{rlibdir}/oro.dicom/DESCRIPTION
%doc %{rlibdir}/oro.dicom/html
%{rlibdir}/oro.dicom/sphere3
%{rlibdir}/oro.dicom/data
%{rlibdir}/oro.dicom/hk-40
%{rlibdir}/oro.dicom/R
%{rlibdir}/oro.dicom/INDEX
%{rlibdir}/oro.dicom/help
%{rlibdir}/oro.dicom/Meta
%{rlibdir}/oro.dicom/dcm
%{rlibdir}/oro.dicom/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.1-1
- initial package for Fedora