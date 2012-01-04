%global packname  Mulcom
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.0
Release:          1%{?dist}
Summary:          Calculates Mulcom test

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-fields R-Biobase 

BuildRequires:    R-devel tex(latex) R-fields R-Biobase 

%description
Identification of differentially expressed genes and false discovery rate
(FDR) calculation by Multiple Comparison test

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.0-1
- initial package for Fedora