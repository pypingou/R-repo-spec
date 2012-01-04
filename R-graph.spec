%global packname  graph
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.32.0
Release:          1%{?dist}
Summary:          graph: A package to handle graph data structures

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
A package that implements some simple graph handling capabilities.

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
%doc %{rlibdir}/graph/doc
%doc %{rlibdir}/graph/html
%doc %{rlibdir}/graph/DESCRIPTION
%{rlibdir}/graph/NAMESPACE
%{rlibdir}/graph/R
%{rlibdir}/graph/perf
%{rlibdir}/graph/Scripts
%{rlibdir}/graph/GXL
%{rlibdir}/graph/help
%{rlibdir}/graph/INDEX
%{rlibdir}/graph/data
%{rlibdir}/graph/Meta
%{rlibdir}/graph/unitTests
%{rlibdir}/graph/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.32.0-1
- initial package for Fedora