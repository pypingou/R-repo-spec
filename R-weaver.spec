%global packname  weaver
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.20.0
Release:          1%{?dist}
Summary:          Tools and extensions for processing Sweave documents

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-digest R-tools R-utils R-codetools 


BuildRequires:    R-devel tex(latex) R-digest R-tools R-utils R-codetools



%description
This package provides enhancements on the Sweave() function in the base
package.  In particular a facility for caching code chunk results is

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
%doc %{rlibdir}/weaver/html
%doc %{rlibdir}/weaver/DESCRIPTION
%doc %{rlibdir}/weaver/doc
%{rlibdir}/weaver/Meta
%{rlibdir}/weaver/NAMESPACE
%{rlibdir}/weaver/extdata
%{rlibdir}/weaver/R
%{rlibdir}/weaver/help
%{rlibdir}/weaver/INDEX

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.20.0-1
- initial package for Fedora