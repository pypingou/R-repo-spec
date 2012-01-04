%global packname  facsDorit
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.4
Release:          1%{?dist}
Summary:          DKFZ FACS example data

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-prada 

BuildRequires:    R-devel tex(latex) R-prada 

%description
FACS example data for cell-based assays. This data is used in the examples
and vignettes of the package prada.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.4-1
- initial package for Fedora