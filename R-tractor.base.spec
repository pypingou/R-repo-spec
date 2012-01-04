%global packname  tractor.base
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.0.8
Release:          1%{?dist}
Summary:          A package for reading, manipulating and visualising magnetic resonance images

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-graphics R-grDevices R-methods R-stats R-utils 
Requires:         R-reportr 

BuildRequires:    R-devel tex(latex) R-graphics R-grDevices R-methods R-stats R-utils
BuildRequires:    R-reportr 


%description
The tractor.base package consists of functions for working with magnetic
resonance images. It can read and write image files stored in Analyze,
NIfTI and DICOM formats (DICOM support is read only), generate images for
use as regions of interest, and manipulate and visualise images.

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
%doc %{rlibdir}/tractor.base/html
%doc %{rlibdir}/tractor.base/DESCRIPTION
%doc %{rlibdir}/tractor.base/CITATION
%doc %{rlibdir}/tractor.base/LICENCE
%{rlibdir}/tractor.base/help
%{rlibdir}/tractor.base/Meta
%{rlibdir}/tractor.base/data
%{rlibdir}/tractor.base/INDEX
%{rlibdir}/tractor.base/R
%{rlibdir}/tractor.base/NAMESPACE

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.8-1
- initial package for Fedora