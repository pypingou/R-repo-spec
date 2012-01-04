%global packname  limma
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          3.10.0
Release:          1%{?dist}
Summary:          Linear Models for Microarray Data

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
Data analysis, linear models and differential expression for microarray

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
%doc %{rlibdir}/limma/doc
%doc %{rlibdir}/limma/html
%doc %{rlibdir}/limma/CITATION
%doc %{rlibdir}/limma/DESCRIPTION
%{rlibdir}/limma/libs
%{rlibdir}/limma/help
%{rlibdir}/limma/Meta
%{rlibdir}/limma/NEWS.Rd
%{rlibdir}/limma/R
RPM build errors:
%{rlibdir}/limma/NAMESPACE
%{rlibdir}/limma/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.10.0-1
- initial package for Fedora