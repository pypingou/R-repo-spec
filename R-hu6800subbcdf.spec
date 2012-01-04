%global packname  hu6800subbcdf
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.9.1
Release:          1%{?dist}
Summary:          hu6800subbcdf

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/data/annotation/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/annotation/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-utils R-AnnotationDbi 


BuildRequires:    R-devel tex(latex) R-utils R-AnnotationDbi



%description
A package containing an environment representing the Hu6800subB.CDF file.

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.9.1-1
- initial package for Fedora