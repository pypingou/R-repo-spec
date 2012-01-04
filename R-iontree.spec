%global packname  iontree
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Data management and analysis of ion trees from ion-trap mass spectrometry

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-rJava R-RSQLite R-XML 

BuildRequires:    R-devel tex(latex) R-methods R-rJava R-RSQLite R-XML 

%description
Ion fragmentation provides structural information for metabolite
identification. This package provides utility functions to manage and
analyse MS2/MS3 fragmentation data from ion trap mass spectrometry. It was
designed for high throughput metabolomics data with many biological
samples and a large numer of ion trees collected. Tests have been done
with data from low-resolution mass spectrometry but could be readily
extended to precursor ion based fragmentation data from high resoultion
mass spectrometry.

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora