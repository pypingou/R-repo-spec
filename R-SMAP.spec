%global packname  SMAP
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.18.0
Release:          1%{?dist}
Summary:          A Segmental Maximum A Posteriori Approach to Array-CGH Copy Number Profiling

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
Functions and classes for DNA copy number profiling of array-CGH data

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
%doc %{rlibdir}/SMAP/doc
%doc %{rlibdir}/SMAP/DESCRIPTION
%doc %{rlibdir}/SMAP/html
%{rlibdir}/SMAP/INDEX
%{rlibdir}/SMAP/Meta
%{rlibdir}/SMAP/NAMESPACE
%{rlibdir}/SMAP/libs
%{rlibdir}/SMAP/R
%{rlibdir}/SMAP/data
%{rlibdir}/SMAP/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.18.0-1
- initial package for Fedora