%global packname  stepNorm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.26.0
Release:          1%{?dist}
Summary:          Stepwise normalization functions for cDNA microarrays

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-marray R-methods 

BuildRequires:    R-devel tex(latex) R-marray R-methods 

%description
Stepwise normalization functions for cDNA microarray data.

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
* Fri Nov 25 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.26.0-1
- initial package for Fedora