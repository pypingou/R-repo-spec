%global packname  convert
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.30.0
Release:          1%{?dist}
Summary:          Convert Microarray Data Objects

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-limma R-marray R-utils R-methods 


BuildRequires:    R-devel tex(latex) R-Biobase R-limma R-marray R-utils R-methods



%description
Define coerce methods for microarray data objects.

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
%doc %{rlibdir}/convert/DESCRIPTION
%doc %{rlibdir}/convert/html
%doc %{rlibdir}/convert/doc
%{rlibdir}/convert/Meta
%{rlibdir}/convert/NAMESPACE
%{rlibdir}/convert/INDEX
%{rlibdir}/convert/R
%{rlibdir}/convert/help

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.30.0-1
- initial package for Fedora