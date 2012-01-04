%global packname  RBGL
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.30.1
Release:          1%{?dist}
Summary:          An interface to the BOOST graph library

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-graph R-methods 

BuildRequires:    R-devel tex(latex) R-graph R-methods 

%description
A fairly extensive and comprehensive interface to the graph algorithms
contained in the BOOST library.

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
%doc %{rlibdir}/RBGL/DESCRIPTION
%doc %{rlibdir}/RBGL/doc
%doc %{rlibdir}/RBGL/html
%doc %{rlibdir}/RBGL/NEWS
%{rlibdir}/RBGL/libs
%{rlibdir}/RBGL/Meta
%{rlibdir}/RBGL/data
%{rlibdir}/RBGL/dot
%{rlibdir}/RBGL/dtd
%{rlibdir}/RBGL/XML
%{rlibdir}/RBGL/demos
%{rlibdir}/RBGL/R
%{rlibdir}/RBGL/help
%{rlibdir}/RBGL/boostExamples
%{rlibdir}/RBGL/NAMESPACE
%{rlibdir}/RBGL/fdep.ps
RPM build errors:
%{rlibdir}/RBGL/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.30.1-1
- initial package for Fedora