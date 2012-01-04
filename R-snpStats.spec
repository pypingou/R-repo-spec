%global packname  snpStats
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.0
Release:          1%{?dist}
Summary:          SnpMatrix and XSnpMatrix classes and methods

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-survival R-methods R-Matrix 

BuildRequires:    R-devel tex(latex) R-survival R-methods R-Matrix 

%description
Classes and statistical methods for large SNP association studies,
extending the snpMatrix package

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
%doc %{rlibdir}/snpStats/html
%doc %{rlibdir}/snpStats/doc
%doc %{rlibdir}/snpStats/DESCRIPTION
%{rlibdir}/snpStats/NAMESPACE
%{rlibdir}/snpStats/help
%{rlibdir}/snpStats/INDEX
%{rlibdir}/snpStats/Meta
%{rlibdir}/snpStats/data
%{rlibdir}/snpStats/R
%{rlibdir}/snpStats/libs
RPM build errors:
%{rlibdir}/snpStats/extdata

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.0-1
- initial package for Fedora