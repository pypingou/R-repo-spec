%global packname  preprocessCore
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.16.0
Release:          1%{?dist}
Summary:          A collection of pre-processing functions

Group:            Applications/Engineering 
License:          LGPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
A library of core preprocessing routines

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
%doc %{rlibdir}/preprocessCore/html
%doc %{rlibdir}/preprocessCore/DESCRIPTION
%{rlibdir}/preprocessCore/NAMESPACE
%{rlibdir}/preprocessCore/include
%{rlibdir}/preprocessCore/help
%{rlibdir}/preprocessCore/Meta
%{rlibdir}/preprocessCore/INDEX
%{rlibdir}/preprocessCore/R
%{rlibdir}/preprocessCore/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.16.0-1
- initial package for Fedora