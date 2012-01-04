%global packname  copa
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.22.0
Release:          1%{?dist}
Summary:          Functions to perform cancer outlier profile analysis.

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-methods 


BuildRequires:    R-devel tex(latex) R-Biobase R-methods



%description
COPA is a method to find genes that undergo recurrent fusion in a given
cancer type by finding pairs of genes that have mutually exclusive outlier

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
%doc %{rlibdir}/copa/html
%doc %{rlibdir}/copa/CITATION
%doc %{rlibdir}/copa/doc
%doc %{rlibdir}/copa/DESCRIPTION
%{rlibdir}/copa/INDEX
%{rlibdir}/copa/Meta
%{rlibdir}/copa/NAMESPACE
%{rlibdir}/copa/libs
%{rlibdir}/copa/R
%{rlibdir}/copa/help

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.22.0-1
- initial package for Fedora