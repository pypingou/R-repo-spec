%global packname  IRanges
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.12.6
Release:          1%{dist}
Summary:          Infrastructure for manipulating intervals on sequences

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-utils R-stats 

BuildRequires:    R-devel tex(latex) R-methods R-utils R-stats 

%description
The package provides efficient low-level and highly reusable S4 classes
for storing ranges of integers, RLE vectors (Run-Length Encoding), and,
more generally, data that can be organized sequentially (formally defined
as Vector objects), as well as views on these Vector objects. Efficient
list-like classes are also provided for storing big collections of
instances of the basic classes. All classes in the package use consistent
naming and share the same rich and consistent "Vector API" as much as

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
%doc %{rlibdir}/IRanges/html
%doc %{rlibdir}/IRanges/doc
%doc %{rlibdir}/IRanges/NEWS
%doc %{rlibdir}/IRanges/DESCRIPTION
%{rlibdir}/IRanges/help
%{rlibdir}/IRanges/Meta
%{rlibdir}/IRanges/extdata
%{rlibdir}/IRanges/INDEX
%{rlibdir}/IRanges/unitTests
%{rlibdir}/IRanges/R
%{rlibdir}/IRanges/libs
%{rlibdir}/IRanges/include
%{rlibdir}/IRanges/NAMESPACE

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 1.12.6-1
- Update to version 1.12.6

* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.12.1-1
- initial package for Fedora